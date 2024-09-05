from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .serializers import TodoSerializer
from .models import Todo
from .utils import CustomPagination


class TodosViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
        
    def list(self, request):
        queryset = Todo.objects.all()
        
        paginator = CustomPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page:
            serializer = TodoSerializer(page, many=True)
            
            return paginator.get_paginated_response(serializer.data)
    
    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if todo.owner != request.user:
            raise PermissionDenied()
        
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if todo.owner != request.user:
            raise PermissionDenied()
        
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)