from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo


class TodoView(APIView):

    serializer_class = TodoSerializer

    def get(self, request, pk=None):  # to retrieve records
        if pk is None:
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
        else:
            todo = Todo.objects.get(id=pk)
            serializer = TodoSerializer(todo)

        return Response(serializer.data)

    def post(self, request):  # to create new records
        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):  # to amend records
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):  # to delete records
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
