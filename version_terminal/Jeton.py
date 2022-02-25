from constantes import *

class Jeton:
    """docstring for Jeton."""

    def __init__(self, valeur):
        self.valeur = valeur

    def afficher(self):
        print(self.valeur,end=" ")

    def est_vide(self):
        return self.valeur == VIDE
