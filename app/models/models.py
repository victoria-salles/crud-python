from django.db import models

class Person(models.Model):
    Name = models.CharField(max_length=80)
    Email = models.EmailField(max_length=80)