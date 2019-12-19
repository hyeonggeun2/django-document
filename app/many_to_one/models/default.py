from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField('차량명', max_length=100)

    def __str__(self):
        return self.name