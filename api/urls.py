from django.urls import path
# from .views import AdAPI

# urlpatterns = [
#     path('', AdAPI.as_view()),
# ]

from .views import CreateListing, ReadListing, UpdateListing, DeleteListing

urlpatterns = [
    path('create_listing/', CreateListing.as_view(), name='create_listing'),
    path('read_listing/', ReadListing.as_view(), name='read_listing'),
    path('update_listing/', UpdateListing.as_view(), name='update_listing'),
    path('delete_listing/', DeleteListing.as_view(), name='delete_listing'),
]