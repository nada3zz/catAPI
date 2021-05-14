from django.contrib import admin
from .models import TechCircle, NonTechCircle
from modeltranslation.admin import TranslationAdmin

class TechCircleAdmin(TranslationAdmin):
    pass

admin.site.register(TechCircle, TechCircleAdmin)

class NonTechAdmin(TranslationAdmin):
    pass

admin.site.register(NonTechCircle, NonTechAdmin)