from django.db.models import fields
from rest_framework import serializers
from .models import EventPhoto, EventSession, Event




class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =('id', 'title', 'date')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSession
        fields = ('id', 'title', 'description', 'event', 'sessionlink',)
 
class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model= EventPhoto
        fields= ('id', 'image', 'session_name', 'created', 'updated') 