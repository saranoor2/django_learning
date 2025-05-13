from rest_framework import status
from rest_framework.views import APIView, Response
from .models import Ad
from .serializers import AdSerializer

class AdAPI(APIView):
    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)
        # items = ['apples','mangoes','banana']
        # response_data = {"data": items}
        # return Response(response_data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        response_data = {"response":"Hello Its Put method"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, pk):
        response_data = {"response":"Hello Its Delete method"}
        return Response(response_data,status=status.HTTP_200_OK)
    
    def get_random(self, request):
        items = ['apples','mangoes','banana']
        response_data = {"data": items}
        return Response(response_data,status=status.HTTP_200_OK)

# class CreateListing(APIView):
#     def post(self, request):
#         return Response({"message": "Listing created"}, status=status.HTTP_201_CREATED)

# class ReadListing(APIView):
#     def get(self, request):
#         return Response({"message": "Here are the listings"}, status=status.HTTP_200_OK)

# class UpdateListing(APIView):
#     def put(self, request):
#         return Response({"message": "Listing updated"}, status=status.HTTP_200_OK)

# class DeleteListing(APIView):
#     def delete(self, request):
#         return Response({"message": "Listing deleted"}, status=status.HTTP_204_NO_CONTENT)