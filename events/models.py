from django.db import models
from django.utils.timezone import now

class Event(models.Model):
    title= models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True,)
       
    def __str__(self):
        return self.title


class EventSession(models.Model):

    title= models.CharField(max_length=255)
    description= models.TextField()
    sessionlink= models.URLField(blank=True)
    date = models.DateTimeField(default=now)
    event=models.ForeignKey(Event, on_delete=models.CASCADE,related_name='event')

    def __str__(self):
        return self.title

class EventPhoto(models.Model):

    image= models.ImageField(blank=True)
    session_name= models.ForeignKey(EventSession, on_delete=models.CASCADE,related_name='eventsessionphotos')
    created= models.DateTimeField(auto_now_add=True,)
    updated= models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title




#relation between sessions and event