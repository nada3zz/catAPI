
from django.contrib import admin
from .models import EventSession,Event,TeamBoard,TechCircle,NonTechCircle,News,History,HeadInfo,TopMember,AboutTeam
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    pass

admin.site.register(News, NewsAdmin)

class EventAdmin(TranslationAdmin):
    pass

admin.site.register(Event, EventAdmin)

class SessionAdmin(TranslationAdmin):
    pass

admin.site.register(EventSession, SessionAdmin)

class BoardAdmin(TranslationAdmin):
    pass

admin.site.register(TeamBoard, BoardAdmin)

class TechCircleAdmin(TranslationAdmin):
    pass

admin.site.register(TechCircle, TechCircleAdmin)

class NonTechAdmin(TranslationAdmin):
    pass

admin.site.register(NonTechCircle, NonTechAdmin)

class HistoryAdmin(TranslationAdmin):
    pass

admin.site.register(History, HistoryAdmin)

class HeadAdmin(TranslationAdmin):
    pass

admin.site.register(HeadInfo, HeadAdmin)

class TopMemAdmin(TranslationAdmin):
    pass

admin.site.register(TopMember, TopMemAdmin)

class AboutAdmin(TranslationAdmin):
    pass

admin.site.register(AboutTeam, AboutAdmin)


