from rest_framework import viewsets
from .import models
from .serializers import AboutSerializer, HistorySerializer, NewsSerializer
from.models import AboutTeam, History, News
from rest_framework import permissions

class AboutViewset(viewsets.ReadOnlyModelViewSet): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = AboutTeam.objects.all()
    serializer_class = AboutSerializer 

class NewsViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = News.objects.all()
    serializer_class = NewsSerializer 

class HistoryViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = History.objects.all()
    serializer_class = HistorySerializer 















