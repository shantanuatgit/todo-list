from django.urls import path, include
from todoapp import views


urlpatterns = [
    path('task/', views.TodoList.as_view(), name='todo-list'),
    path('task/<int:pk>/', views.TodoListDetail.as_view(), name='todo-list'),
]