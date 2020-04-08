# P5-OpenFoodFacts

## P5 du parcours DA Python d'OpenClassRoom

### version python
**≥ 3.7**

### Requirements (fichier requirements.txt)
mysql-connector  
requests

### Base de données
MariaDB 10.3
- Créer une base de données et un utilisateur ayant les droits d'admin sur cette base.  
- Modifier le fichier setup.py à la racine du projet en modifiant les variables  
sous #DATABASE
- Lancer le programme avec le parametre -t test pour tester la connexion et les tables
- Lancer le programme avec le parametre -t create pour initialiser ou recréer les données

### Installation
- Récupérer les source dans un repertoire (ie dir)
- Créer un environnement virtuel avec virtualenv, pipenv...
- Installer les modules requis via pip
- positionner la variable d'environnement PYTHONPATH au repertoire d'installation (ie export PYTHONPATH='/home/foo/dir/')
Vous avez alors l'arborescence suivante /home/foo/dir/myapp/...)

### lancement du programme et paramètres
Taper : python3 -m myapp.main
- paramètres  
-t create --> (re)crée les tables et les rempli <br />
-t test --> teste connexion à la base et les tables 

### fin


