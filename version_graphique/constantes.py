
NB_LIGNES = 6
NB_COLONNES = 7
NB_JETONS_JOUEUR = 21
NB_JETONS_VICTOIRE = 4

LARGEUR_FENETRE = 600
HAUTEUR_FENETRE = 480

LARGEUR_GRILLE = 420
HAUTEUR_GRILLE = 360


# COULEURS
COULEUR_BLEUE = 0,0,255
COULEUR_ROUGE = 255,0,0
COULEUR_JAUNE = 255,255,0
COULEUR_BLANCHE = 255,255,255


# TYPE DE CASE/JETON
# TYPE_JETON_
VIDE = 0
ROUGE = 1
JAUNE = 2

#TYPE_JEU
TYPE_JOUEUR_JOUEUR = 1
TYPE_JOUEUR_ORDINATEUR = 2
TYPE_ORDINATEUR_ORDINATEUR = 3

# TYPE DE CHOIX ORDINATEUR
CHOIX_ORDINATEUR_FACILE = 1
CHOIX_ORDINATEUR_MOYEN = 2
CHOIX_ORDINATEUR_DIFFICILE = 3
CHOIX_ORDINATEUR_ALEATOIRE = 4

# NIVEAU ORDINATEUR
NIVEAU_FACILE = "Facile"
NIVEAU_MOYEN = "Moyen"
NIVEAU_DIFFICILE = "Difficile"
NIVEAU_ALEATOIRE = "Aléatoire"

# NOMS COULEURS
NOM_COULEUR_BLEUE = "bleu"
NOM_COULEUR_ROUGE = "Rouge"
NOM_COULEUR_JAUNE = "Jaune"

# CONSTANTES STRING
NOM_DEFAUT_JOUEUR = "Joueur"
NOM_DEFAUT_JOUEUR1 = "Joueur1"
NOM_DEFAUT_JOUEUR2 = "Joueur2"
NOM_DEFAUT_ORDINATEUR = "Ordinateur"
NOM_DEFAUT_ORDINATEUR1 = "Ordinateur1"
NOM_DEFAUT_ORDINATEUR2 = "Ordinateur2"

NOM_JEU = "PUISSANCE4"
MESSAGE_BIENVENUE = "BIENVENU(E) SUR PUISSANCE4"
MESSAGE_VICTOIRE = "Nous avons un vainqueur: "
ANNONCE_VAINQUEUR = " a remporté la partie !"
MESSAGE_GRILLE_PLEINE = "WOOW! Mais quelle partie! Vous avez tous deux perdu !"
MESSAGE_QUITTER_JEU = "Au revoir "

JOUEUR_VS_JOUEUR = "Joueur VS Joueur"
JOUEUR_VS_ORDINATEUR = "Joueur VS Ordinateur"
ORDINATEUR_VS_ORDINATEUR = "Ordinateur VS Ordinateur"

TEXTE_INPUT_CHOIX_JOUEUR = "Dans quelle colonne (1 à "+str(NB_COLONNES)+") voulez-\
vous placer le jeton? >"
TEXTE_INPUT_NOM_JOUEUR = "Veuillez saisir votre nom (par defaut = "+NOM_DEFAUT_JOUEUR+")\n>"
TEXTE_INPUT_NOM_JOUEUR1 = "Veuillez saisir le nom du joeur1(par defaut = "+NOM_DEFAUT_JOUEUR1+")\n>"
TEXTE_INPUT_NOM_JOUEUR2 = "Veuillez saisir le nom du joeur2(par defaut = "+NOM_DEFAUT_JOUEUR2+")\n>"

TEXTE_INPUT_NOM_ORDINATEUR = "Veuillez saisir le nom de l'Ordinateur (nom par defaut = "+NOM_DEFAUT_ORDINATEUR+")\n>"
TEXTE_INPUT_NOM_ORDINATEUR1 = "Veuillez saisir le nom de l'Ordinateur1 (nom par defaut = "+NOM_DEFAUT_ORDINATEUR1+")\n>"
TEXTE_INPUT_NOM_ORDINATEUR2 = "Veuillez saisir le nom de l'Ordinateur2 (nom par defaut = "+NOM_DEFAUT_ORDINATEUR2+")\n>"

TEXTE_INPUT_COULEUR_JETON_JOUEUR = "Veuillez choisir la couleur de vos jetons [1]Rouge [2]Jaune\n>"
TEXTE_INPUT_COULEUR_JETON_JOUEUR1 = "Veuillez choisir la couleur des jetons du joueur1 [1]Rouge [2]Jaune\n>"
TEXTE_INPUT_COULEUR_JETON_ORDINATEUR1 = "Veuillez choisir la couleur des jetons de l'ordinateur1 [1]Rouge [2]Jaune\n>"

TEXTE_INPUT_NIVEAU_ORDINATEUR = "Choisissez un niveau de difficulté pour l'ordinateur : [1]"+NIVEAU_FACILE+"[2]"+NIVEAU_MOYEN+"[3]"+NIVEAU_DIFFICILE+ "[4]"+NIVEAU_ALEATOIRE+"\n>"
TEXTE_INPUT_NIVEAU_ORDINATEUR1 = "Choisissez un niveau de difficulté pour l'ordinateur1 : [1]"+NIVEAU_FACILE+"[2]"+NIVEAU_MOYEN+"[3]"+NIVEAU_DIFFICILE+ "[4]"+NIVEAU_ALEATOIRE+"\n>"
TEXTE_INPUT_NIVEAU_ORDINATEUR2 = "Choisissez un niveau de difficulté pour l'ordinateur2 : [1]"+NIVEAU_FACILE+"[2]"+NIVEAU_MOYEN+"[3]"+NIVEAU_DIFFICILE+ "[4]"+NIVEAU_ALEATOIRE+"\n>"

TEXTE_INPUT_NOUVELLE_PARTIE = "Voulez-vous lancer une autre partie?[1]Oui [2]Non\n>"
TEXTE_INPUT_TYPE_JEU = "Choisissez le type de jeu : \n[1]"+JOUEUR_VS_JOUEUR+"\n[2]"+JOUEUR_VS_ORDINATEUR+"\n[3]"+ORDINATEUR_VS_ORDINATEUR+"\n[4]Quitter\n>"

# CONSTANTES DIRECTIONS
DIRECTION_HORIZONTALE = (1,0)
DIRECTION_VERTICALE = (0,1)
DIRECTION_DIAGONALE_DROITE = (1,1)
DIRECTION_DIAGONALE_GAUCHE = (1,-1)
