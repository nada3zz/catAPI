from django.contrib import admin
from .models import AboutTeam, Circles, TopMembers,HeadsInfo,Events
from parler.admin import TranslatableAdmin


class AboutteamAdmin(TranslatableAdmin):
    list_display = ['title', 'body']

admin.site.register(AboutTeam)

class CirclesAdmin(TranslatableAdmin):
    list_display = ['Type', 'title','description']

admin.site.register(Circles)

class TopmembersAdmin(TranslatableAdmin):
    list_display = ['firstname', 'lastname']

admin.site.register(TopMembers)
class HeadinfoAdmin(TranslatableAdmin):
    list_display = ['firstname', 'lastname']

admin.site.register(HeadsInfo)

class EventsAdmin(TranslatableAdmin):
    list_display = ['title', 'description']

admin.site.register(Events)