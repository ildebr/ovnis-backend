from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterUsersSerializer, NewUserSerializer
from rest_framework import generics
from users.models import NewUser
# Create your views here.


class CustomUserCreate(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		reg_serializaer = RegisterUsersSerializer(data=request.data)
		val = reg_serializaer.is_valid()
		print(reg_serializaer.errors)
		if reg_serializaer.is_valid():
			newuser = reg_serializaer.save()
			if newuser:
				return Response(status=status.HTTP_201_CREATED)
		return Response(reg_serializaer.errors, status=status.HTTP_400_BAD_REQUEST)


#Usuarios

class CurrentUser(APIView):
	permission_classes = [IsAuthenticated]
	print('alo')
	def post(self, request):
		print(request.user)
		user = request.user
		queryset = NewUser.objects.filter(user=user)
		return queryset

class UserList(generics.ListCreateAPIView):
	queryset = NewUser.objects.all()
	serializer_class = NewUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = NewUser.objects.all()
	serializer_class = NewUserSerializer