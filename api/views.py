from rest_framework import status
from rest_framework.views import APIView, Response

# class AdAPI(APIView):
#     def get(self, request):
#         items = ['apples','mangoes','banana']
#         response_data = {"data": items}
#         return Response(response_data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         response_data = {"response":"Hello Its Post method"}
#         return Response(response_data,status=status.HTTP_200_OK)

class CreateListing(APIView):
    def post(self, request):
        return Response({"message": "Listing created"}, status=status.HTTP_201_CREATED)

class ReadListing(APIView):
    def get(self, request):
        return Response({"message": "Here are the listings"}, status=status.HTTP_200_OK)

class UpdateListing(APIView):
    def put(self, request):
        return Response({"message": "Listing updated"}, status=status.HTTP_200_OK)

class DeleteListing(APIView):
    def delete(self, request):
        return Response({"message": "Listing deleted"}, status=status.HTTP_204_NO_CONTENT)