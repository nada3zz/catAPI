from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Event,EventSession, EventPhoto

# Register your models here.
class EventAdmin(TranslationAdmin):
    pass

admin.site.register(Event, EventAdmin)

class SessionAdmin(TranslationAdmin):
    pass

admin.site.register(EventSession, SessionAdmin)


admin.site.register(EventPhoto)