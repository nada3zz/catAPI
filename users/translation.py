from modeltranslation.translator import translator, TranslationOptions
from .models import MemberInfo, MemberRole


class MemeberInfoTranslationOptions(TranslationOptions):
    fields = ('firstname','lastname', 'role' )

translator.register(MemberInfo, MemeberInfoTranslationOptions)



class MemberRoleTranslationOptions(TranslationOptions):
    fields = ('role')

translator.register(MemberRole, MemberRoleTranslationOptions)