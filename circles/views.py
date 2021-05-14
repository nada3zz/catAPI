from rest_framework import viewsets
from .import models
from .serializers import TechCircleSerializer, NonTechCircleSerializer
from.models import TechCircle, NonTechCircle
from rest_framework import permissions


class TechCircleViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = TechCircle.objects.all()
    serializer_class = TechCircleSerializer 


class NonTechCircleViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = NonTechCircle.objects.all()
    serializer_class = NonTechCircleSerializer 