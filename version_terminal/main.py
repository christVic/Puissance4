from constantes import *
from Jeton import Jeton
from Participant import Participant
from Joueur import Joueur
from Ordinateur import Ordinateur
from Grille import Grille
from Jeu import Jeu

import random

nom_joueur = input(TEXTE_INPUT_NOM_JOUEUR)
if not nom_joueur:
    nom_joueur = NOM_DEFAUT_JOUEUR

nom_ordinateur = input(TEXTE_INPUT_NOM_ORDINATEUR)
if not nom_ordinateur:
    nom_ordinateur = NOM_DEFAUT_ORDINATEUR

type_jeton = int(input(TEXTE_INPUT_COULEUR_JETON_JOUEUR))
if type_jeton == ROUGE:
    couleur_jeton = ROUGE
else:
    couleur_jeton = JAUNE
niveau_jeu = int(input(TEXTE_INPUT_NIVEAU_JEU))
if niveau_jeu-1 == JEU_INTELLIGENT:
    type_jeu =JEU_INTELLIGENT
elif niveau_jeu-1 == JEU_IA:
    type_jeu =JEU_IA
else:
    type_jeu =JEU_ALEATOIRE

jeu = Jeu(nom_joueur,nom_ordinateur,couleur_jeton,type_jeu)
jeu.jeu()
