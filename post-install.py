import os
#!/bin/bash

print("INSTALLATION DU SCRIPT POST-INSTALL D'UBUNTU")

print("Lancement des maj")
#Lancement de la commande qui lance les maj
os.system("sudo apt-get update ")
#La commande clear efface les étapes précédentes 
os.system("clear")

print("Installation des paquets de base ")
#Installation des modules pour Python
os.system("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances")

os.system("clear")

print("Installation de discord")
#Installation de discord via snap
os.system("sudo snap install discord")

os.system("clear")

print("Installation de Vscode")
#Installation de Vscode via snap
os.system("sudo snap install --classic code")


