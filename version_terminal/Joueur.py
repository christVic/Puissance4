import random

from constantes import *
from Participant import Participant

class Joueur(Participant):
    """Represente le Joueur."""

    def __init__(self, nom,couleur_jeton):
        """Initialise le nom et la couleur du jeton du joueur"""
        super(Joueur, self).__init__(nom,couleur_jeton)


    def choix_colonne(self,grille):
        """Demande à l'utilisateur un numero de colonne entre 1 et NB_COLONNES(compris)
        Return:
        - colonne (int)
        """
        colonne = int(input(TEXTE_INPUT_CHOIX_JOUEUR))
        while colonne<1 or colonne>NB_COLONNES:
            colonne = int(input(TEXTE_INPUT_CHOIX_JOUEUR))

        return colonne-1
