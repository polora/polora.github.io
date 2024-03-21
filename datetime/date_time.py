# bac à sable

"""
    https://openclassrooms.com/courses/apprenez-a-programmer-en-python/le-temps

    gestion du temps dans Python 
    time
    datetime
    
"""

# import des modules time et datetime
import time, datetime


"""
### UTILISATION DU MODULE TIME

# afficher le temps écoulé depuis l'epoch
T = time.time()
print(T)

# mesurer le temps écoulé entre deux évènement du programme - sleep permet de faire une pause
start = time.time()
time.sleep(3.5)
end = time.time()

print (round((end - start),1))


# strftime : permet de formater date et heure en chaîne de caractères
print(time.strftime("%A %d %B %Y - %H:%M:%S"))
"""

### UTILISATION DU MODULE DATETIME - FACILITE L'AFFICHAGE

maintenant = datetime.date.today()
print(maintenant.day, "/", maintenant.month, "/", maintenant.year," ", )

maintenant = datetime.datetime.now()
print(maintenant.day, "/", maintenant.month, "/", maintenant.year," ", maintenant.hour, ":", maintenant.minute, ":", maintenant.second )

# définir une date et calculer un nombre d'années écoulées
debut = datetime.date(2011, 8, 25)
print(debut)
fin = datetime.date.today()
print("Années écoulées : ", fin.year - debut.year)

# même chose mais avec l'heure
debut = datetime.time(16,10,0)
print(debut)
fin = datetime.datetime.now()
print("Temps écoulé : ", fin.hour - debut.hour,":",fin.minute-debut.minute, ":",fin.second - debut.second)

