from rest_framework import viewsets
from .import models
from.import serializers
from rest_framework import permissions

class AboutViewset(viewsets.ModelViewSet): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.AboutTeam.objects.all()
    serializer_class = serializers.AboutSerializer 

class NewsViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer 

class HistoryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializer 

class BoardViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.TeamBoard.objects.all()
    serializer_class = serializers.BoardSerializer

class EventViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer 
 
class SessionViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.EventSession.objects.all()
    serializer_class = serializers.SessionSerializer 

class TechCircleViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.TechCircle.objects.all()
    serializer_class = serializers.TechCircleSerializer 


class NonTechCircleViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.NonTechCircle.objects.all()
    serializer_class = serializers.NonTechCircleSerializer 


class HeadInfoViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.HeadInfo.objects.all()
    serializer_class = serializers.HeadInfoSerializer 

class TopMemberViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.TopMember.objects.all()
    serializer_class = serializers.TopMemSerializer 












