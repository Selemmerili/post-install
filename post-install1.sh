#!/bin/bash

echo "UBUNTU POST-INSTALL SCRIPT"

echo "Updating APT..."
#Commande pour installer les maj
sudo apt-get update 

clear

echo "Installing base packages"
#commande permettant d'installer python
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances

clear
#commande qui installe discord via snap
sudo snap install discord
echo "Installation de discord"
clear

#Installation de vscode via snap
sudo snap install --classic code
echo "Installation de vscode"

