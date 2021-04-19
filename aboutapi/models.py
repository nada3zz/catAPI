from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class TopMembers(TranslatableModel):
    class Meta:
        verbose_name = "topMember"
        verbose_name_plural ="topMembers"
        
    translations = TranslatedFields(
        firstname= models.CharField(max_length=100),
        lastname= models.CharField(max_length=100),
    )
   
    photo= models.ImageField(blank=True),
    contactinfo=models.TextField(blank=True)
    #lang_code= models.CharField("lang code", max_length=2, unique=True)

    def __str__(self):
        return self.firstname

class Events(TranslatableModel):
    class Meta:
        verbose_name = "event"
        verbose_name_plural ="events"

    translations = TranslatedFields(
        title= models.CharField(max_length=150),
        description= models.TextField()
    )
    
    image= models.ImageField()
    

    def __str__(self):
        return self.title


class AboutTeam(TranslatableModel):
    class Meta:
        verbose_name ="aboutTeam"

    translations = TranslatedFields(
        title= models.CharField(max_length=100),
        body= models.TextField(),
       
    )
    
    logoUrl= models.ImageField()
    

    def __str__(self):
        return self.title


class HeadsInfo(TranslatableModel):
    class Meta:
        verbose_name = "headInfo"
        verbose_name_plural ="headsInfo"

    translations= TranslatedFields (
        firstname= models.CharField(max_length=100),
        lastname= models.CharField(max_length=100),
       
    )
    phoneNo=models.CharField(max_length=12)
    
    def __str__(self):
        return self.firstname



class Circles(TranslatableModel):
    class Meta:
        verbose_name = "circle"
        verbose_name_plural ="circles"

    translations= TranslatedFields(
        Type= models.CharField(max_length=100),
        title= models.CharField(max_length=100),
        description= models.TextField(),
    )

    RMlink= models.URLField()
    headinfo= models.ForeignKey(HeadsInfo, on_delete=models.CASCADE,related_name='headsinfo')
    
    def __str__(self):
        return self.title











