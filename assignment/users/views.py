from django.shortcuts import render
from rest_framework import viewsets
from .models import UserData
from .serializers import UserDataSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
class UserDataView(viewsets.ModelViewSet):
    queryset=UserData.objects.all()
    serializer_class=UserDataSerializer
    pagination_class=LimitOffsetPagination
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=['first_name']
    ordering_fields=['age']

