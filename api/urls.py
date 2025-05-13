from django.urls import path
from .views import AdAPI

urlpatterns = [
    path('', AdAPI.as_view()),
]