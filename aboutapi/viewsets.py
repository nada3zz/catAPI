from rest_framework import viewsets
from .import models
from.import serializers

class AboutTeamViewset(viewsets.ModelViewSet):
    queryset = models.AboutTeam.objects.all()
    serializer_class = serializers.AboutTeamSerializer 

class CirclesViewset(viewsets.ModelViewSet):
    queryset = models.Circles.objects.all()
    serializer_class = serializers.CirclesSerializer 

class HeadInfoViewset(viewsets.ModelViewSet):
    queryset = models.HeadsInfo.objects.all()
    serializer_class = serializers.HeadInfoSerializer 

class TopMembersViewset(viewsets.ModelViewSet):
    queryset = models.TopMembers.objects.all()
    serializer_class = serializers.TopMembersSerializer 

class EventViewset(viewsets.ModelViewSet):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventSerializer 