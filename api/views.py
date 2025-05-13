from rest_framework import status
from rest_framework.views import APIView, Response

class AdAPI(APIView):
    def get(self, request):
        items = ['apples','mangoes','banana']
        response_data = {"data": items}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def post(self,request):
        response_data = {"response":"Hello Its Post method"}
        return Response(response_data,status=status.HTTP_200_OK)