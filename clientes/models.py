from django.db import models

# Create your models here.
class Person(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photo', null=True, blank=True)

    def __str__(self):
        return self.frist_name


class Docs(models.Model):
    type_name = models.CharField(max_length=100)
    note = models.TextField()

    def __str__(self):
        return self.type_name

