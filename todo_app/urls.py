from django.urls import path
from .views import TodolistList
from .views import TodolistDetail

urlpatterns = [
    path('todolist/', TodolistList.as_view(), name = "My-todo-list"),
    path('todolist_modify/<int:pk>/', TodolistDetail.as_view(), name = 'My-todo-list-update')
]
