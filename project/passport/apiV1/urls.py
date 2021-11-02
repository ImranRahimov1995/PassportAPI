from .views import *
from django.urls import path

urlpatterns = [
    path('passport/all/',PassportListView.as_view()),
    path('customer/all/',CustomerListView.as_view()),
    path('passport/<str:personal>/',PassportDetailView.as_view()),
    path('customer/<str:phone>/',CustomerDetailView.as_view()),
    path('create/',JoinedCreateView.as_view()),
]