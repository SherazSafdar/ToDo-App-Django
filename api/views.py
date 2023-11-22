from todo_handler.models import Task
from api.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create_task(request):
    if request.method=='POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])            
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
    
    

        
    #elif request.method in ['PUT', 'PATCH']:
    #    task_id = request.data.get('id')
    #    
    #    if not task_id:
    #        return Response({'error': 'Task ID is required for update operations.'}, status=status.HTTP_400_BAD_REQUEST)

    #    try:
    #        task = Task.objects.get(id=task_id)
    #    except Task.DoesNotExist:
    #        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    #    if request.method == 'PUT':
    #        serializer = TaskSerializer(task, data=request.data)
    #    elif request.method == 'PATCH':
    #        serializer = TaskSerializer(task, data=request.data, partial=True)

    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data)
    #    else:
    #        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #elif request.method == 'DELETE':
    #    task_ids_to_delete = request.data.get('task_ids', [])
    #    tasks = Task.objects.filter(id__in=task_ids_to_delete)
    #    tasks.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)
    #return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)