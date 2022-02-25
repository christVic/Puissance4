import random

from constantes import *
from Participant import Participant

class Joueur(Participant):
    """Represente le Joueur."""

    def __init__(self, nom,couleur_jeton):
        """Initialise le nom et la couleur du jeton du joueur"""
        super(Joueur, self).__init__(nom,couleur_jeton)

    def jouer(self):
        """Demande à l'utilisateur un numero de colonne entre 1 et NB_COLONNES(compris)
        Return:
        - int
        """
        saisie = int(input(TEXTE_INPUT_CHOIX_JOUEUR))
        while saisie<1 or saisie>NB_COLONNES:
            saisie = int(input(TEXTE_INPUT_CHOIX_JOUEUR))

        return saisie-1

    def choix_aleatoire(self):
        """Choisi aléatoirement un numero de colonne entre 0 et NB_COLONNES
        Return:
        - int
        """
        return int(random.random() * NB_COLONNES)
