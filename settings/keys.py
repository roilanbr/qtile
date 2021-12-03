# Qtile keybindings

import os
import subprocess

from libqtile.config import Key
from libqtile.command import lazy

homeUser = os.path.expanduser('~')
qtilePath = os.path.join(homeUser, ".config", "qtile")

mod = "mod4"

keys = [
    # Moverse entre ventanas
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Mover la ventana activa a otra posición
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    
    # Cambiar tamaño de la ventana activa
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    
    # Lanzar terminal
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Alternar entre diferentes diseños como se define a continuación
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Cerrar ventana activa (original es "w") 
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Mis atajos de teclado
    Key([mod], "F1", lazy.spawn("alacritty -t Ayuda -e " + qtilePath + "/scripts/help.sh"), desc="Ayuda atajos de teclado"),
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Lanzardor"),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Explorador"),
    Key([mod], "F2", lazy.spawn("rofi -show run"), desc="Ejecutar"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Cambiar entre ventana flotante/no-flotante"),
    #Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
]

# mod = "mod4"

# keys = [Key(key[0], key[1], *key[2:]) for key in [
#     # ------------ Window Configs ------------

#     # Switch between windows in current stack pane
#     ([mod], "j", lazy.layout.down()),
#     ([mod], "k", lazy.layout.up()),
#     ([mod], "h", lazy.layout.left()),
#     ([mod], "l", lazy.layout.right()),

#     # Change window sizes (MonadTall)
#     ([mod, "shift"], "l", lazy.layout.grow()),
#     ([mod, "shift"], "h", lazy.layout.shrink()),

#     # Toggle floating
#     ([mod, "shift"], "f", lazy.window.toggle_floating()),

#     # Move windows up or down in current stack
#     ([mod, "shift"], "j", lazy.layout.shuffle_down()),
#     ([mod, "shift"], "k", lazy.layout.shuffle_up()),

#     # Toggle between different layouts as defined below
#     ([mod], "Tab", lazy.next_layout()),
#     ([mod, "shift"], "Tab", lazy.prev_layout()),

#     # Kill window
#     ([mod], "w", lazy.window.kill()),

#     # Switch focus of monitors
#     ([mod], "period", lazy.next_screen()),
#     ([mod], "comma", lazy.prev_screen()),

#     # Restart Qtile
#     ([mod, "control"], "r", lazy.restart()),

#     ([mod, "control"], "q", lazy.shutdown()),
#     ([mod], "r", lazy.spawncmd()),

#     # ------------ App Configs ------------

#     # Menu
#     ([mod], "m", lazy.spawn("rofi -show drun")),

#     # Window Nav
#     ([mod, "shift"], "m", lazy.spawn("rofi -show")),

#     # Browser
#     ([mod], "b", lazy.spawn("firefox")),

#     # File Explorer
#     ([mod], "e", lazy.spawn("pcmanfm")),

#     # Terminal
#     ([mod], "Return", lazy.spawn("alacritty")),

#     # Redshift
#     ([mod], "r", lazy.spawn("redshift -O 2400")),
#     ([mod, "shift"], "r", lazy.spawn("redshift -x")),

#     # Screenshot
#     ([mod], "s", lazy.spawn("scrot")),
#     ([mod, "shift"], "s", lazy.spawn("scrot -s")),

#     # ------------ Hardware Configs ------------

#     # Volume
#     ([], "XF86AudioLowerVolume", lazy.spawn(
#         "pactl set-sink-volume @DEFAULT_SINK@ -5%"
#     )),
#     ([], "XF86AudioRaiseVolume", lazy.spawn(
#         "pactl set-sink-volume @DEFAULT_SINK@ +5%"
#     )),
#     ([], "XF86AudioMute", lazy.spawn(
#         "pactl set-sink-mute @DEFAULT_SINK@ toggle"
#     )),

#     # Brightness
#     ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
#     ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
# ]]
