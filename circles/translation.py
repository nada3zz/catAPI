from modeltranslation.translator import translator, TranslationOptions
from .models import TechCircle, NonTechCircle


class TechCircleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'designtools')

translator.register(TechCircle, TechCircleTranslationOptions)

class NonTechCircleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'skills')

translator.register(NonTechCircle, NonTechCircleTranslationOptions)
