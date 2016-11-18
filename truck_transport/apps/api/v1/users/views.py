from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from rest_framework.decorators import api_view, permission_classes

from .serializers import *

@csrf_exempt
@api_view(['POST'])
def register(request):
    serialized = RegistrationSerializer(data=request.data)
    print serialized
    if serialized.is_valid():
        username = serialized.data['username']
        email = serialized.data['email']
        password = serialized.data['password']
        phone = serialized.data['phone']
        User.objects.create_user(username, email, password)   
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
