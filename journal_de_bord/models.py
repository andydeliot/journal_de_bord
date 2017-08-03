from django.db import models

import arrow

# Create your models here.

def aujourdhui():
    return arrow.utcnow().to("UTC+2")

class Journee(models.Model):
    jour = models.DateField(unique=True)

    def __str__(self):
        return arrow.get(self.jour).format("dddd DD MMMM YYYY", locale="fr_FR")


class Souvenir(models.Model):
    journee = models.ForeignKey(Journee,
                                on_delete=models.CASCADE)
    texte = models.CharField(max_length=10000)

    def __str__(self):
        return self.texte

