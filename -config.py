
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal
from libqtile import hook

# Mis módulos
import os
import subprocess
from settings.keys import mod, keys


#terminal = guess_terminal()

# Grupo de escritorios
groups = [Group(i) for i in "123456789"]
#groups = [ Group(i) for i in [
#        "Uno", "Dos", "Tres", "Cuatro",
#    ]
#]

# Mis variables
homeUser = os.path.expanduser('~')
qtilePath = os.path.join(homeUser, ".config", "qtile")

colorBg =      "#282a36" # Background
colorCl =      "#44475a" # Current Line
colorFg =      "#f8f8f2" # Foreground
colorComment = "#6272a4" # Comment
colorCyan =    "#8be9fd" # Cyan
colorGreen =   "#50fa7b" # Green
colorOrange =  "#ffb86c" # Orange
colorPink =    "#ff79c6" # Pink
colorPurple =  "#bd93f9" # Purple
colorRed =     "#ff5555" # Red
colorYellow =  "#f1fa8c" # Yellow

# Programas que autoinician
@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([homeUser + '/.config/qtile/scripts/autostart.sh'])

for i, group in enumerate(groups):
    #desktopNumber = str (i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(  # Cambiar posición del panel: top(arriba)/bottom(abajo)
            [
                widget.CurrentLayout(), # Diseño de los Layouts: Columns/Max/Matrix/MonadTall etc.
                widget.GroupBox(), # Los Escritorios: 123456789
                widget.Prompt(),
                widget.WindowName(), # Nombre de la ventana activa
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(), # Bandeja del sistema
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'), # Reloj 
                widget.QuickExit(), # Cerrar sesión 
            ],
            24, # Altura del panel
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    
    # Mis ventanas flotantes
    Match(wm_class='Alacritty', title='Ayuda'), # Ayuda atajos de teclado
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
