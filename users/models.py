from django.db import models

class MemberRole(models.Model):
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return self.role

class MemberInfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    photo = models.ImageField(blank=True)
    fblink = models.URLField()
    linkedin= models.URLField()
    role= models.ForeignKey(MemberRole,  on_delete=models.CASCADE,related_name='memberRole')

    def __str__(self):
        return self.firstname

