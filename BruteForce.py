# Importation de itertools, une bibliothèque de fonctions permettant des boucles optimisés
from itertools import chain, product
# imporation de time, des fonctions permettant de calculer le temps avec l'horloge interne
import time
# importation de sys, des fonctions permettant d'utiliser les entrées du système
import sys

# entrées de l'utilisateur
fonction = sys.argv[1]
mot_de_passe = sys.argv[2]

longueur_motDePasse = len(mot_de_passe)


# Logique du BruteForce
def BruteForce(liste_de_symbole, longueur_motDePasse):
    return (
        ''.join(symbole)  # fusionne les symboles
        for symbole in chain.from_iterable(product(liste_de_symbole, repeat=i)  # pour tout les symboles dans la chaine des produits de la liste de symboles exposé par la grosseur du mot de passe
        for i in range(1, longueur_motDePasse + 1))  # permet de répéter le nombre exact de la longueur du mot de passe
        )


# Fonction du bruteforce faible
def BruteForceFaible():
    liste_de_symbole = "abcdefghijklmnopqrstuvwxyz"
    depart = time.time()
    for essai in BruteForce(liste_de_symbole, longueur_motDePasse):
        if essai == mot_de_passe:
            fin = time.time()
            print("Mot de passe cisco trouvé en ", (fin - depart), "secondes")
            break


# Fonction du bruteforce moyen
def BruteForceMoyen():
    liste_de_symbole = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    depart = time.time()
    for essai in BruteForce(liste_de_symbole, longueur_motDePasse):
        if essai == mot_de_passe:
            fin = time.time()
            print("Mot de passe cisco trouvé en ", (fin - depart), "secondes")
            break


#Fonction du bruteforce fort
def BruteForceFort():
    liste_de_symbole = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    depart = time.time()
    for essai in BruteForce(liste_de_symbole, longueur_motDePasse):
        if essai == mot_de_passe:
            fin = time.time()
            print("Mot de passe cisco trouvé en ", round((fin - depart), 2), "secondes")
            break

if fonction == "faible":
    BruteForceFaible()
elif fonction == "moyen":
    BruteForceMoyen()
elif fonction == "fort":
    BruteForceFort()
