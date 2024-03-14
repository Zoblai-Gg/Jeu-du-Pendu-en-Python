""" Ce fichier définit des fonctions utiles pour le programme pendu.

    On utilise les données du programme contenues dans donnees.py """


import donnees
import random
import pickle


def choose_random_word():
    """"Cette fonction permet de choisir àléatoirement un mot dans une liste.
        Elle renvoie cette dernière"""
    val_aleat = random.randrange(8)
    while len(donnees.liste_de_mots[val_aleat]) > donnees.taille_max_mot:
        val_aleat = random.randrange(8)

    return donnees.liste_de_mots[val_aleat]


def create_choosing_word(mot):
    """"Cette fonction  crée une chaine de caractère  de la même taille que le mot récupéré
        en paramettre et la remplie par '*'. Elle renvoie cette dernière """
    i = 0
    mot_a_deviner = list()
    while i < len(mot):
        mot_a_deviner.append('*')
        i += 1
    return "".join(mot_a_deviner)


def verif_carac_valide():
    """"Cette fonction  vérifie si un l'utilisateur a bien saisi un seul caractère si non il lui
        est démandé de resaisir. Elle renvoie ce caractère"""
    carac = "depart"

    while len(carac) != 1:
        carac = input("Veuillez saisir un caractère :")

    return carac


def verif_carac_in_word(carac, mot, mot_devine):
    """"cette fonction vérifie si un carctère se trouve dans une chaine de caratère.
        Elle renvoie une nouvelle chaine de caractère pourvu du caractère """
    mot_devine = list(mot_devine)

    if carac in mot:
        for i, elmt in enumerate(mot_devine):
            if mot[i] == carac:
                mot_devine[i] = carac
    return "".join(mot_devine)


def save_score(score):
    """"Cette foonction permet de sauvegarger dans un fichier un score contenu dans un dictionnaire.
        Si le speudo existe déjà, son score sera modifié. Sinon ils seront crée"""
    saving_board = dict()
    nom = input("Veuillez saisir votre pseudo :")

    with open("score", 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        saving_board = mon_depickler.load()
        fichier.close()

    saving_board[nom] = score

    with open("score", 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(saving_board)
        fichier.close()
