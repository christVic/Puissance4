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
            return NOM_COULEUR_ROUGE
        else:
            return NOM_COULEUR_JAUNE

    def incrementer_score(self):
        """Augmente le score du joueur de 1"""
        self.score += 1

    def choix_colonne(self,grille):
        """Retourne un numero de colonne entre 0 et NB_COLONNES(exclus)
        Arg:
        - grille (Grille) : la grille de Jeu
        Returns:
        - colonne (int) : numero de colonne choisie
        """
        return 0

    def joue(self,grille):
        """Place un jeton dans la Grille
        Arg:
        - grille (Grille) : la grille de Jeu
        Returns:
        - ligne (int) :ligne du jeton posé
        - colonne (int) : colonne du jeton posé
        """
        # on choisit une colonne
        colonne = self.choix_colonne(grille)
        # on place le jeton
        placement,ligne = grille.placer_jeton(colonne,self.jeton)
        while not placement :
            colonne =self.choix_colonne(grille)
            placement,ligne = grille.placer_jeton(colonne,self.jeton)
        return ligne,colonne

    def victoire(self):
        """Affiche les messages qui annonce une victoire et met à jour le score"""
        print(MESSAGE_VICTOIRE)
        print(self.nom,ANNONCE_VAINQUEUR)
        self.incrementer_score()
