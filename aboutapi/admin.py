
from django.contrib import admin
from .models import EventSessions,Events,TeamBoard,TechCircles,NonTechCircles,News,History,HeadsInfo,TopMembers
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    pass

admin.site.register(News, NewsAdmin)

class EventAdmin(TranslationAdmin):
    pass

admin.site.register(Events, EventAdmin)

class SessionsAdmin(TranslationAdmin):
    pass

admin.site.register(EventSessions, SessionsAdmin)

class BoardAdmin(TranslationAdmin):
    pass

admin.site.register(TeamBoard, BoardAdmin)

class TechCirclesAdmin(TranslationAdmin):
    pass

admin.site.register(TechCircles, TechCirclesAdmin)

class NonTechAdmin(TranslationAdmin):
    pass

admin.site.register(NonTechCircles, NonTechAdmin)

class HistoryAdmin(TranslationAdmin):
    pass

admin.site.register(History, HistoryAdmin)

class HeadsAdmin(TranslationAdmin):
    pass

admin.site.register(HeadsInfo, HeadsAdmin)

class TopMemAdmin(TranslationAdmin):
    pass

admin.site.register(TopMembers, TopMemAdmin)




