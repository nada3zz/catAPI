from rest_framework import viewsets
from .models import MemberInfo,MemberRole
from.serializers import MemberInfoSerializer
from rest_framework import permissions

class MemberInfoViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = MemberInfo.objects.all()
    serializer_class = MemberInfoSerializer 
 