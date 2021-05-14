from rest_framework import serializers
from .models import TechCircle, NonTechCircle

class TechCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCircle
        fields = ('id','title_en', 'description_en', 'designtools_en', 'RMlink', 'title_ar', 'description_ar', 'designtools_ar')


class NonTechCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonTechCircle
        fields = ('id','title_en', 'description_en', 'skills_en', 'title_ar', 'description_ar', 'skills_ar')
