from django.db.models import fields
from rest_framework import serializers
from .models import MemberInfo




class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberInfo
        fields =('id', 'firstname_en', 'lastname_en', 'role_en', 'firstname_ar', 'lastname_ar', 'role_ar', 'fblink', 'linkedin')
