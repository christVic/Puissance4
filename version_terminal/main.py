from constantes import *
from Jeton import Jeton
from Participant import Participant
from Joueur import Joueur
from Ordinateur import Ordinateur
from Grille import Grille
from Jeu import Jeu

import random

def jeu_joueur_joueur():
    # joueur1
    nom_joueur1 = input(TEXTE_INPUT_NOM_JOUEUR1)
    if not nom_joueur1:
        nom_joueur1 = NOM_DEFAUT_JOUEUR1

    couleur_jeton1 = int(input(TEXTE_INPUT_COULEUR_JETON_JOUEUR1))
    while couleur_jeton1>2 or couleur_jeton1<1:
        couleur_jeton1 = int(input(TEXTE_INPUT_COULEUR_JETON_JOUEUR1))
    # joueur2
    nom_joueur2 = input(TEXTE_INPUT_NOM_JOUEUR2)
    if not nom_joueur2:
        nom_joueur2 = NOM_DEFAUT_JOUEUR2

    couleur_jeton2 = ROUGE
    if couleur_jeton1 == ROUGE:
        couleur_jeton2 = JAUNE

    joueur1 = Joueur(nom_joueur1,couleur_jeton1)
    joueur2 = Joueur(nom_joueur2,couleur_jeton2)

    jeu = Jeu(joueur1,joueur2)
    jeu.jeu()

def jeu_joueur_ordinateur():
    # joueur
    nom_joueur = input(TEXTE_INPUT_NOM_JOUEUR)
    if not nom_joueur:
        nom_joueur = NOM_DEFAUT_JOUEUR

    couleur_jeton1 = int(input(TEXTE_INPUT_COULEUR_JETON_JOUEUR))
    while couleur_jeton1>2 or couleur_jeton1<1:
        couleur_jeton1 = int(input(TEXTE_INPUT_COULEUR_JETON_JOUEUR))
    # ordinateur
    nom_ordinateur = input(TEXTE_INPUT_NOM_ORDINATEUR)
    if not nom_ordinateur:
        nom_ordinateur = NOM_DEFAUT_ORDINATEUR

    couleur_jeton2 = ROUGE
    if couleur_jeton1 == ROUGE:
        couleur_jeton2 = JAUNE

    niveau_ordinateur = int(input(TEXTE_INPUT_NIVEAU_ORDINATEUR))
    while niveau_ordinateur>4 or niveau_ordinateur<1:
        niveau_ordinateur = int(input(TEXTE_INPUT_NIVEAU_ORDINATEUR))

    joueur = Joueur(nom_joueur,couleur_jeton1)
    ordinateur = Ordinateur(nom_ordinateur,couleur_jeton2,niveau_ordinateur)

    jeu = Jeu(joueur,ordinateur)
    jeu.jeu()

def jeu_ordinateur_ordinateur():
    # ordinateur1
    nom_ordinateur1 = input(TEXTE_INPUT_NOM_ORDINATEUR1)
    if not nom_ordinateur1:
        nom_ordinateur1 = NOM_DEFAUT_ORDINATEUR1

    couleur_jeton1 = int(input(TEXTE_INPUT_COULEUR_JETON_ORDINATEUR1))
    while couleur_jeton1>2 or couleur_jeton1<1:
        couleur_jeton1 = int(input(TEXTE_INPUT_COULEUR_JETON_ORDINATEUR1))

    niveau_ordinateur1 = int(input(TEXTE_INPUT_NIVEAU_ORDINATEUR1))
    while niveau_ordinateur1>4 or niveau_ordinateur1<1:
        niveau_ordinateur1 = int(input(TEXTE_INPUT_NIVEAU_ORDINATEUR1))

    # ordinateur2
    nom_ordinateur2 = input(TEXTE_INPUT_NOM_ORDINATEUR2)
    if not nom_ordinateur2:
        nom_ordinateur2 = NOM_DEFAUT_ORDINATEUR2

    couleur_jeton2 = ROUGE
    if couleur_jeton1 == ROUGE:
        couleur_jeton2 = JAUNE

    niveau_ordinateur2 = int(input(TEXTE_INPUT_NIVEAU_ORDINATEUR2))
    while niveau_ordinateur2>4 or niveau_ordinateur2<1:
        niveau_ordinateur2 = int(input(TEXTE_INPUT_NIVEAU_ORDINATEUR2))

    ordinateur1 = Ordinateur(nom_ordinateur1,couleur_jeton1,niveau_ordinateur1)
    ordinateur2 = Ordinateur(nom_ordinateur2,couleur_jeton2,niveau_ordinateur2)

    jeu = Jeu(ordinateur1,ordinateur2)
    jeu.jeu()


print(MESSAGE_BIENVENUE)

type_jeu = int(input(TEXTE_INPUT_TYPE_JEU))
while type_jeu>4 or type_jeu<1:
    type_jeu = int(input(TEXTE_INPUT_TYPE_JEU))

if type_jeu == TYPE_JOUEUR_JOUEUR:
    jeu_joueur_joueur()
elif type_jeu == TYPE_JOUEUR_ORDINATEUR:
    jeu_joueur_ordinateur()
elif type_jeu == TYPE_ORDINATEUR_ORDINATEUR:
    jeu_ordinateur_ordinateur()
else:
    print(MESSAGE_QUITTER_JEU)
    exit()

"""
nom_joueur = input(TEXTE_INPUT_NOM_JOUEUR)
if not nom_joueur:
    nom_joueur = NOM_DEFAUT_JOUEUR

nom_ordinateur = input(TEXTE_INPUT_NOM_ORDINATEUR)
if not nom_ordinateur:
    nom_ordinateur = NOM_DEFAUT_ORDINATEUR

couleur_jeton = int(input(TEXTE_INPUT_COULEUR_JETON_JOUEUR))
while couleur_jeton>2 or couleur_jeton<1:
    couleur_jeton = int(input(TEXTE_INPUT_COULEUR_JETON_JOUEUR))
niveau_jeu = int(input(TEXTE_INPUT_NIVEAU_JEU))
if niveau_jeu-1 == JEU_INTELLIGENT:
    type_jeu =JEU_INTELLIGENT
elif niveau_jeu-1 == JEU_IA:
    type_jeu =JEU_IA
else:
    type_jeu =JEU_ALEATOIRE

jeu = Jeu(nom_joueur,nom_ordinateur,couleur_jeton,type_jeu)
jeu.jeu()
"""
