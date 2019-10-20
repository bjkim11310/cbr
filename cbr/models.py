from django.db import models

class Resource (models.Model):
    testName = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.testName

class Exam (models.Model):
    testType = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

