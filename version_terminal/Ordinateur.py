import random

from constantes import *
from Participant import Participant

class Ordinateur(Participant):
    """Represente l'Ordinateur."""

    def __init__(self, nom,couleur_jeton,type_jeu):
        """Initialise le nom, la couleur du jeton et le type de jeu de l'ordinateur"""
        super(Ordinateur, self).__init__(nom,couleur_jeton)
        self.type_jeu = type_jeu

    def jouer(self):
        """Donne la colonne choisie par l'ordinateur selon le type de jeu de l'ordinateur
        Return:
        - un entier : le numero de colonne
        """
        if self.type_jeu == JEU_INTELLIGENT :
            return self.choix_intelligent()
        elif self.type_jeu == JEU_IA :
            return self.choix_ia()
        return self.choix_aleatoire()

    def choix_aleatoire(self):
        """Choisi aléatoirement un numero de colonne entre 0 et NB_COLONNES
        Return:
        - int
        """
        v = int(random.random() * NB_COLONNES)
        return v

    def choix_intelligent(self):
        """Choisi plus ou moins intelligement un numero de colonne entre 0 et NB_COLONNES
        Return:
        - int
        """
        return self.choix_aleatoire()

    def choix_ia(self):
        """Choisi grace à une IA un numero de colonne entre 0 et NB_COLONNES
        Return:
        - int
        """
        return self.choix_aleatoire()
