from events.models import Event, EventSession, SessionPhoto
import factory

class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title_en = factory.Faker("text", max_nb_chars=30)
    title_ar = factory.Faker(provider="text",locale = "ar_AA", max_nb_chars=30)

class EventSessionFactory(EventFactory):
    class Meta:
        model = EventSession
    
    description_en = factory.Faker(provider="paragraph")
    description_ar = factory.Faker(provider="paragraph", locale = "ar_AA")
    sessionlink = factory.Faker(provider="uri")
    event = factory.SubFactory(EventFactory)

class SessionPhotoFactory(factory.django.DjangoModelFactory):
    class Meta :
        model = SessionPhoto
    image = factory.django.ImageField()