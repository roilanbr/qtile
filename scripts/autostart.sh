#!/bin/sh

# systray
udiskie -t -n &   # Extraer Unidades
#volumeicon &      # Volumen
nm-applet &       # Red
#cbatticon -u 10 & # Batería

# Wallpaper
feh -z --bg-fill ~/.config/qtile/bg.jpg 
# App
# alacritty & # Terminal
picom --no-vsync & # Transparencias y efectos (--no-vsync es para VM)
