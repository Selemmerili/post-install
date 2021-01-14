import os
#!/bin/bash

print("UBUNTU POST-INSTALL SCRIPT")

print("Updating APT...")

os.system("sudo apt-get update ")

os.system("clear")

print("Installing base packages")

os.system("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances")

os.system("clear")

os.system("sudo snap install discord")

os.system("clear")

os.system("sudo snap install --classic code")


