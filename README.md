# Projet Singlefind

![forthebadge](project/badges/projet-nsi-terminale.svg)     ![forthebadge](project/badges/python-flask.svg)     ![forthebadge](project/badges/bootstrap-4.0.svg)      ![forthebadge](project/badges/fait-avec-github.svg)

Singlefind est un projet de site de rencontre développé dans le cadre des cours de NSI
Le but de ce document est de vous expliquer les prérequis pour que le projet fonctionne pas de vous expliquer son fonctionnement
Pour avoir des explications sur le fonctionnement sur le projet, nous vous conseillons de lire notre documentation.

### Installation

Après avoir cloner le projet dans un dossier (avec l'archive ou avec git) , ouvrez un terminal avec le répertoire du projet et exécuter la commande suivante :
``python3 -m venv auth``
Cette commande va créer un environnement virtuel qui nous sera utile pour installer les dépendances du projet

Ensuite, pour nous activer l'environnement virtuel il faut lancer la commande suivante :
``source auth/Scripts/activate``
Rappelons ici que cette commande et la plupart du projet a été testé uniquement sur windows. Pour un OS de type linux la commande sera :
``source auth/bin/activate``

Une fois l'environnement virtuel activé il faut installer les modules python nécéssaires au fonctionnement du projet
``pip install flask flask_login flask_sqlalchemy``
En effet, Flask est le framework dont nous nous servons pour le serveur.

Maintenant nous allons définir le répertoire de notre dossier grâce à cette commande
``export FLASK_APP=project``
Cette dernière étape sera à effectuer à chaque fois que vous fermerez le terminal depuis lequel vous lancer le serveur

Si vous avez réussi à exécuter toutes ses commandes sans erreur le projet devrait être prêt à fonctionner.

### Erreurs possibles

Vous pourriez recontrer plusieurs erreurs lors de votre tentative d'installation du projet

## Démarrage

Pour démarrer le projet 

## Fabriqué avec

Entrez les programmes/logiciels/ressources que vous avez utilisé pour développer votre projet

_exemples :_
* [Materialize.css](http://materializecss.com) - Framework CSS (front-end)
* [Atom](https://atom.io/) - Editeur de textes

## Contributing

Si vous souhaitez contribuer, lisez le fichier [CONTRIBUTING.md](https://example.org) pour savoir comment le faire.

## Versions
Listez les versions ici 
_exemple :_
**Dernière version stable :** 5.0
**Dernière version :** 5.1
Liste des versions : [Cliquer pour afficher](https://github.com/your/project-name/tags)
_(pour le lien mettez simplement l'URL de votre projets suivi de ``/tags``)_

## Auteurs
Listez le(s) auteur(s) du projet ici !
* **Jhon doe** _alias_ [@outout14](https://github.com/outout14)

Lisez la liste des [contributeurs](https://github.com/your/project/contributors) pour voir qui à aidé au projet !

_(pour le lien mettez simplement l'URL de votre projet suivi de ``/contirubors``)_

## License

Ce projet est sous licence ``exemple: WTFTPL`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations



Singlefind est un projet de site de rencontre
Il utilise les languages suivantes : Python , Css, Javascript, Html
Avec les modules suivants : Flask, flask_login, flask_sqlalchemy, bootstrap, github
