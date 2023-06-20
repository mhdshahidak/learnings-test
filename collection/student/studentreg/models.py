from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.URLField(null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=150,null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

