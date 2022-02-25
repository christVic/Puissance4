#
NB_LIGNES = 6
NB_COLONNES = 7
NB_JETONS_JOUEUR = 21
NB_JETONS_VICTOIRE = 4

# TYPE DE CASE/JETON
VIDE = 0 #case vide
ROUGE = 1
JAUNE = 2

# TYPE DE JEU ORDINATEUR
JEU_ALEATOIRE = 0 # niveau facile
JEU_INTELLIGENT = 1 # niveau moyen
JEU_IA = 2 # niveau difficile

# NIVEAU Jeu
FACILE = "Facile"
MOYEN = "Moyen"
DIFFICILE = "Difficile"

# CONSTANTES COULEURS
COULEUR_BLEUE = "bleu"
COULEUR_ROUGE = "Rouge"
COULEUR_JAUNE = "Jaune"

# CONSTANTES STRING
NOM_DEFAUT_JOUEUR = "Joueur"
NOM_DEFAUT_ORDINATEUR = "Ordinateur"

TEXTE_INPUT_CHOIX_JOUEUR = "Dans quelle colonne (1 à "+str(NB_COLONNES)+") voulez-\
vous placer le jeton? >"
TEXTE_INPUT_NOM_JOUEUR = "Veuillez saisir votre nom (par defaut = "+NOM_DEFAUT_JOUEUR+")\n>"
TEXTE_INPUT_NOM_ORDINATEUR = "Veuillez saisir le nom de l'Ordinateur (nom par defaut = "+NOM_DEFAUT_ORDINATEUR+")\n>"
TEXTE_INPUT_COULEUR_JETON_JOUEUR = "Veuillez choisir la couleur de vos jetons [1]Rouge [2]Jaune\n>"
TEXTE_INPUT_NIVEAU_JEU = "Choisissez un niveau de difficulté : [1]Facile [2]Moyen [3]Difficile\n>"
TEXTE_INPUT_NOUVELLE_PARTIE = "Voulez-vous lancer une autre partie?[1]Oui [2]Non\n>"

MESSAGE_VICTOIRE = "Nous avons un vainqueur: "
ANNONCE_VAINQUEUR = " a remporté la partie !"
MESSAGE_QUITTER_JEU = "Au revoir "

# CONSTANTES DIRECTIONS
DIRECTION_HORIZONTALE = (1,0)
DIRECTION_VERTICALE = (0,1)
DIRECTION_DIAGONALE_DROITE = (1,1)
DIRECTION_DIAGONALE_GAUCHE = (1,-1)
