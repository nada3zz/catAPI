#from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .models import AboutTeam, Circles, HeadsInfo, TopMembers, Events

class AboutTeamSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=AboutTeam)
    class Meta:
        model= AboutTeam
        fields= '__all__'

class CirclesSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=Circles)
    class Meta:
        model= Circles
        fields= '__all__'

class HeadInfoSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=HeadsInfo)
    class Meta:
        model= HeadsInfo
        fields= '__all__'

class TopMembersSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=TopMembers)
    class Meta:
        model= TopMembers
        fields= '__all__'

class EventSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Events)
    class Meta:
        model= Events
        fields= '__all__'