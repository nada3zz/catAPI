from django.db import models
from django.utils import timezone

class AboutTeam(models.Model):
    title= models.CharField(max_length=255)
    body= models.TextField()

    def __str__(self):
        return self.title

class History(models.Model):
    
    date = models.DateField()
    achievments= models.TextField()   
    #remember to add events to history section
    class Meta:
        ordering= ('-date',)

    def __str__(self):
        return str(self.date)

class News(models.Model):

    title= models.CharField(max_length=255)
    body= models.TextField()
    image= models.ImageField(blank=True)
    publish= models.DateTimeField(default=timezone.now)
    updated= models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering= ('-publish',)

    def __str__(self):
        return self.title








