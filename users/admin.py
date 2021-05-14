from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import MemberRole, MemberInfo
# Register your models here.
class MemberInfoAdmin(TranslationAdmin):
    pass

admin.site.register(MemberInfo, MemberInfoAdmin)
 

class UserRoleAdmin(TranslationAdmin):
    pass

admin.site.register(MemberRole)