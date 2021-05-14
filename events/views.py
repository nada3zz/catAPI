from rest_framework import viewsets
from .models import Event,EventPhoto,EventSession
from.serializers import EventSerializer, SessionSerializer, EventPhotoSerializer
from rest_framework import permissions

class EventViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = Event.objects.all()
    serializer_class = EventSerializer 
 
class SessionViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = EventSession.objects.all()
    serializer_class = SessionSerializer 

class EventPhotoViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = EventPhoto.objects.all()
    serializer_class = EventPhotoSerializer 

