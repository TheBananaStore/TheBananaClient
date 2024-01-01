#!/bin/bash

# Uninstaller script for Banana App Store

# Define installation directory
INSTALL_DIR="$HOME/Banana"

# Remove Banana App Store directory and its contents
rm -rf "$INSTALL_DIR"
echo "Banana App Store removed."

# Remove desktop shortcut
rm -f "$HOME/Desktop/banana.desktop"
echo "Desktop shortcut removed."

# Remove menu entry
sudo rm -f "/usr/local/share/applications/banana.desktop"
echo "Menu entry removed."

echo "Banana App Store is uninstalled!"
