from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

urlpatterns = [
    path('sensors/', ListCreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateDestroyAPIView.as_view()),
    path('measurements/', CreateAPIView.as_view()),
]
