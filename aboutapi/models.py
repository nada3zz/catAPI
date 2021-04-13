from django.db import models

class TopMembers(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    photo= models.ImageField()
    contactinfo=models.TextField()

class Events(models.Model):
    title= models.CharField(max_length=150)
    description= models.TextField()
    image= models.ImageField()


class AboutTeam(models.Model):
    title= models.CharField(max_length=100)
    body= models.TextField()
    logoUrl= models.ImageField()
    topmembers= models.ForeignKey(TopMembers, on_delete=models.CASCADE,related_name='topmembers')
    events= models.ForeignKey(Events, on_delete=models.CASCADE,related_name='events')

    def __str__(self):
        return self.title

class HeadsInfo(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    phoneNo=models.CharField(max_length=12)



class Circles(models.Model):
    Type= models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    description= models.TextField()
    RMlink= models.URLField()
    headinfo= models.ForeignKey(HeadsInfo, on_delete=models.CASCADE,related_name='headsinfo')

    def __str__(self):
        return self.title











