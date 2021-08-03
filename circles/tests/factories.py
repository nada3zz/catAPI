import factory
from circles.models import TechCircle, NonTechCircle

class TechCircleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TechCircle
    
    title_en = factory.Faker("text", max_nb_chars=30)
    title_ar = factory.Faker(provider="text",locale = "ar_AA", max_nb_chars=30)
    description_en = factory.Faker(provider="paragraph")
    description_ar = factory.Faker(provider="paragraph", locale = "ar_AA")
    RMlink = factory.Faker(provider="uri")
    designtools = factory.Faker(provider="paragraph")

class NonTechCircleFactory(TechCircleFactory):
    class Meta:
        model = NonTechCircle
    RMlink = None
    designtools = None
    skills = factory.Faker(provider="paragraph")
