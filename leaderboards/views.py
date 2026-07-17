from django.db.models import F, Window
from django.db.models.functions import RowNumber
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import LeaderboardSerializer
from test_results.models import TestResults

# note: views are functions or class object methods that take in http requests as parameters and return http responses



#
class LeaderboardPagination(PageNumberPagination):
    page_size = 50

# 
class LeaderboardAPIView(APIView):

    # variable populated with ALL test results entry rows of sql table
    queryset = TestResults.objects.all()

    def get(self, request):
        # save query params filters to vars
        test_type = request.query_params.get('test_type')
        specialization_field = request.query_params.get('specialization_field')
        # entry_id = request.query_params.get('entry_id')
        # use query params to grab all entries that match request test_type and specialization_field
        filtered_results = self.queryset.filter(
            test_type=test_type,
            test_specialization_field=specialization_field
            )
        # order returned query results by test_overall_score
        ordered_results = filtered_results.order_by('-test_overall_score')
        # assign rank field to each row based on currently ordered queryset (that is ordered by highest to lowest score)
        ranked_results = ordered_results.annotate(
            rank=Window(
                expression=RowNumber(),
                order_by=F('test_overall_score').desc()
            )
        )

        # declare paginator due to class being an APIView type
        paginator = LeaderboardPagination()
        # declare serializer to be used to return response data
        leaderboard_serializer_class = LeaderboardSerializer

        # paginate ranked results manually because of custom actions
        page = paginator.paginate_queryset(ranked_results, request)
        # serialize the data before returning the response
        serializer_instance = leaderboard_serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer_instance.data)





# # Handles public leaderboard get/put/push/post requests
# class PublicLeaderboards(View):
    
#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PublicLeaderboards class in leaderboards django app')


# # Handles public leaderboard get/put/push/post requests
# class PrivateLeaderboard(View):

#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PrivateLeaderboard class in leaderboards django app')


