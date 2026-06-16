from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db.models import F, Window
from django.db.models.functions import RowNumber
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TestResultsSerializer
from .serializers import TestResultsLeaderboardSerializer
from .models import TestResults

# note: views are functions or class object methods that take in http requests as parameters and return http responses



# 
class TestResultsViewSet(viewsets.ModelViewSet):

    # assigning test results translation process (between JSON and django model instances) to serializer class TestResultsSerializer
    serializer_class = TestResultsSerializer

    # variable populated with ALL test results entry rows of sql table
    queryset = TestResults.objects.all()

    @action(detail=False, methods=['get'])
    def return_test_results_page_leaderboard(self, request):
        # save query params filters to vars
        test_type = request.query_params.get('test_type')
        specialization_field = request.query_params.get('specialization_field')
        entry_id = request.query_params.get('entry_id')
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
        # grab the user's row and their rank value of their entry row
        user_rank = ranked_results.filter(id=entry_id).values('rank')[0].get('rank')
        # grab length of user_results ONCE using len() will trigger a SELECT COUNT(*) sql query every time which is inefficient
        ranked_results_length = ranked_results.count()
        # declare serializer to be used to return response data
        leaderboard_serializer_class = TestResultsLeaderboardSerializer

        # if total entries is at least 51
        if ranked_results_length >= 51:
            # if user's rank is not in top 25 and not in bottom 25
            if user_rank > 25 and user_rank <= ranked_results_length - 25:
                # then grab the 25 rows above user rank and the 25 below and concatenate them into one list of object rows then return that list
                test_results_leaderboard_51rows = ranked_results[(user_rank - 26):(user_rank + 25):1]

                # serialize the data before returning response
                serializer_instance = leaderboard_serializer_class(test_results_leaderboard_51rows, many=True)
                return Response(serializer_instance.data)
            
            # else if user's rank is in the bottom 25
            elif user_rank > ranked_results_length - 25:
                # then grab the bottom 51 rows and return that list
                bottom_51rows = ranked_results[(ranked_results_length - 51):ranked_results_length:1]
                
                # serialize the data before returning response
                serializer_instance = leaderboard_serializer_class(bottom_51rows, many=True)
                return Response(serializer_instance.data)
            
            # else if user's rank is in the top 25
            elif user_rank <= 25:
                # then grab the top 51 rows and return that list
                top_51rows = ranked_results[0:51:1]

                # serialize the data before returning response
                serializer_instance = leaderboard_serializer_class(top_51rows, many=True)
                return Response(serializer_instance.data)
            
            else:
                return Response({'error': 'Unexpected error: paradox found'}, status=400)
            
        # else total entries is less than 51 currently so return all that is present
        else:
            # serialize the data before returning response
            serializer_instance = leaderboard_serializer_class(ranked_results, many=True)
            return Response(serializer_instance.data)



# Handles public leaderboard get/put/push/post requests
# class PublicLeaderboards(View):
    
#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PublicLeaderboards class in leaderboards django app')


# # Handles public leaderboard get/put/push/post requests
# class PrivateLeaderboard(View):

#     def get(self, request) -> HttpResponse:
#         return HttpResponse('im in the get method in PrivateLeaderboard class in leaderboards django app')


