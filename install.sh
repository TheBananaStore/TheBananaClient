#!/bin/bash

sudo apt update 
sudo apt install figlet wget yad jq git lxterminal -y

git clone https://github.com/BananaAppStore/BananaAppStore.git ~/Banana

mv ~/Banana/desktopconf.desktop ~/Desktop/banana.desktop
echo "Desktop shortcut entry created."
sudo mv ~/Banana/menuconf.desktop /usr/local/share/applications/banana.desktop 
echo "Menu entry made."

chmod 777 ~/Banana/main.sh



echo "Banana App Store is installed!"
echo "https://github.com/BananaAppStore"
