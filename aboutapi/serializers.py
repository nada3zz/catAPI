from rest_framework import serializers
from .models import EventSession,Event,HeadInfo,History,TeamBoard,TechCircle,News,NonTechCircle,TopMember, AboutTeam

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSession
        fields = '__all__'
 
class HeadInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadInfo
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamBoard
        fields = '__all__'

class TechCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCircle
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NonTechCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonTechCircle
        fields = '__all__'

class TopMemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopMember
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTeam
        fields = '__all__'