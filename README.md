# Projet Singlefind

![forthebadge](project/badges/projet-nsi-terminale.svg)     ![forthebadge](project/badges/python-flask.svg)     ![forthebadge](project/badges/bootstrap-4.0.svg)      ![forthebadge](project/badges/fait-avec-github.svg)

Singlefind est un projet de site de rencontre développé dans le cadre des cours de NSI.
Le but de ce document est de vous expliquer les prérequis pour que le projet fonctionne pas de vous expliquer son fonctionnement.
Pour avoir des explications sur le fonctionnement sur le projet, nous vous conseillons de lire notre [documentation](https://www.canva.com/design/DAFVMh7-8q8/aPnWPXd2rqjSdGNrK0UxWg/edit?layoutQuery=presentation+de+projet).

## Installation

Après avoir cloner le projet dans un dossier (avec l'archive ou avec git) , ouvrez un terminal avec le répertoire du projet et exécuter la commande suivante :
``python3 -m venv auth``
Cette commande va créer un environnement virtuel qui nous sera utile pour installer les dépendances du projet

Ensuite, pour nous activer l'environnement virtuel il faut lancer la commande suivante :
``source auth/Scripts/activate``
_Cette étape sera à effectuer à chaque fois que vous fermerez le terminal depuis lequel vous lancer le serveur_
Rappelons ici que cette commande et la plupart du projet a été testé uniquement sur windows. Pour un OS de type linux la commande sera :
``source auth/bin/activate``

Une fois l'environnement virtuel activé il faut installer les modules python nécéssaires au fonctionnement du projet
``pip install flask flask_login flask_sqlalchemy geopy``
En effet, Flask est le framework dont nous nous servons pour le serveur.

Maintenant nous allons définir le répertoire de notre dossier grâce à cette commande
``export FLASK_APP=project``
_Cette étape sera à effectuer à chaque fois que vous fermerez le terminal depuis lequel vous lancer le serveur_

Si vous avez réussi à exécuter toutes ses commandes sans erreur le projet devrait être prêt à fonctionner.

### Démarrage

Une fois le projet correctement installé, exécuter la commande ``flask run``, elle permettra l'initialisation du serveur et de la base de données.
Pour vous connecter au serveur, lancez votre navigateur préféré et tapez "localhost:5000" : il s'agit de l'adresse du serveur sur votre machine.  

### Erreurs possibles

Vous pourriez recontrer plusieurs erreurs lors de votre tentative d'installation et de démarrage du projet, voici les plus fréquentes :

- ``flask: command not found`` => Celle-ci se produit lorsque l'environnement virtuel n'est pas initialisé ou lorsque les dépendances ne sont pas installées
- ``Error: could not locate a Flask application`` => Vous pouvez rencontrer cette erreur si vous avez mal définit la variable FLASK_APP
- ``Error: could not import 'project.project`` => Pour résoudre cette erreur un simple ``cd ..`` suffira.

Si vous croisez d'autres erreurs essayer dans un premier temps de les résoudre vous-mêmes (grâce à des forums), puis dans un deuxième temps, contactez les contributeurs du projet dont la liste de trouve plus bas.

## Fabriqué avec

Pour développer ce projet nous avons utilisé les programmes/logiciels suivants :

* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - Framework CSS & JS (frontend)
* [Visual Studio Code](https://code.visualstudio.com) - Editeur de code
* [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Framework Python (backend)
* [Github](https://github.com) - Système de contrôle de version

## Auteurs
Liste des membres du projet :
* **Tristan** _alias_ [@Skiifig](https://github.com/Skiifig)
* **Louis** _alias_ [@compotecassis](https://github.com/compotescassis)

Retrouvez la liste des contributeurs [ici](https://github.com/skiifig/project-sf/contributors) pour voir qui à aidé au projet !
