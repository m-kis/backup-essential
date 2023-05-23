# backup-essential
Ce script permet d'effectuer des opérations de sauvegarde des fichiers, la sauvegarde des bases de données MySQL et MongoDB, la sauvegarde des fichiers journaux, la mise à jour des packages et le nettoyage des fichiers journaux.

Usage :

Assurez-vous d'avoir les privilèges requis pour exécuter les commandes système sur le serveur.
Assurez-vous d'avoir les paquets mysql-client, mongodb-tools et tar installés sur le serveur.
Exécutez le script à l'aide de la commande suivante : python maintenance_server.py
Suivez les instructions affichées pour fournir les informations nécessaires.
Note : Le script effectuera les opérations suivantes :

Sauvegarde des fichiers sur le serveur.
Sauvegarde de la base de données MySQL spécifiée.
Sauvegarde de la base de données MongoDB spécifiée.
Sauvegarde des fichiers journaux sur le serveur.
Mise à jour des packages du serveur.
Nettoyage des fichiers journaux du serveur.
Assurez-vous d'avoir suffisamment d'espace de stockage disponible dans le répertoire de destination pour les sauvegardes.

README :

Script de maintenance du serveur
Ce script permet d'effectuer des opérations de maintenance courantes sur un serveur, telles que la sauvegarde des fichiers, la sauvegarde des bases de données MySQL et MongoDB, la sauvegarde des fichiers journaux, la mise à jour des packages et le nettoyage des fichiers journaux.

Prérequis
Les privilèges requis pour exécuter des commandes système sur le serveur.
Les paquets mysql-client, mongodb-tools et tar installés sur le serveur.
Utilisation
Clonez ce dépôt ou copiez le contenu du script maintenance_server.py dans un fichier local.
Exécutez le script à l'aide de la commande suivante : python maintenance_server.py
Suivez les instructions affichées pour fournir les informations suivantes :
Adresse IP ou nom du serveur.
Chemin de destination des sauvegardes.
Nom de la base de données MySQL à sauvegarder.
Nom de la base de données MongoDB à sauvegarder.
Assurez-vous d'avoir suffisamment d'espace de stockage disponible dans le répertoire de destination pour les sauvegardes.

Le script effectuera les opérations de sauvegarde et de maintenance spécifiées, puis affichera un message de confirmation une fois terminé.

Auteur
Ce script a été développé par M-KIS.

N'hésitez pas à personnaliser le script en fonction de vos besoins spécifiques, par exemple en ajoutant des opérations supplémentaires ou en adaptant les commandes de sauvegarde aux spécificités de votre environnement.

Assurez-vous de comprendre les implications de chaque opération avant de l'exécuter sur votre serveur.
