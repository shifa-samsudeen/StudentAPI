from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name