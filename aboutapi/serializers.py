from rest_framework import serializers
from .models import AboutTeam, Circles, HeadsInfo, TopMembers, Events

class AboutTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model= AboutTeam
        fields= '__all__'

class CirclesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Circles
        fields= '__all__'

class HeadInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= HeadsInfo
        fields= '__all__'

class TopMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model= TopMembers
        fields= '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Events
        fields= '__all__'