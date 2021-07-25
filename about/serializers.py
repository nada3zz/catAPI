from rest_framework import serializers
from .models import History, News, AboutTeam, Home
from events.models import Event
from events.serializers import EventSerializer

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'title', 'body', 'image')
        
class HistorySerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()
    class Meta:
        model = History
        fields = ('id', 'date', 'achievments','events')
    def get_events(self, obj):
        qs = Event.objects.filter(date__year=obj.date.year)
        return EventSerializer(qs, many=True).data

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'body', 'image', 'publish', 'updated')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTeam
        fields = ('id', 'title','body')

