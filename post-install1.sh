#!/bin/bash

echo "UBUNTU POST-INSTALL SCRIPT"

echo "Updating APT..."

sudo apt-get update 

clear

echo "Installing base packages"

sudo apt-get install --yes git git-extras build-essential python3-pip htop glances

clear

sudo snap install discord
echo "Installation de discord"
clear

sudo snap install --classic code
echo "Installation de vscode"

