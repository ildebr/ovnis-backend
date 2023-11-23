from rest_framework import serializers
from .models import Sighting, Comment
from users.models import NewUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ("user_name",)

class SightingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model= Sighting
        fields= ('id','title','description', 'latitude', 'longitude','date','user', 'country','continent')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('date', 'text', 'sighting', 'user')

class ApiNewSightingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sighting
        fields= ('id','title','description', 'latitude', 'longitude')
        optional_field = ['id',]
    def create(self, validated_data):
        user = self.context['user']
        print(user)
        sighting = Sighting.objects.create(
            user=user, 
            **validated_data
        )
        return sighting
