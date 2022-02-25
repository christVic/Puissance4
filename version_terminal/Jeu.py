from constantes import *
from Grille import Grille
from Participant import Participant
from Joueur import Joueur
from Ordinateur import Ordinateur

class Jeu:
    """Represente le Jeu."""
    def __init__(self,nom_joueur,nom_ordinateur,couleur_jeton_joueur,type_jeu_ordinateur):
        """Initialise les noms et les couleurs de jeton du joueur et de l'ordinateur ainsi que le type de jeu de l'ordinateur"""
        self.grille = Grille()

        self.joueur = Joueur(nom_joueur,couleur_jeton_joueur)

        couleur_jeton_ordinateur = -1
        if couleur_jeton_joueur == JAUNE:
            couleur_jeton_ordinateur = ROUGE
        else:
            couleur_jeton_ordinateur = JAUNE
        self.ordinateur = Ordinateur(nom_ordinateur, couleur_jeton_ordinateur,type_jeu_ordinateur)

    def action_realisee(self,nom_participant,colonne_choisie):
        """ Décrit une action realisée par un participant
        Args:
        - nom_participant(string) : le nom du participant qui choisi la colonne
        - colonne_choisie (int) : le numero de la colonne choisie
        Return:
        - string
        """
        return ""+nom_participant+" a choisi la colonne "+str(colonne_choisie+1)

    def afficher_score(self):
        """Affiche le score du jeu"""
        print(self.joueur.nom,"(",self.joueur.get_nom_couleur(),"):",self.joueur.score,"-",self.ordinateur.score,":(",self.ordinateur.get_nom_couleur(),")",self.ordinateur.nom)

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
        """Lance/Commence une partie du jeu"""
        self.grille.afficher_grille()
        while not self.fin_partie():
            # Tour du joueur
            choix_joueur = self.joueur.jouer()
            placement_j,ligne_j = self.grille.placer_jeton(choix_joueur,self.joueur.jeton)
            print(self.action_realisee(self.joueur.nom,choix_joueur))
            while not placement_j :
                choix_joueur =self.joueur.jouer()
                placement_j,ligne_j = self.grille.placer_jeton(choix_joueur,self.joueur.jeton)
                print(self.action_realisee(self.joueur.nom,choix_joueur))

            # on affiche la grille
            self.grille.afficher_grille()
            # si il y a assez de jetons alignés
            if self.victoire_partie(ligne_j,choix_joueur):
                self.joueur.victoire()
                print("ligne=",ligne_j+1,"colonne=",choix_joueur+1)
                # fin de la partie / on quitte la boucle
                break

            # Tour de l'ordinateur
            choix_ordinateur = self.ordinateur.jouer()
            placement_o,ligne_o = self.grille.placer_jeton(choix_ordinateur,self.ordinateur.jeton)
            print(self.action_realisee(self.ordinateur.nom,choix_ordinateur))
            while not placement_o :
                choix_ordinateur =self.ordinateur.jouer()
                placement_o,ligne_o = self.grille.placer_jeton(choix_ordinateur,self.ordinateur.jeton)
                print(self.action_realisee(self.ordinateur.nom,choix_ordinateur))
            # on affiche la grille
            self.grille.afficher_grille()
            # si il y a assez de jetons alignés
            if self.victoire_partie(ligne_o,choix_ordinateur):
                self.ordinateur.victoire()
                print("ligne=",ligne_o+1,"colonne=",choix_ordinateur+1)
                # fin de la partie / on quitte la boucle
                break

        self.afficher_score()

    def jeu(self):
        """Demarre/Lance le jeu"""
        print(self.joueur.nom,"(",self.joueur.get_nom_couleur(),") VS (",self.ordinateur.get_nom_couleur(),")",self.ordinateur.nom)
        i = 1
        while 1:
            print("Partie",i)
            self.lancer_partie()
            nouvelle_partie = int(input(TEXTE_INPUT_NOUVELLE_PARTIE))
            if nouvelle_partie == 1:
                i+=1
                self.grille.nettoyer_grille()
                print(self.joueur.nom,"(",self.joueur.get_nom_couleur(),") VS (",self.ordinateur.get_nom_couleur(),")",self.ordinateur.nom)

            else:
                break

        print(MESSAGE_QUITTER_JEU,self.joueur.nom)
