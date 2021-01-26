import os
#!/bin/bash

print("INSTALLATION DU SCRIPT POST-INSTALL D'UBUNTU")

print("Lancement des maj")

os.system("sudo apt-get update ")

os.system("clear")

print("Installation des paquets de base ")

os.system("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances")

os.system("clear")

print("Installation de discord")

os.system("sudo snap install discord")

os.system("clear")

print("Installation de Vscode")

os.system("sudo snap install --classic code")


