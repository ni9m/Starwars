from films import *
from acteur import *
from personnage import *

film = Films("Un nouvel espoir", 1977, 4, 500000, 1500000)

print("Titre du film :", film.get__titre(), "/Annee du film :", film.get__annee(), "/Numero du film :",
      film.get__numero(), "/Cout du film :", film.get__cout(), "/Recette du film :", film.get__recette())

# on utilise la class films
film2 = Films()

# on saisie les infos concernant ce film
saisieTitre = input("Saisir titre du film : ")
saisieAnnee = input("Saisir année du film : ")
saisieNumero = input("Saisir numéro du film : ")
saisieCout = input("Saisir coût du film : ")
saisieRecette = input("Saisir recette du film : ")

# on attribu les infos précédemment saisies au film
film2.set__titre(saisieTitre)
film2.set__annee(saisieAnnee)
film2.set__numero(saisieNumero)
film2.set__cout(saisieCout)
film2.set__recette(saisieRecette)

pers1 = Personnages("Bang", "Olufsen")
pers2 = Personnages("Logitech", "Samsung")
pers3 = Personnages("Bourdy", "Tom")

# test
# print(pers3.prenom, pers3.nom)

# on utilise la class acteurs
acteur1 = Acteurs()
# on saisi le nom et prenom de l'acteur1
acteur1.nom = input("saisir le Nom de l'acteur")
acteur1.prenom = input("saisir le prenom de l'acteur")

# puis le nombre de personnages qu'il incarne
print("Saisir nombre de personnages pour l'acteur")
nbperso = int(input())
acteur1.nbperso = nbperso

# saisie du nom des perso
print("Saisir nom des", nbperso, " personnages")

# on créé une liste poru les personnages
listepers = []

# on met les personnages précédemment saisi dans cette liste
for i in range(0, nbperso):
    element = str(input())
    listepers.append(element)
acteur1.duet = listepers
for i in range(0, nbperso):
    print(acteur1.duet[i])

anneesaisie = input("Saisir une année au hasard :")

filmdico1 = Films(titre="Titre1", annee=1970, cout=50000, recette=100000)
# filmdico1.dico()

print("L'acteur", acteur1.nom, acteur1.prenom, "joue", acteur1.nbperso, "personnages qui sont : ")
print("Le nombre d'acteurs du film", film2.titre, "est de : ", film2.nbActeurs)
print("Le nombre de personnages du film", film2.titre, "est de : ", film2.nbPerso)
print("Le nombre de personnages du film", film2.titre, "est de : ", film2.nbPerso)
print(film2.calcul(int(saisieCout), int(saisieRecette)), "€")
print("Annee :", film2.isbefore(anneesaisie))
print(film2.tri())
print(filmdico1.dico("Titre1", 1970, filmdico1.calcul(int(saisieCout), int(saisieRecette))))