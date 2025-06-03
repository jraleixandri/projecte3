from django.db import models

class Escuderia(models.Model):
    nom = models.CharField(max_length=100)
    any_creacio = models.PositiveIntegerField(help_text="Any de creació de l'escuderia")
    seu = models.CharField(max_length=100, help_text="Seu principal de l'escuderia")
    campionats_pilots = models.PositiveIntegerField(default=0, help_text="Nº de campionats de pilots aconseguits")
    campionats_equips = models.PositiveIntegerField(default=0, help_text="Nº de campionats de constructors aconseguits")

    def __str__(self):
        return self.nom

class Pilot(models.Model):
    nom = models.CharField(max_length=100)
    edat = models.PositiveIntegerField()
    nacionalitat = models.CharField(max_length=50)
    escuderia = models.ForeignKey(Escuderia, on_delete=models.CASCADE, related_name='pilots')

    def __str__(self):
        return f"{self.nom} ({self.nacionalitat})"

class Cursa(models.Model):
    nom = models.CharField(max_length=100)
    data = models.DateField()
    pais = models.CharField(max_length=50, help_text="País on es disputa la cursa")
    voltes = models.PositiveIntegerField(help_text="Nº de voltes de la cursa")
    longitud_circuit_km = models.DecimalField(max_digits=5, decimal_places=2, help_text="Longitud del circuit en km")
    pole_position = models.ForeignKey(Pilot, on_delete=models.SET_NULL, null=True, related_name='poles')

    def __str__(self):
        return f"{self.nom} - {self.data}"

class ResultatCursa(models.Model):
    cursa = models.ForeignKey(Cursa, on_delete=models.CASCADE, related_name='resultats')
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    posicio_final = models.PositiveIntegerField()
    temps_diferencia = models.DurationField(help_text="Temps respecte al guanyador (HH:MM:SS)")

    class Meta:
        unique_together = ('cursa', 'pilot')
        ordering = ['cursa', 'posicio_final']

    def __str__(self):
        return f"{self.cursa.nom} - {self.pilot.nom}: P{self.posicio_final}"
