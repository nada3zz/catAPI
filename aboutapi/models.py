from django.db import models
from django.utils import timezone

class AboutTeam(models.Model):
    title= models.CharField(max_length=255)
    body= models.TextField()

class EventSession(models.Model):

    title= models.CharField(max_length=255)
    description= models.TextField()
    sessionlink= models.URLField(blank=True)
    image= models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    
    title= models.CharField(max_length=255)
    image= models.ImageField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    #sessions= models.ManyToManyField(EventSessions)
    
    def __str__(self):
        return self.title


class TeamBoard(models.Model):

    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    photo= models.ImageField(blank=True)
    FBlink= models.URLField(blank=True)
    linkedIn= models.URLField(blank=True)

    def __str__(self):
        return self.firstname


class History(models.Model):
    
    date = models.DateTimeField(auto_now=True)
    board= models.ForeignKey(TeamBoard, on_delete=models.CASCADE,related_name='teamboard')
    achievments= models.TextField()   
    
    def __str__(self):
        return self.date

class News(models.Model):

    title= models.CharField(max_length=255)
    body= models.TextField()
    image= models.ImageField(blank=True)
    publish= models.DateTimeField(default=timezone.now)

    class Meta:
        ordering= ('-publish',)

    def __str__(self):
        return self.title

class HeadInfo(models.Model):

    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    FBlink= models.URLField(blank=True)
    linkedIn= models.URLField(blank=True)   
   
    def __str__(self):
        return self.firstname

#change forgin key into head sh

class TechCircle(models.Model):
 
    title= models.CharField(max_length=100)
    description= models.TextField()
    RMlink= models.URLField()
    designTools= models.TextField()
    headinfo= models.ForeignKey(HeadInfo, on_delete=models.CASCADE,related_name='techHeads')
    
    def __str__(self):
        return self.title

class NonTechCircle(models.Model):

    title= models.CharField(max_length=100)
    description= models.TextField()
    skills= models.TextField()
    headinfo= models.ForeignKey(HeadInfo, on_delete=models.CASCADE,related_name='nontechHeads')

    def __str__(self):
        return self.title

class TopMember(models.Model):

    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    photo= models.ImageField(blank=True),
    FBlink= models.URLField(blank=True)
    linkedIn= models.URLField(blank=True)

    def __str__(self):
        return self.firstname






