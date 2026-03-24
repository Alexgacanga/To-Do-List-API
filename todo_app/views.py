from django.shortcuts import render
from rest_framework import generics
from .serializers import TodolistSerializer
from .models import Todolist


class TodolistList(generics.ListCreateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer

class TodolistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    lookup_field = "pk"