import requests
from rest_framework.views import APIView
from rest_framework.response import Response

# note: views are functions or class object methods that take in http requests as parameters and return http responses



#
class TextGeneratorAPIView(APIView):

    def post(self, request):
        # the url of the external backend api of text generator
        text_gen_url = 'http://localhost:5000/api/generate'

        # post request to text generator backend
        response = requests.post(text_gen_url, json=request.data)

        return Response(response.json(), status=response.status_code)
