from rest_framework import viewsets
from .serializers import AboutSerializer, HistorySerializer, NewsSerializer, HomeSerializer
from .models import AboutTeam, History, News, Home
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class NewsAndHomeViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    serializer_class_news = NewsSerializer
    serializer_class_home = HomeSerializer 
    def get_queryset_News(self):
        return News.objects.all()

    def get_queryset_Home(self):
        return Home.objects.all()

    def list(self, request, *args, **kwargs):
        news = self.serializer_class_news(self.get_queryset_News(), many=True)
        home = self.serializer_class_home(self.get_queryset_Home(), many=True)
        
        return Response ({
            "**News**": news.data,
            "**Home**": home.data
        })
    
    
    def retrieve(self, request, pk=None ,*args, **kwargs):
        queryset =News.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        #title = self.kwargs.get('id')
        serializer = NewsSerializer(instance)
       
        return Response(serializer.data)
   
"""
    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset =Home.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = HomeSerializer(instance)

        return Response(serializer.data)
"""


class AboutViewset(viewsets.ReadOnlyModelViewSet): 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = AboutTeam.objects.all()
    serializer_class = AboutSerializer 
 

class HistoryViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = History.objects.all()
    serializer_class = HistorySerializer 

