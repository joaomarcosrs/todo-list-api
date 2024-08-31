from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.response import Response


def custom_exceptions_handle(exc, context):
    if isinstance(exc, NotAuthenticated):
        return Response({'message': 'Unauthorized'}, status=401)
    
    if isinstance(exc, PermissionDenied):
        return Response({'message': 'Forbidden'}, status=403)
    
    return exception_handler(exc, context)