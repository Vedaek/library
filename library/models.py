from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    phone = models.IntegerField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
