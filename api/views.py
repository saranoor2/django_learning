from rest_framework import status
from rest_framework.response import Response  # ✅ fixed
from .models import Ad
from .serializers import AdSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    @action(detail=True, methods=['post']) 
    def post_random_ads(self, request, pk=None):
        # this function works if the given id is present in the db; http://127.0.0.1:8000/ads/7/post_random_ads/
        ad = self.get_object() 
        serializer = self.get_serializer(ad)
        return Response({'message': f'Ad "{ad.title}" posted!', 'ad': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def get_random_ads(self, request):
        ads = Ad.objects.order_by('?')[:5]  # Get 5 random ads
        if not ads:
            return Response({'ads': []}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(ads, many=True)
        return Response({'ads': serializer.data}, status=status.HTTP_200_OK)
    
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
