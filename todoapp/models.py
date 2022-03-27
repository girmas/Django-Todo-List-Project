from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    
    
    
    def __str__(self):
        return self.title
