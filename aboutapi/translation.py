from modeltranslation.translator import translator, TranslationOptions
from .models import News, History, AboutTeam

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(News, NewsTranslationOptions)

class HistoryTranslationOptions(TranslationOptions):
    fields = ('achievments',)

translator.register(History, HistoryTranslationOptions)

class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(AboutTeam, AboutTranslationOptions)

