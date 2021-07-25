from modeltranslation.translator import translator, TranslationOptions
from .models import News, History, AboutTeam, Home

class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(Home, HomeTranslationOptions)    

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(News, NewsTranslationOptions)

class HistoryTranslationOptions(TranslationOptions):
    fields = ('achievments',)

translator.register(History, HistoryTranslationOptions)

class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(AboutTeam, AboutTranslationOptions)

