from django.db import models


class student(models.Model):
    name = models.CharField(max_length=150,blank=False , null=False)
    email = models.EmailField()
    age= models.IntegerField()
    gender= models.CharField(max_length=20 ,blank=False , null=False)
    semester= models.IntegerField(max_length=2 , default=0)
    project = models.CharField(max_length=500 , default=0)
  
    def __str__(self):
        return self.name

