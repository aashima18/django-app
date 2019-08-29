from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    objects = models.Manager()
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    url=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    summary=models.TextField()
    parentid=models.ForeignKey('self', blank=True, null=True,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
