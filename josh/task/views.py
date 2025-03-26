from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,Task
from .serializers import TaskSerializer,AssignTaskSerializer

class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class AssignTaskView(APIView):
    def post(self, request):
        serializer = AssignTaskSerializer(data=request.data)
        if serializer.is_valid():
            try:
                task = Task.objects.get(id=serializer.validated_data['task_id'])
                users = User.objects.filter(id__in=serializer.validated_data['user_ids'])
                task.users.set(users)
                return Response({'message': 'Task assigned successfully'}, status=status.HTTP_200_OK)
            except Task.DoesNotExist:
                return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTasksView(APIView):
    def get(self, request, user_id):
        tasks = Task.objects.filter(users__id=user_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
