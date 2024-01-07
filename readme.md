# Projet Bataille navale — NSI T°

## Description

Ce projet de Bataille Navale, développé dans le cadre de la matière NSI (Numérique et Sciences Informatiques) en
Terminale générale, vise à mettre en pratique et évaluer nos compétences acquises durant l'année de Première et le début
de la Terminale. Il s'agit d'un travail de groupe qui combine programmation, utilisation de bases de données, et
développement d'interfaces graphiques...

Ce projet a été réalisé du 12/12/2023 au 7/01/2024, les auteurs sont Léo Lesimple, Timothée Gallier et Léa-Angélina
Kolmerschlag, il est distribué sous la license CC BY-NC-ND 4.0, voir en bas de page le détail, une copie de la license
est disponibles dans le fichier LICENSE.

## Prérequis

- Python : Une version récente de Python (3.x) doit être installée. Le projet a été développé avec Python 3.8, mais il
  devrait être compatible avec les versions ultérieures.

- Bibliothèques Python :

    - Tkinter : Pour l'interface graphique. Tkinter est généralement inclus dans les installations standard de Python.
    - SQLite3 : Utilisé pour la gestion de la base de données. Cette bibliothèque est normalement incluse dans les
      distributions standard de Python.
    - Pyglet (optionnel) : Pour la gestion des sons dans le jeu, si utilisé.
    - SQLite : Une base de données SQLite est requise pour stocker les informations des joueurs et leurs scores. Le
      fichier de base de données doit être nommé general.db.

## Utilisation

- Pour lancer le jeu, il suffit de lancer depuis votre environnement de développement ou depuis votre terminal.
    - Pour lancer depuis le terminal :

    1. Pointer le dossier (répertoire) où sont stockés les fichiers du jeu.
    2. Taper ``` python index.py ``` ou ``` py index.py ``` selon votre installation
    3. Le jeu est lancé !

## Fonctionnalités implémentées

<details>
    <summary> Cliquez pour lire les fonctionnalités.</summary>

### Sélection des Joueurs :

Choix des joueurs parmi une liste existante dans une base de données.
Vérification pour s'assurer que les deux joueurs sélectionnés sont différents.

### Gestion des Joueurs dans la Base de Données :

Ajout de nouveaux joueurs dans la base de données.
Suppression de joueurs existants de la base de données.

### Affichage et Gestion du Tableau des Scores (Leaderboard) :

Affichage des scores des joueurs.
Mise à jour des scores en fonction des performances dans le jeu.

### Configuration du Jeu :

Configuration des paramètres initiaux du jeu, comme le placement des bateaux.

### Déroulement du Jeu :

Gestion des tours entre les joueurs.
Placement des bateaux sur la grille de jeu.
Exécution des tirs et gestion des résultats (touché, manqué, coulé).
Détection et annonce du gagnant.

### Interface Graphique Utilisateur :

Fenêtres et interfaces graphiques pour la configuration du jeu, le jeu lui-même, et l'affichage des scores.
Boutons interactifs pour diverses actions dans le jeu.

### Gestion des Erreurs :

Messages d'erreur pour guider les utilisateurs lors de situations incorrectes (par exemple, sélection de joueurs
identiques).

### Jouer des Effets Sonores (non actif):

Lecture de sons d'ambiance pendant le jeu.

### Fin du Jeu :

Affichage d'un écran de fin de jeu avec le nom du gagnant.
Option pour fermer le jeu ou afficher le tableau des scores.

### Menu Principal :

Écran d'accueil offrant des options pour commencer une nouvelle partie ou consulter le tableau des scores.

### Crédits du Jeu :

Affichage des noms des développeurs ou contributeurs du jeu.

</details>

## Dépannage :

**Au lancement de nouvelles fenêtres, celle-ci a de temps en temps besoin d'être déplacée pour fonctionner, nous
espérons trouver la solution à ce problème au plus vite !**

## Commentaires : 
- La partie de code produite par Léo est essentiellement formulée en anglais par habitude sur d'autres projets.

## Crédits images 
Fond mer : <a href="https://www.freepik.com/free-photo/background-sea-water_4433046.htm#query=ocean%20texture&position=4&from_view=keyword&track=ais&uuid=531d7c86-377e-43e9-a98e-0c378f0d8e39">Image by kdekiara</a> on Freepik

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/LeoL456/Bataille-Navale">Projet Bataille Navale</a> © 2024 by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/LeoL456/">Léo Lesimple, Timothée Gallier, Léa-Angélina Kolmerschlag</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-ND 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1"></a></p>