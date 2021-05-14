from modeltranslation.translator import translator, TranslationOptions
from .models import EventSession, Event


class EventTranslationOptions(TranslationOptions):
    fields = ('title', )

translator.register(Event, EventTranslationOptions)


class SessionTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'event_name')

translator.register(EventSession, SessionTranslationOptions)


