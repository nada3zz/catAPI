
from modeltranslation.translator import translator, TranslationOptions
from .models import EventSessions,Events,TeamBoard,TechCircles,NonTechCircles,News,History,HeadsInfo,TopMembers

class SessionsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(EventSessions, SessionsTranslationOptions)

class EventsTranslationOptions(TranslationOptions):
    fields = ('title', )

translator.register(Events, EventsTranslationOptions)

class BoardTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname')

translator.register(TeamBoard, BoardTranslationOptions)

class TechCirclesTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'designTools')

translator.register(TechCircles, TechCirclesTranslationOptions)

class NonTechCirclesTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'skills')

translator.register(NonTechCircles, NonTechCirclesTranslationOptions)

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(News, NewsTranslationOptions)

class HistoryTranslationOptions(TranslationOptions):
    fields = ('achievments', 'board')

translator.register(History, HistoryTranslationOptions)

class HeadInfoTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname')

translator.register(HeadsInfo, HeadInfoTranslationOptions)

class TopMemTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname')

translator.register(TopMembers, TopMemTranslationOptions)


