from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Человек'
        verbose_name_plural = 'Люди'

class Order(models.Model):
    datetime = models.DateTimeField()

    def __str__(self):
        return str(self.datetime)