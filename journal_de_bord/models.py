from django.db import models

import arrow

# Create your models here.

class Journee(models.Model):
    jour = models.DateField(unique=True)


class Souvenir(models.Model):
    journee = models.ForeignKey(Journee,
                                on_delete=models.CASCADE)
    texte = models.CharField(max_length=150)



