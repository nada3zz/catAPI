from django.db.models import fields
from rest_framework import serializers
from .models import EventPhoto, EventSession, Event




class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =('id', 'title_en','title_ar', 'date')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSession
        fields = ('id', 'title_en', 'description_en', 'event_name_en', 'sessionlink', 'title_ar','description_ar', 'event_name_ar')
 
class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model= EventPhoto
        fields= ('id', 'image', 'session_name', 'created', 'updated') 