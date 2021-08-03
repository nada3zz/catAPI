from django.db import models


class TechCircle(models.Model):
 
    title= models.CharField(max_length=30)
    description= models.TextField()
    RMlink= models.URLField()
    designtools= models.TextField()
    #headinfo= models.ForeignKey(HeadInfo, on_delete=models.CASCADE,related_name='techHeads')
    
    def __str__(self):
        return self.title

class NonTechCircle(models.Model):

    title= models.CharField(max_length=30)
    description= models.TextField()
    skills= models.TextField()
    #headinfo= models.ForeignKey(HeadInfo, on_delete=models.CASCADE,related_name='nontechHeads')

    def __str__(self):
        return self.title





