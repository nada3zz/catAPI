from rest_framework import viewsets
from .import models
from.import serializers
from rest_framework import permissions
"""
class AboutTeamViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.AboutTeam.objects.all()
    serializer_class = serializers.AboutTeamSerializer 

class CirclesViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.Circles.objects.all()
    serializer_class = serializers.CirclesSerializer 

class HeadInfoViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.HeadsInfo.objects.all()
    serializer_class = serializers.HeadInfoSerializer 

class TopMembersViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.TopMembers.objects.all()
    serializer_class = serializers.TopMembersSerializer 

class EventViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventSerializer 
"""