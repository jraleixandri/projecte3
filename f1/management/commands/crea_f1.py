from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from random import randint
 
from f1.models import *
 
faker = Faker(["es_CA","es_ES"])
 
class Command(BaseCommand):
    help = 'Creo un campionat amb escuderies, pilots i curses'
 
#    def add_arguments(self, parser):
#        parser.add_argument('titol_lliga', nargs=1, type=str)
 
    def handle(self, *args, **options):
#        titol_lliga = options['titol_lliga'][0]
#        lliga = Lliga.objects.filter(nom=titol_lliga)
#        if lliga.count()>0:
#            print("Aquesta lliga ja està creada. Posa un altre nom.")
#        return
# 
#        print("Creem la nova lliga: {}".format(titol_lliga))
#        lliga = Lliga( nom=titol_lliga, temporada="temporada" )
#        lliga.save()
 
        print("Creem escuderies")
        prefixos = ["","McLaren", "Sauber", "RedBull", "Williams", "Haas"]
        motors = ["Mercedes", "Honda", "Renault", "BMW","Ferrari"]
        for i in range(10):
            ciutat = faker.city()
            prefix = prefixos[randint(0,len(prefixos)-1)]
            motor = motors[randint(0,len(motors)-1)]
            if prefix:
                nom =  prefix + "-" + motor
            else:
                nom =  motor + "-Team"
            creacio=randint(1950,2025)
            campio_p=randint(0,15)
            campio_e=randint(0,15)
            escuderia = Escuderia(nom=nom,seu=ciutat,any_creacio=creacio,
campionats_pilots=campio_p,campionats_equips=campio_e)
            #print(equip)
            escuderia.save()
 
            print("Creem pilots de l'equip "+nom)
            for j in range(2):
                nom = faker.name()
                edat = randint(18,40)
                nacionalitat = faker.country()
                pilot = Pilot(nom=nom,edat=edat,nacionalitat=nacionalitat,escuderia=escuderia)
                #print(jugador)
                pilot.save()
 
        print("Creem curses")
        for i in range(20):
                nom = faker.city()
                data = "2025-06-01"
                pais = faker.country()
                voltes= randint(30,70)
                longitud=randint(3,5)
                num=0;
                for pilot in Pilot.objects.all():
                    if i==num:
                        pole=pilot
                    num+=1
                cursa = Cursa(nom=nom,data=data,pais=pais,voltes=voltes,longitud_circuit_km=longitud,pole_position=pole)
                #print(cursa)
                cursa.save()

#        print("Creem resultat curses")
#        for resultat in f1.curses.all():
#            for pilot in f1.pilots.all():
#                    resultat.pilot = pilot
#            resultat.save()
