import factory
from about.models import News

class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News
    
    title_en = factory.Faker("text", max_nb_chars=50)
    title_ar = factory.Faker(provider="text",locale = "ar_AA", max_nb_chars=50)
    body_en = factory.Faker(provider="paragraph")
    body_ar = factory.Faker(provider="paragraph", locale = "ar_AA")
    image = factory.django.ImageField()