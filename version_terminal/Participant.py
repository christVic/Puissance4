from Jeton import Jeton
from constantes import *

class Participant:
    """Participant."""
    score = 0

    def __init__(self, nom, couleur_jeton):
        """Initialise le nom, la couleur de jeton du participant"""
        self.nom = str(nom)
        self.couleur_jeton = couleur_jeton
        self.jeton = Jeton(couleur_jeton)

    def get_nom_couleur(self):
        """Retourne le nom (string) correspondant à la couleur du jeton"""
        if self.couleur_jeton == ROUGE:
            return COULEUR_ROUGE
        else:
            return COULEUR_JAUNE
    def incrementer_score(self):
        """Augmente le score du joueur de 1"""
        self.score += 1

    def victoire(self):
        """Affiche les messages qui annonce une victoire et met à jour le score"""
        print(MESSAGE_VICTOIRE)
        print(self.nom,ANNONCE_VAINQUEUR)
        self.incrementer_score()
