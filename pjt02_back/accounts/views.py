from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# Create your views here.
@api_view(['POST'])
def signup(request):
  # 클라이언트가 username과 password를 보낼건데
  # user를 만들어 저장
  # 저장한 user를 리턴
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    user = serializer.save()
    user.set_email(request.data.get('email'))
    user.set_password(request.data.get('password'))
    user.save()
    return Response(serializer.data)