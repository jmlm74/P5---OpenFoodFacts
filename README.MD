# P5-OpenFoodFacts  

## P5 du parcours DA Python d'OpenClassRoom

### version python
**≥ 3.7**

### Requirements (fichier requirements.txt)
mysql-connector  == 2.2.9  
prompt-toolkit  == 1.0.14  
PyInquirer  == 1.0.3  
pretty_Table  == 0.7.2   
requests  == 2.23.0  

### Base de données
MariaDB 10.3
- Créer une base de données et un utilisateur ayant les droits d'admin sur cette base.  
- Modifier le fichier setup.py à la racine du projet en modifiant les variables  
sous #DATABASE
- Lancer le programme avec le parametre -t test pour tester la connexion et les tables
- Lancer le programme avec le parametre -t create pour initialiser ou recréer les données

### Installation
* Récupérer les source dans un repertoire (ie dir)
* Créer un environnement virtuel avec virtualenv, pipenv...
* Installer les modules requis via pip
* Positionner la variable d'environnement PYTHONPATH au repertoire d'installation (ie export PYTHONPATH='/home/foo/dir/')
* Vous avez alors l'arborescence suivante /home/foo/dir/myapp/...)

### lancement du programme et paramètres
Taper : python3 -m myapp.main
- paramètres  
-t create --> (re)crée les tables et les rempli <br />
-t test --> teste connexion à la base et les tables 

### Menus et fonctionnalités
**Menu :**   
1 - Categories  
2 - Liste aliments substitués  
<br />
**Menu 1.1 :**  
Liste categories --> choix d'une categorie  
<br />
**Menu 1.2 :**
Liste des produits de la catégorie choisie --> Possibilité d'en choisir 1  
<br />
**Menu 1.3 :**
Display du détail du produit choisi en 1.2  
Display d'un tableau des alimentsqui peuvent substituer celui choisi  
   Possibilité d'en choisir un ou plusieurs pour pouvoir les retrouver ultérieurement en tant qu'aliments de substitution  
<br />
     
**Menu 2.1 :**
Liste des aliments et des aliments qui leur sont sbstituables  
Possibilité de selectionner 1 article pour en afficher les détail et le détail de ses aliments de substitution  
