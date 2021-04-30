
from modeltranslation.translator import translator, TranslationOptions
from .models import EventSession,Event,TeamBoard,TechCircle,NonTechCircle,News,History,HeadInfo,TopMember,AboutTeam

class SessionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(EventSession, SessionTranslationOptions)

class EventTranslationOptions(TranslationOptions):
    fields = ('title', )

translator.register(Event, EventTranslationOptions)

class BoardTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname')

translator.register(TeamBoard, BoardTranslationOptions)

class TechCircleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'designTools')

translator.register(TechCircle, TechCircleTranslationOptions)

class NonTechCircleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'skills')

translator.register(NonTechCircle, NonTechCircleTranslationOptions)

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(News, NewsTranslationOptions)

class HistoryTranslationOptions(TranslationOptions):
    fields = ('achievments', 'board')

translator.register(History, HistoryTranslationOptions)

class HeadInfoTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname')

translator.register(HeadInfo, HeadInfoTranslationOptions)

class TopMemTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname')

translator.register(TopMember, TopMemTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(AboutTeam, AboutTranslationOptions)
