from rest_framework import serializers
from .models import User,Task
class UserSerializer(serializers.ModelSerializer):
    class Mets:
        model = User
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True,read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class AssignTaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    user_ids = serializers.ListField(child = serializers.IntegerField())


