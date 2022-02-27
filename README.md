# Puissance4
Implémentation en python du jeu "Puissance4" entre un joueur et l'ordinateur

<!--
# Rappel des règles du jeu
-->

* L'utilisateur peut choisir le type de jeu : Joueur VS Joueur, Joueur VS Ordinateur, Ordinateur VS Ordinateur  
* L'utilisateur peut saisir un pseudo pour les deux participants au jeu, la couleur des jetons et le niveau de difficulté du jeu.
* Il y a deux couleurs de jeton :Rouge et Jaune
* Il y a quatre niveaux de difficulté pour l'ordinateur : facile, moyen, difficile et aléatoire
##### Niveau facile
L'ordinateur place ses jetons dans les colonnes où il aura le plus de jetons alignés
##### Niveau moyen
L'ordinateur place ses jetons dans les colonnes où son adversaire aura le plus de jetons alignés
##### Niveau difficile
L'ordinateur place ses jetons dans les colonnes où l'adversaire aura le plus de jetons alignés et où l'ordinateur aura le plus de jetons alignés
##### Niveau aléatoire
L'ordinateur place ses jetons de manière aléatoire.
# Versions
Nous proposons  2 versions du jeu:
* une version sur le terminal : dossier "version_terminal"
* une version avec une interface graphique : dossier "version_graphique"

## version_terminal
Le jeu s'effectue sur le terminal
### Pré-requis
* Python3

### Lancement du jeu
```
python3 version_terminal/main.py
```
OU
```
cd version_terminal/
python3 main.py
```
### Améliorations possibles
* gerer le bug ordinateur (difficile) vs ordinateur(moyen)
<!--* Afficher le niveau du Jeu-->
<!--* ajouter les exceptions (try/catch)-->

## version_graphique
Le jeu s'effectue sur une interface graphique
### Pré-requis
* Python3
* pygame
### Lancement du jeu
```
python3 version_graphique/main.py
```
OU
```
cd version_graphique/
python3 main.py
```
-->
### Améliorations possibles
* gerer le bug ordinateur (difficile) vs ordinateur(moyen)
