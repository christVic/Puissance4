from constantes import *

import pygame
from pygame.locals import *

class Jeton:
    """docstring for Jeton."""

    def __init__(self, valeur):
        self.valeur = valeur
        self.couleur = COULEUR_BLANCHE
        if self.valeur == ROUGE:
            self.couleur = COULEUR_ROUGE
        elif self.valeur == JAUNE:
            self.couleur = COULEUR_JAUNE


    def afficher(self):
        print(self.valeur,end=" ")

    def est_vide(self):
        return self.valeur == VIDE

    def dessiner(self, surface,position,dimension):
        """dessine un jeton
        Args:
        - surface : surface sur laquelle on dessine le jeton
        - position (int,int) : coordonnées x et y du centre du jeton sur la surface
        - rayon (int) : le rayon du jeton
        """
        # on calcule la position du coin superieur gauche
        posX = position[0]-(dimension[0]/2)
        posY = position[1]-(dimension[1]/2)
        rect = (posX,posY,dimension[0],dimension[1])
        pygame.draw.ellipse(surface,pygame.Color(self.couleur),rect)

        #pygame.draw.circle(surface,pygame.Color(self.couleur),position,dimension[0]/2)
