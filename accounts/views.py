from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import AccountsSerializer


class ResgisterViewSet(viewsets.ViewSet):
    
    permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
