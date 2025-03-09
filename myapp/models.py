from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    address=models.TextField()

    def __str__(self):
        return self.name