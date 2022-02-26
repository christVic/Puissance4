from constantes import *
from Jeton import Jeton
class Grille:
    """Represente la Grille."""
    nb_lignes = NB_LIGNES
    nb_colonnes = NB_COLONNES
    grille = []

    def __init__(self):
        """Initialise la grille"""
        for i in range(self.nb_lignes):
            ligne = [Jeton(VIDE)] * self.nb_colonnes
            self.grille.append(ligne)

    def set_case_grille(self,ligne,colonne,jeton):
        """Modifie le jeton situé sur la ligne et la colonne
        Args:
        -ligne (int)
        -colonne (int)
        -jeton (Jeton)
        """
        self.grille[ligne][colonne] = jeton

    def set_case_grille_vide(self,ligne,colonne):
        """Remplace le jeton situé sur la ligne et la colonne par le jeton VIDE
        Args:
        -ligne (int)
        -colonne (int)
        """
        self.grille[ligne][colonne] = Jeton(VIDE)

    def nettoyer_grille(self):
        """Vide la grille"""
        for ligne in range(len(self.grille)):
            for colonne in range(len(self.grille[ligne])):
                self.grille[ligne][colonne] = Jeton(VIDE)

    def afficher_grille(self):
        """Affiche la Grille et son contenu :
        les lignes sont affichées par index decroissant"""
        self.grille.reverse()
        for ligne in self.grille:
            print(end=" ")
            for colonne in ligne:
                colonne.afficher()
            print()
        self.grille.reverse()

    def coup_possible(self, colonne):
        """Determine si il est possible de jouer dans la colonne.
        Arg:
        - colonne (int) : La colonne dans laquelle on cherche la ligne vide
        Return:
        - Boolean
        """
        if colonne >= 0 and colonne < self.nb_colonnes:
            return self.grille[self.nb_lignes-1][colonne].est_vide()
        return False

    def premiere_ligne_disponible(self,colonne):
        """Cherche la première ligne non vide de la colonne passée en argument.
        Necessite de tester si le coup est possible avant d'appeler la méthode
        Arg:
        - colonne (int) : La colonne dans laquelle on cherche la ligne vide
        Return:
        - ligne (int) : la premiere ligne non vide
        """
        ligne = 0
        while not self.grille[ligne][colonne].est_vide() :
            ligne += 1
        return ligne

    def placer_jeton(self,colonne,jeton):
        """Place le jeton dans la colonne donnée si c'est coup_possible
        Arg:
        - colonne (int) : La colonne dans laquelle on veut jouer
        - jeton (Jeton) : Le jeton à placer
        Return:
        - boolean : indique si le placement a reussi
        - ligne : la ligne où est placé le jeton
        """
        if self.coup_possible(colonne):
            ligne = self.premiere_ligne_disponible(colonne)
            self.grille[ligne][colonne] = jeton
            return True,ligne
        #else:
        #print("Colonne ",colonne+1," déjà remplie")
        return False,NB_LIGNES

    def compter_jetons_direction(self,ligne,colonne,direction):
        """Compte les jetons de meme couleur que le jeton de la case grille[ligne][colonne].
        Le compte s'effectue dans la direction donnée.
        Args:
        - ligne (int) : ligne du jeton
        - colonne (int) : colonne du jeton
        - direction ((int,int)) : direction de la recherche (x,y)
        Return:
        - nombre (int) : le nombre de jetons aligné trouvé
        """
        jeton = self.grille[ligne][colonne]
        nb_jetons = 1       # le jeton lui-meme
        nb_jeton_bon_sens = 0
        nb_jetons_sens_oppose = 0

        # on compte dans le bon sens
        ligne_direction = ligne + direction[1]
        colonne_direction = colonne + direction[0]

        while (ligne_direction >= 0) and (ligne_direction < self.nb_lignes) and (colonne_direction >= 0) and (colonne_direction < self.nb_colonnes):
            if self.grille[ligne_direction][colonne_direction].valeur == jeton.valeur :
                ligne_direction += direction[1]
                colonne_direction += direction[0]
                nb_jeton_bon_sens += 1
            else:
                break

        # on compte dans le sens opposé
        ligne_direction = ligne - direction[1]
        colonne_direction = colonne - direction[0]

        while (ligne_direction >= 0) and (ligne_direction < self.nb_lignes) and (colonne_direction >= 0) and (colonne_direction < self.nb_colonnes):
            if self.grille[ligne_direction][colonne_direction].valeur == jeton.valeur :
                ligne_direction -= direction[1]
                colonne_direction -= direction[0]
                nb_jetons_sens_oppose += 1
            else:
                break

        # on additionne les valeurs obtenues
        nb_jetons += (nb_jeton_bon_sens + nb_jetons_sens_oppose)

        return nb_jetons

    def compter_jetons(self,ligne,colonne):
        """Compte les jetons de meme couleur que le jeton de la case grille[ligne][colonne]
        Le compte s'effectue à l'horizontale, à la verticale et sur la verticale (gauche et droite)
        Args:
        - ligne (int) : ligne du jeton
        - colonne (int) : colonne du jeton
        Return:
        - nombre (int) : le plus grand nombre de jetons trouvé
        """
        nb_jetons = 1

        if not self.grille[ligne][colonne].est_vide():
            # on compte les jetons pour chaque directions
            horizontale = self.compter_jetons_direction(ligne,colonne,DIRECTION_HORIZONTALE)
            verticale = self.compter_jetons_direction(ligne,colonne,DIRECTION_VERTICALE)
            diagonale_gauche = self.compter_jetons_direction(ligne,colonne,DIRECTION_DIAGONALE_GAUCHE)
            diagonale_droite = self.compter_jetons_direction(ligne,colonne,DIRECTION_DIAGONALE_DROITE)

            nb_jetons = max(horizontale,verticale,diagonale_droite,diagonale_gauche,nb_jetons)

        return nb_jetons

    def est_plein(self):
        """Determine si la grille est pleine
        Return:
        - Boolean
        """
        for i in range(self.nb_colonnes):
            if self.coup_possible(i):
                return False
        return True

    def est_vide(self):
        for case in self.grille[0]:
            if not case.est_vide():
                return False
        return True
