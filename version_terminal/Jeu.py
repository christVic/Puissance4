import random
from constantes import *
from Grille import Grille
from Participant import Participant

class Jeu:
    """Represente le Jeu."""
    #def __init__(self,nom_joueur,nom_ordinateur,couleur_jeton_joueur,type_jeu_ordinateur):
    def __init__(self,participant1,participant2):

        """Initialise la grille et les participants du jeu"""
        self.grille = Grille()

        self.participant1 = participant1
        self.participant2 = participant2

        """self.joueur = Joueur(nom_joueur,couleur_jeton_joueur)

        couleur_jeton_ordinateur = -1
        if couleur_jeton_joueur == JAUNE:
            couleur_jeton_ordinateur = ROUGE
        else:
            couleur_jeton_ordinateur = JAUNE
        self.ordinateur = Ordinateur(nom_ordinateur, couleur_jeton_ordinateur,type_jeu_ordinateur)
        """

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
        self.grille.afficher_grille()
        compteur = int(random.random() * NB_COLONNES)

        while not self.fin_partie():
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
