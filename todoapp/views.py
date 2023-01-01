from django.shortcuts import render
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

class TodoList(generics.ListCreateAPIView, generics.GenericAPIView):
    
    """ display the currently added task in the list """

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['topic', 'category']

    def get_queryset(self):
        """
        This view should return a list of all the task
        for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(task_user=user)


class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdminOnly]