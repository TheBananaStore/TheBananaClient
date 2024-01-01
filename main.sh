#!/bin/bash

figlet "Banana App Store"
json_file="$HOME/Banana/apps/list.json"

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


selected_installer=$(jq -r --arg selected_app "$selected_app" '.apps[] | select(.name == $selected_app) | .installer' "$json_file")


chmod +x "$selected_installer" && "$selected_installer"

exit 0
