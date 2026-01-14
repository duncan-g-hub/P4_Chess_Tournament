# P4 : Application d'organisation de tournois d'échecs

Projet réalisé dans le cadre du développement d'un logiciel d'organisation pour un club d'échecs.

Il s'agit d'une application permettant la gestion et l'organisation de tournois d'échecs.

L'objectif est de constituer un outil qui ne nécessite aucune connexion internet et qui permet de sauvegarder et d'afficher les données de chaque tournoi.

---

## Fonctionnalités

- Gestion des joueurs : 
  - Ajouter des joueurs
- Gestion des tournois : 
  - Ajouter des tournois
  - Sélection d'un tournoi :
    - Ajouter des joueurs au tournoi
    - Commencer un tournoi
- Gestion des matchs et tours : 
  - Génération de paires de joueurs uniques pour chaque tour
  - Déroulement d'un tournoi sous forme de tours
  - Déroulement d'un tour sous forme de match
- Sauvegarde des données dans des fichiers .json : 
  - Données joueurs : `/data/players.json`
  - Données tournois : `/data/tournaments.json`
- Afficher des rapports : 
  - Afficher les joueurs
  - Afficher les tournois
  - Afficher les informations d'un tournoi
  - Afficher les joueurs inscrits à un tournoi 
  - Afficher les tours et matchs liés à un tournoi

---

## Architecture

Le projet suit une architecture de type MVC :
- Models : logique métier, gestion des données et entités
- Views : interface en ligne de commande
- Controllers : coordination entre modèles et vues

---

## Structure du projet

```
P4_Chess_Tournament/
    main.py                             # Point d'entrée de l'application
    requirements.txt                    # Dépendances
    README.md                           # Documentation
    .gitignore                          # Liste des dossiers et fichiers à ignorer pour le repository
    .flake8                             # Paramètres rapport flake8
    
    models/                             # Package contenant les modèles
        __init__.py                     # Fichier d'initialisation du package
        constants.py                    # Gère le chemin et la création du dossier `data/`
        match.py                        # Gère une paire de joueur, attribue des couleurs et met les scores à jour
        player.py                       # Gère les informations personnelles et le score d'un joueur
        tournament.py                   # Gère les joueurs, les tours et les informations générales du tournoi
        turn.py                         # Gère la génération des paires, les matchs joués et les dates de début et de fin
    
    controllers/                        # Package contenant les contrôleurs
        __init__.py                     # Fichier d'initialisation du package
        list_sorter.py                  # Contient des fonctions de tri de liste
        main_menu_controller.py         # Gère les fonctionnalités liées au menu principal
        tournament_controller.py        # Gère le déroulement complet d'un tournoi
        tournament_menu_controller.py   # Gère les fonctionnalités liées au menu d'un tournoi
    
    views/                              # Package contenant les vues
        __init__.py                     # Fichier d'initialisation du package
        input_checker.py                # Contrôle la validité d'une saisie
        input_format.py                 # Nettoie les données d'entrée pour le stockage
        main_menu_view.py               # Gère l'affichage du menu principal
        message_view.py                 # Gère l'affichage des messages
        player_view.py                  # Gère l'affichage et la saisie des informations liées aux joueurs
        players_in_tournament_view.py   # Gère l'affichage et la saisie des informations liées aux joueurs dans un tournoi
        tournament_view.py              # Gère l'affichage et la saisie des informations liées aux tournois
    
    data/                               # Généré automatiquement (non inclus dans le repo GitHub)
        players.json                    # Données des joueurs sauvegardés
        tournaments.json                # Données des tournois sauvegardés
    
    flake8_rapport/                     # Fichiers issus du rapport flake8-html
    
    
    

```

---

## Technologies utilisées

- Python 3.13
- Librairies standards : random, datetime, pathlib, json
- flake8
- flake8-html

---

## Limitations connues

- Interface uniquement en ligne de commande
- Pas de gestion multi-utilisateur
- Données stockées localement en fichiers JSON

---

## Installation 

### Prérequis :

- Python 3.10 ou plus récent
- Connexion Internet uniquement pour la récupération du code via GitHub et l'installation des dépendances 

### Cloner le repository : 

```bash
git clone https://github.com/duncan-g-hub/P4_Chess_Tournament.git
cd P4_Chess_Tournament/
```

### Créer et activer l'environnement virtuel : 

```bash
cd P4_Chess_Tournament/
python -m venv env 
source env/Scripts/activate
```

### Installer les dépendances : 

```bash
cd P4_Chess_Tournament/
pip install -r requirements.txt
```

---

## Exécution de l'application

```bash
cd P4_Chess_Tournament/
python main.py
```
Le menu principal apparaîtra dans le terminal sous forme de ligne de commande. 

---

## Mise à jour du rapport flake8-html

```bash
cd P4_Chess_Tournament/
flake8 --format=html --htmldir=flake8_rapport
```
Le contenu du dossier `flake8_rapport/` sera remplacé par le nouveau rapport flake8.
Glisser-déposer le fichier index.html dans un navigateur internet pour visualiser le rapport.

---

## Contact

Pour toute question :  
Duncan GAURAT - duncan.dev@outlook.fr

            
