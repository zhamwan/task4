from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    numberSis = models.IntegerField('number')
    numberBro = models.IntegerField('number')
    user = models.CharField('user', max_length=50)
    time = models.DateTimeField('time', auto_now=True)
    mes = models.CharField('message', max_length=50)

    def __str__(self):
        return str(self.mes)
