from django.db import models

class Day(models.Model):
    date = models.OneToOneField("Date", on_delete=models.CASCADE, related_name="day")
    temp = models.OneToOneField("Temp", on_delete=models.CASCADE, related_name="day")

class Date(models.Model):
    Name = models.CharField(max_length=20)
    D = models.IntegerField()
    M = models.IntegerField()
    Y = models.IntegerField()

class Temp(models.Model):
    Morn = models.IntegerField()
    Noon = models.IntegerField()
    Night = models.IntegerField()