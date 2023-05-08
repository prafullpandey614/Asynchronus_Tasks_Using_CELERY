from django.urls import path
from .views import OverviewCreateAPIView
urlpatterns = [
    path('',OverviewCreateAPIView.as_view())
]