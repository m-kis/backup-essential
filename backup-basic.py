# Maintenance du serveur
# Auteur: M-KIS

import datetime
import subprocess

def backup_files(server, destination):
    # Code pour effectuer la sauvegarde des fichiers sur le serveur
    pass

def backup_mysql(server, database, destination):
    # Code pour effectuer la sauvegarde de la base de données MySQL sur le serveur
    backup_cmd = f"mysqldump --user=username --password=password {database} > {destination}/backup_database_{database}.sql"
    subprocess.run(backup_cmd, shell=True)

def backup_mongodb(server, database, destination):
    # Code pour effectuer la sauvegarde de la base de données MongoDB sur le serveur
    backup_cmd = f"mongodump --host {server} --db {database} --out {destination}/backup_database_{database}"
    subprocess.run(backup_cmd, shell=True)

def backup_logs(server, destination):
    # Code pour effectuer la sauvegarde des fichiers journaux sur le serveur
    backup_cmd = f"cp /var/log/* {destination}/logs_backup/"
    subprocess.run(backup_cmd, shell=True)

def update_packages(server):
    # Code pour mettre à jour les packages du serveur
    update_cmd = "apt-get update && apt-get upgrade -y"
    subprocess.run(update_cmd, shell=True)

def clean_logs(server):
    # Code pour nettoyer les fichiers journaux du serveur
    clean_cmd = "rm -rf /var/log/*"
    subprocess.run(clean_cmd, shell=True)

# Définir la date actuelle pour le nom du fichier de sauvegarde
date = datetime.datetime.now().strftime("%Y-%m-%d")

# Demander les informations du serveur à l'utilisateur
server = input("Veuillez entrer l'adresse IP ou le nom du serveur : ")
destination = input("Veuillez entrer le chemin de destination des sauvegardes : ")

# Effectuer la sauvegarde des fichiers
backup_files(server, f"{destination}/backup_files_{date}.tar.gz")

# Effectuer la sauvegarde de la base de données MySQL
mysql_database = input("Veuillez entrer le nom de la base de données MySQL : ")
backup_mysql(server, mysql_database, f"{destination}/backup_database_{mysql_database}_{date}.sql")

# Effectuer la sauvegarde de la base de données MongoDB
mongodb_database = input("Veuillez entrer le nom de la base de données MongoDB : ")
backup_mongodb(server, mongodb_database, f"{destination}/backup_database_{mongodb_database}_{date}")

# Effectuer la sauvegarde des fichiers journaux
backup_logs(server, f"{destination}/backup_logs_{date}.tar.gz")

# Mettre à jour les packages du serveur
update_packages(server)

# Nettoyer les fichiers journaux du serveur
clean_logs(server)

# Afficher un message de confirmation
print("Les opérations de maintenance ont été effectuées avec succès.")
