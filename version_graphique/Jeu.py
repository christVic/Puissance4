import random
import pygame
from pygame.locals import *

from constantes import *
from Grille import Grille
from Participant import Participant

class Jeu:
    """Represente le Jeu."""
    def __init__(self,participant1,participant2):

        """Initialise la grille et les participants du jeu"""
        self.grille = Grille()

        self.participant1 = participant1
        self.participant2 = participant2

        #self.fenetre_jeu = pygame.display.set_mode((500,500),pygame.RESIZABLE)

        #pygame.init()

        #pygame.quit()


    def action_realisee(self,participant,colonne_choisie):
        """ Décrit une action realisée par un participant
        Args:
        - participant (Participant) : le nom du participant qui choisi la colonne
        - colonne_choisie (int) : le numero de la colonne choisie
        Return:
        - string
        """
        return ""+participant.nom+" a choisi la colonne "+str(colonne_choisie+1)

    def afficher_score(self):
        """Affiche le score du jeu"""
        print(self.participant1.nom,"(",self.participant1.get_nom_couleur(),"):",self.participant1.score,"-",self.participant2.score,":(",self.participant2.get_nom_couleur(),")",self.participant2.nom)

    def fin_partie(self):
        """Determine si la partie est finie
        Return:
        - Boolean
        """
        return self.grille.est_plein()

    def victoire_partie(self,ligne,colonne):
        """Determine si la partie est gagnée
        Args:
        -ligne (int) : numero de ligne du dernier jeton posé
        -colonne (int) : numero de colonne du dernier pion posé
        Return:
        - Boolean
        """
        if self.grille.compter_jetons(ligne,colonne) >= NB_JETONS_VICTOIRE :
            return True
        return False;

    def lancer_partie(self):
        """Lance une partie du jeu"""
        # on initialise la fenetre de jeu
        pygame.init()
        fenetre_partie = pygame.display.set_mode((500,500),pygame.RESIZABLE)
        pygame.display.set_caption(NOM_JEU)
        fenetre_partie.fill(COULEUR_BLANCHE)
        # on calcule les dimensions de la grille
        largeur_fenetre,hauteur_fenetre = fenetre_partie.get_size()
        centre_fenetre_x,centre_fenetre_y = largeur_fenetre*0.5,hauteur_fenetre*0.5

        largeur_grille = centre_fenetre_x*1.5
        hauteur_grille = centre_fenetre_y*1.5

        positionX = abs(centre_fenetre_x-largeur_grille*0.5)
        positionY = abs(centre_fenetre_y-hauteur_grille*0.5)

        # on affiche la grille
        self.grille.afficher_grille()
        self.grille.dessiner(fenetre_partie,(positionX,positionY),largeur_grille,hauteur_grille)

        # on initialise le compteur
        compteur = int(random.random() * NB_COLONNES)
        pygame.display.update()

        while not self.fin_partie():
            for event in pygame.event.get():
                if event.type == QUIT:
                    break

            # on rafraichit la fenetre
            fenetre_partie.fill(COULEUR_BLANCHE)
            largeur_fenetre,hauteur_fenetre = fenetre_partie.get_size()
            centre_fenetre_x,centre_fenetre_y = largeur_fenetre*0.5,hauteur_fenetre*0.5

            positionX = abs(centre_fenetre_x-largeur_grille*0.5)
            positionY = abs(centre_fenetre_y-hauteur_grille*0.5)

            ligne_jeton = -1
            colonne_jeton = -1

            if compteur % 2 == 0:
                # Tour participant1
                print("**c'est au tour de ",self.participant1.nom,"**")
                ligne_jeton,colonne_jeton = self.participant1.joue(self.grille)
                print(self.action_realisee(self.participant1,colonne_jeton))

            else:
                # Tour participant2
                print("**c'est au tour de ",self.participant2.nom,"**")
                ligne_jeton,colonne_jeton = self.participant2.joue(self.grille)
                print(self.action_realisee(self.participant2,colonne_jeton))

            # on affiche la grille
            self.grille.afficher_grille()
            self.grille.dessiner(fenetre_partie,(positionX,positionY),largeur_grille,hauteur_grille)
            # si il y a assez de jetons alignés
            if self.victoire_partie(ligne_jeton,colonne_jeton):
                if compteur % 2 == 0:
                    # participant1
                    self.participant1.victoire()
                else:
                    # participant2
                    self.participant2.victoire()
                # on affiche la position du jeton de la victoire
                print("ligne=",ligne_jeton+1,"colonne=",colonne_jeton+1)
                # fin de la partie / on quitte la boucle
                break

            # on incremente le compteur
            compteur += 1
            pygame.display.update()

        pygame.quit()
        if self.fin_partie():
            print(MESSAGE_GRILLE_PLEINE)
        self.afficher_score()

    def jeu(self):
        """Demarre/Lance le jeu"""
        print(self.participant1.nom,"(",self.participant1.get_nom_couleur(),") VS (",self.participant2.get_nom_couleur(),")",self.participant2.nom)
        compteur = 1

        while 1:
            print("Partie",compteur)
            self.lancer_partie()
            nouvelle_partie = int(input(TEXTE_INPUT_NOUVELLE_PARTIE))
            if nouvelle_partie == 1:
                compteur += 1
                self.grille.nettoyer_grille()
                print(self.participant1.nom,"(",self.participant1.get_nom_couleur(),") VS (",self.participant2.get_nom_couleur(),")",self.participant2.nom)

            else:
                break

        print(MESSAGE_QUITTER_JEU,self.participant1.nom)
        print(MESSAGE_QUITTER_JEU,self.participant2.nom)
