from rest_framework import serializers
from .models import Todolist,Category



class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'