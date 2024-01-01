#!/bin/bash

figlet "Banana App Store"

json_file="/tmp/banana_app_store_list.json"
curl -o "$json_file" http://mirror.thebananastore.xyz/list.json

if [ ! -f "$json_file" ]; then
    echo "Error: Local JSON file '$json_file' not found."
    exit 1
fi

app_names=($(jq -r '.apps[].name' "$json_file"))

selected_app=$(yad --list --title="Banana App Store" --column="Apps" "${app_names[@]}" \
                    --height=300 --button="Install" --button="Cancel" --separator=$'\n')

if [ "$?" -eq 252 ] || [ -z "$selected_app" ]; then
    exit 0
fi

selected_installer_url=$(jq -r --arg selected_app "$selected_app" '.apps[] | select(.name == $selected_app) | .installer' "$json_file")
install_script="/tmp/install_script.sh"
wget -O "$install_script" "$selected_installer_url"
chmod +x "$install_script" && "$install_script"

exit 0
