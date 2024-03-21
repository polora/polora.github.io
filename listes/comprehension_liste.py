
### Liste de compréhension - comprehension lists /// vu ds cours OpenClassRoom

# test tri avec une list comprehension
liste = [0,1,2,3,4,5,6,7,8,9]
print(liste)
liste = [nb * nb for nb in liste]
print(liste)

liste = [nb for nb in liste if nb % 2 == 0]
print(liste)

print("\n")

liste2 = [0,1,2,3,4,5,6,7,8,9]
liste2 = [nb-4 for nb in liste2 if nb>4] # retire 4 à chaque elt de la liste si cet element>4
print(liste2)

print("\n")

# ---- Exercice OpenClassRoom ----
inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
    ]

# tri inverse
inventaire = [(qte,fruit) for fruit,qte in inventaire]
print(inventaire)
# tri par quantité croissante
inventaire =  [(qte,fruit) for qte,fruit in sorted(inventaire)]
print(inventaire)
