from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterUsersSerializer, NewUserSerializer
from rest_framework import generics
from users.models import NewUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from ovnis_api.models import Sighting
from ovnis_api.serializers import SightingSerializer, ApiNewSightingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
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
	# permission_classes = [IsAuthenticated]
	authentication_classes = [JWTAuthentication]
	print('alo')
	def post(self, request):
		user = request.user.id
		queryset = NewUser.objects.filter(id=user)
		serializer = NewUserSerializer(queryset, many=True)
		print(serializer.data)
		if serializer.data:
			return Response(serializer.data)
		else:
			Response(status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListCreateAPIView):
	queryset = NewUser.objects.all()
	serializer_class = NewUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = NewUser.objects.all()
	serializer_class = NewUserSerializer

class sightingEndpoint(generics.RetrieveUpdateDestroyAPIView):
	queryset = NewUser.objects.all()
	serializer_class = NewUserSerializer

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getNotes(request):
	print(request.user)
	print(request.user.first_name)
	print(request.user.id)
	notes = Sighting.objects.filter(user=request.user)
	serializer = SightingSerializer(notes, many=True)
	# notes = NewUser.objects.filter(id=request.user.id)
	# serializer = NewUserSerializer(notes, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createSighting(request):
	print(request.data)
	serializer = ApiNewSightingSerializer(data=request.data, context={'user': request.user})
	if serializer.is_valid():
		new_sighting = serializer.save()
		if new_sighting:
			return Response(serializer.data,status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
class updateSighting(UpdateAPIView):
	model = Sighting
	serializer_class = ApiNewSightingSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [JWTAuthentication]

	def get_queryset(self, *args, **kwargs):
		return Sighting.objects.filter(user=self.request.user)
	