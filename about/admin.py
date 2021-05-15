from django.contrib import admin
from .models import News, History, AboutTeam
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    pass

admin.site.register(News, NewsAdmin)

class HistoryAdmin(TranslationAdmin):
    pass

admin.site.register(History, HistoryAdmin)

class AboutAdmin(TranslationAdmin):
    pass

admin.site.register(AboutTeam, AboutAdmin)


