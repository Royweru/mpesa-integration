from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    lec = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=50, blank=False)
    tscno = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.subject} {self.tscno}"


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    names = models.CharField(max_length=250)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.IntegerField()
    code = models.IntegerField()

    def __str__(self):
        return f'{self.names} {self.age} {self.email}'
