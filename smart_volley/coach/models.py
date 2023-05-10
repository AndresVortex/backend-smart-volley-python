from django.db import models

# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    date_birth = models.DateField()
    
    class Meta:
        ordering = ["-name"]


    def __str__(self):
        return self.name

