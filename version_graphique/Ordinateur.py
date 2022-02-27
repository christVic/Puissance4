import random

from constantes import *
from Jeton import Jeton
from Participant import Participant
#from Grille import Grille

class Ordinateur(Participant):
    """Represente l'Ordinateur."""

    def __init__(self, nom,couleur_jeton,type_choix):
        """Initialise le nom, la couleur du jeton et le niveau de l'ordinateur"""
        super(Ordinateur, self).__init__(nom,couleur_jeton)
        self.type_choix = type_choix

    def choix_colonne(self,grille):
        """Donne la colonne choisie par l'ordinateur selon son type de choix
        Arg:
        - grille (Grille) : la grille utilisée pour simuler le placement des jetons
        Return:
        - un entier : le numero de colonne
        """
        if grille.est_vide():
            return self.choix_aleatoire()
        if self.type_choix == CHOIX_ORDINATEUR_FACILE :
            return self.choix_meilleur_coup_ordinateur(grille)
        elif self.type_choix == CHOIX_ORDINATEUR_MOYEN :
            return self.choix_meilleur_coup_adversaire(grille)
        elif self.type_choix == CHOIX_ORDINATEUR_DIFFICILE:
            return self.choix_meilleur_coup(grille)
        return self.choix_aleatoire()

    def choix_aleatoire(self):
        """Choisi aléatoirement un numero de colonne entre 0 et NB_COLONNES
        Return:
        - int
        """
        return int(random.random() * NB_COLONNES)

    def choix_meilleur_coup_ordinateur(self,grille):
        """Calcule la colonne à jouer où l'ordinateur aura le plus de jetons alignés
        Arg:
        - grille (Grille) : la copie de la grille utilisé pour simuler le placement des jetons
        Return:
        - int
        """
        max_jetons = 1
        best_colonne = 0
        # on simule la pose d'un jeton de l'ordinateur sur chaque colonne
        # la colonne à choisir est celle qui permettra d'obtenir le plus grand nombre de jetons alignés
        for i in range(grille.nb_colonnes):
            if grille.coup_possible(i):
                placement,ligne = grille.placer_jeton(i,self.jeton)
                nb_jetons = grille.compter_jetons(ligne,i)
                # on efface le jeton posé
                grille.set_case_grille_vide(ligne,i)

                if nb_jetons>max_jetons:
                    max_jetons = nb_jetons
                    best_colonne = i
        print("choix ordinateur =",best_colonne)
        return best_colonne

    def choix_meilleur_coup_adversaire(self,grille):
        """Calcule la colonne à jouer où l'adversaire' aura le plus de jetons alignés
        Arg:
        - grille (Grille) : la grille du jeu utilisé pour simuler le placement des jetons
        Return:
        - int
        """
        # on trouve la couleur du jeton de l'adversaire
        jeton_adversaire = Jeton(ROUGE)
        if self.jeton.valeur == ROUGE:
            jeton_adversaire = Jeton(JAUNE)

        max_jetons = 1
        best_colonne = 0
        # on simule la pose d'un jeton de l'adversaire sur chaque colonne
        # la colonne à choisir est celle qui permettra d'obtenir le plus grand nombre de jetons alignés
        for i in range(grille.nb_colonnes):
            if grille.coup_possible(i):
                placement,ligne = grille.placer_jeton(i,jeton_adversaire)
                nb_jetons = grille.compter_jetons(ligne,i)
                # on efface le jeton posé
                grille.set_case_grille_vide(ligne,i)

                if nb_jetons>max_jetons:
                    max_jetons = nb_jetons
                    best_colonne = i
        print("choix ordinateur =",best_colonne)
        return best_colonne

    def choix_meilleur_coup(self,grille):
        """Calcule la colonne à jouer où l'adversaire aura le plus de chance de perdre
        Arg:
        - grille (Grille) : la copie de la grille utilisé pour simuler le placement des jetons
        Return:
        - int
        """
        # on trouve la couleur du jeton de l'adversaire
        jeton_adversaire = Jeton(ROUGE)
        if self.jeton.valeur == ROUGE:
            jeton_adversaire = Jeton(JAUNE)

        max_jetons_adversaire = []
        max_jetons = []

        # on simule la pose d'un jeton de l'ordinateur sur chaque colonne
        for i in range(grille.nb_colonnes):
            nb_jetons = 0
            if grille.coup_possible(i):
                placement,ligne = grille.placer_jeton(i,self.jeton)
                nb_jetons = grille.compter_jetons(ligne,i)
                # on efface le jeton posé
                grille.set_case_grille_vide(ligne,i)
            max_jetons.append(nb_jetons)

        # on simule la pose d'un jeton de l'adversaire sur chaque colonne
        for i in range(grille.nb_colonnes):
            nb_jetons = 0
            if grille.coup_possible(i):
                placement,ligne = grille.placer_jeton(i,jeton_adversaire)
                nb_jetons = grille.compter_jetons(ligne,i)
                # on efface le jeton posé
                grille.set_case_grille_vide(ligne,i)
            max_jetons_adversaire.append(nb_jetons)

        max_a = max(max_jetons_adversaire)
        max_o = max(max_jetons)

        # on compare les plus longs alignement de l'ordinateur et de l'adversaire
        if max_a>max_o:
            return max_jetons_adversaire.index(max_a)
        return max_jetons.index(max_o)
