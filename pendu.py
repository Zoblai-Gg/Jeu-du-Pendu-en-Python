""" Ce fichier contient le jeu du pendu. Il s ' appuie sur les fichiers :
    - donnees.py
    - fonctions.py  """

import donnees
import fonctions


print("BIENVENUE DANS LE JEU DU PENDU SUR LE THÈME \"FRUITS\" \n\n "
      "IL CONSISTE À DEVINER UN FRUIT CARACTÈRE PAR CARACTÈRE \n\n")


# Variables

quitter = "O"

while quitter != 'N':

    bravo = False
    i = donnees.chance
    mot = fonctions.choose_random_word()
    mot_a_deviner = fonctions.create_choosing_word(mot)
    print("\nMot à deviner : {}\n".format(mot_a_deviner))

    while i > 1 and bravo is False:
        carac = fonctions.verif_carac_valide()

        mot_a_deviner = fonctions.verif_carac_in_word(carac, mot, mot_a_deviner)

        print("\nMot à deviner : {}\n".format(mot_a_deviner))
        if '*' not in mot_a_deviner:
            bravo = True

        i -= 1
        print("Il vous reste {} chance \n".format(i))

    if i > 1:
        print("Bvravo vous avez trouver le mot {}".format(mot))
        fonctions.save_score(i)
    else:
        print("PENDU ! Vous avez perdu !\n")

    quitter = input("\nVoulez vous reprendre le jeu ?:(O/N)\n")
    quitter.capitalize()
