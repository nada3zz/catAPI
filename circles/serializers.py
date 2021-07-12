from rest_framework import serializers
from .models import TechCircle, NonTechCircle

class TechCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCircle
        fields = ('id','title', 'description', 'designtools', 'RMlink', 'title', 'description', 'designtools')


class NonTechCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonTechCircle
        fields = ('id','title', 'description', 'skills', 'title', 'description', 'skills')
