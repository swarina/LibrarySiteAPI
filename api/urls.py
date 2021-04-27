from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path('api', BookAPIView.as_view()),
]
