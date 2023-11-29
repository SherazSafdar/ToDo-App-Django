from todo_handler.models import Task
from api.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_task(request):
    print(request.user)
    if request.method=='POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'PATCH', 'DELETE']) 
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])           
def retrieve_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error':'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
            
    if request.method=='GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class based

class CreateTaskView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TaskView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None

    def get(self, request, task_id):
        task = self.get_object(task_id)
        if task is not None:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, task_id):
        task = self.get_object(task_id)
        if task is not None:
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, task_id):
        task = self.get_object(task_id)
        if task is not None:
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, task_id):
        task = self.get_object(task_id)
        if task is not None:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)                
            
