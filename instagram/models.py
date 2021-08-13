from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25, default="")
    username = models.CharField(max_length=25, default="")
    password = models.CharField(max_length=25, default="")

    def __str__(self):
        return self.name
