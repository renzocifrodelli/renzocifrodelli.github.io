from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=40, unique=True)
    email = models.EmailField()
    message = models.TextField(null= True, blank= True)
    
class News(models.Model):
    tittle = models.CharField(max_length=40,)
    subtittle = models.CharField(max_length=40,)
    notice = models.CharField(max_length=4000)