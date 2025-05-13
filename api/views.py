from rest_framework import status
from rest_framework.response import Response  # ✅ fixed
from .models import Ad
from .serializers import AdSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    @action(detail=True, methods=['post'])  # ✅ use detail=True to get one Ad
    def post_random_ads(self, request, pk=None):
        ad = self.get_object()  # ✅ now this works
        # Your custom logic here, e.g., simulate ad publishing
        return Response({'message': f'Ad "{ad.title}" posted!'}, status=status.HTTP_200_OK)
# class AdAPI(APIView):
#     def get_object(self, pk):
#         try:
#             return Ad.objects.get(pk=pk)
#         except Ad.DoesNotExist:
#             raise Http404
#     def get(self, request):
#         ads = Ad.objects.all()
#         serializer = AdSerializer(ads, many=True)
#         return Response(serializer.data)
#         # items = ['apples','mangoes','banana']
#         # response_data = {"data": items}
#         # return Response(response_data,status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = AdSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, pk):
#         book = self.get_object(pk)
#         serializer = AdSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def get_random(self, request):
#         items = ['apples','mangoes','banana']
#         response_data = {"data": items}
#         return Response(response_data,status=status.HTTP_200_OK)
    

#     @action(detail=True, methods=['post'])
#     def publish_random_ad(self, request, pk=None):
#         book = self.get_object()
#         # your logic here
#         return Response({'message': f'Book "{book.title}" published!'})
