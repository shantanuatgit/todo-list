from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    task_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Task
        fields = '__all__'