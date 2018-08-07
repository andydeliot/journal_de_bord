from django.db import models

import arrow

# Create your models here.


class Lieu(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Lieux"

    def __str__(self):
        return self.nom


class Journee(models.Model):
    jour = models.DateField(unique=True)
    lever = models.TimeField(null=True,
                             blank=True)
    dure = models.DurationField(null=True,
                            blank=True)
    lieu = models.ForeignKey(Lieu,
                             null=True,
                             blank=True,
                             on_delete=models.SET_NULL)

    def souvenirs(self):
        return Souvenir.objects.filter(journee=self)
        
    def __str__(self):
        return arrow.get(self.jour).format("dddd DD MMMM YYYY", locale="fr_FR")


class Souvenir(models.Model):
    journee = models.ForeignKey(Journee,
                                on_delete=models.CASCADE)
    texte = models.CharField(max_length=10000)

    def __str__(self):
        return self.texte

