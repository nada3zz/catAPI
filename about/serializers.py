from rest_framework import serializers
from .models import History, News, AboutTeam

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'date', 'achievments_en','achievments_ar')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title_en','title_ar', 'body_en','body_ar', 'image', 'publish', 'updated')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTeam
        fields = ('id', 'title_en','title_ar', 'body_en', 'body_ar')

