# Para localizar las configuraciones buscar "Mis", los que e creado:
# Mis módulos importados
# Mis variables
# Mis atajos de teclado
# Mis ventanas flotantes
# Mis programas que autoinician

# Para los simbolos en los grupos necesita instalar Nerd Fonts
# pacman -S ttf-nerd-fonts-symbols ttf-nerd-fonts-símbolos-mono
# wget https://github.com/ryanoasis/nerd-fonts/archive/v2.1.0.tar.gz

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Mis módulos importados
import os
import subprocess
from libqtile import qtile, hook
import mywidget     # Mis widget personalizado



mod = "mod4"
terminal = "alacritty"

# Mis variables
homeUser = os.path.expanduser('~')
qtilePath = os.path.join(homeUser, ".config", "qtile")

#groups = [ Group(i) for i in ["1", "2", "3", "4"]]
groups = [ Group(i) for i in ["", "", "", ""]]

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

fontSymbols = "Symbols Nerd Font"
colorFont = colorFg
sizeFont = 12 # Tamaño de los texto
sizeBar = 24  # Ancho de la barra(24), coge la altura de la letra si es mayor

# Mis funciones
# Función para mostrar separador formateado
def fcSeparator():
    return widget.Sep(
        background = colorYellow, # Color del fondo del widget
        foreground = colorRed, # Color del fondo del separador
        linewidth = 5, # Ancho del separador.
        padding =2, # Ancho de los bordes del separador
    )

# Función para dibujar punta formateada: color/0(izquierda)/1(derecha)
def fcPuntasWidget(colorBgIcon, colorIcon, tipoIcon):
    if tipoIcon == 0:   # Si es 0
        icono = ""  # ◥ nf-weather-moon_third_quarter
    else:           # Si es 1
        icono = ""  # ◣ nf-weather-moon_first_quarter
    return widget.TextBox(
        text = icono,           # Icono a mostrar
        font = fontSymbols,
        fontsize = sizeBar + 7, # +5 para que ocupe el ancho de la barra
        background = colorBgIcon,   # fondo texto
        foreground = colorIcon, # Color texto
        padding = -0.9, # Ancho de los bordes del separador
        )

# Función para mostrar icono formateado: icono/fondo/color
def fcIcon(tipoIcon, colorIconBg, colorIconFg):
    return widget.TextBox(
        text = tipoIcon,
        font = fontSymbols,
        background = colorIconBg,
        foreground = colorIconFg,
        fontsize = sizeBar - 5,
        #padding = 0
    )

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    #Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),  # Terminal a lanzar
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),  # Terminal a lanzar
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
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
]


for i, group in enumerate(groups):
    desktopNumber = str(i+1) # Enumerar los escritorios
    keys.extend([
        # mod1 + letter of group = switch to group
        #Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key([mod], desktopNumber, lazy.group[group.name].toscreen(), desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
        Key([mod, "shift"], desktopNumber, lazy.window.togroup(group.name, switch_group=True), desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        #border_width=2,
        border_normal=colorCl,
        border_focus=colorRed,
        border_width=2,
    ),
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
    font='Ubuntu',
    fontsize=sizeFont,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        #left=bar.Bar( [ funcSep(), ], 20, ), 
        #right=bar.Bar( [ funcSep(), ], 20, ),

        # Barra superior
        top=bar.Bar(
            [


                widget.TextBox("", background= colorBg, fontsize=sizeBar-5),
                widget.CheckUpdates(
                    background= colorBg,
                    foreground = colorRed,
                    colour_have_updates = colorGreen,
                    colour_no_updates = colorYellow,
                    display_format = ': {updates}', #  nf-fa-refresh
                    distro = "Arch",
                    fontsize = sizeBar - 5,
                ),
                 widget.TextBox("Equipo", background= colorBg, foreground=colorFg),
                 fcPuntasWidget(colorRed, colorBg, 1),
                 
                 widget.TextBox("Home", background=colorRed, foreground=colorBg),
                 fcPuntasWidget([colorBg, colorCl], colorRed, 1),

                widget.Spacer(), # Para mover los widget a los extremos
                widget.WindowName(foreground=colorPurple),
                widget.Spacer(), # Para mover los widget a los extremos
                widget.Notify(),
                # widget.Prompt(
                #      prompt="run: ",
                # ),
                # fcSeparator(),

                # # Módulo Sensores
                 #fcPuntasWidget("", colorOrange, 0),
                # fcIcon("龍", colorOrange, colorBg),# nf-mdi-speedometer
                # widget.Net(background = colorOrange, foreground = colorBg,
                #     format = '龍Net: {down} ↓↑ {up}'
                # ),
                # fcIcon("", colorOrange, colorBg,), #  nf-mdi-memory
                # widget.CPU(background = colorOrange, foreground = colorBg, 
                #     format = 'Cpu: {load_percent}%',),
                # fcIcon("", colorOrange, colorBg),#  nf-fa-microchip
                # widget.Memory( background = colorOrange,foreground = colorBg,foreground_alert = colorRed,
                #     format = "Ram: {MemUsed: .0f}{mm} -{MemPercent:.0f}%/ free: {MemFree: .0f}{mm}",
                # ),
                # fcPuntasWidget(colorOrange, 1),

                
                # Módulo información CPU/RAM/NET
                # Temperatura
                #fcSeparator(),                
                fcPuntasWidget("", colorOrange, 0),
                fcIcon("", colorOrange, colorBg), #  nf-fa-thermometer_2
                widget.ThermalSensor(
                     foreground = colorBg,   # Color fondo
                     background = colorOrange,       # Color texto
                     foreground_alert = colorRed,# Color texto alerta
                     tag_sensor = "Temp1",
                     fmt = "T1:{}",
                     padding = 0,
                 ),
                widget.ThermalSensor( foreground = colorBg, background = colorOrange, foreground_alert = colorRed,
                     tag_sensor = "Temp1",
                     fmt = "T2:{}",
                     padding = 0,
                 ),
                                
                # Módulo CPU/RAM/NET en Gráficos
                fcPuntasWidget(colorOrange, colorPurple, 0),
                widget.TextBox("Cpu", background=colorPurple, foreground=colorBg, fontsize = 10, padding=0), #  nf-fa-microchip
                widget.CPUGraph(
                    background = colorPurple,
                    foreground=colorBg,
                    width=20,
                    border_width=1,
                    border_color = colorBg,
                    frequency=5,
                    line_width=1,
                    samples=50,
                 ),

                widget.TextBox("Ram", background = colorPurple, foreground=colorBg, fontsize = 10, padding=0), #  nf-fa-microchip
                widget.MemoryGraph(
                    background = colorPurple,
                    foreground=colorBg,
                    width=20,
                    border_width=1,
                    border_color = colorBg, 
                    line_width=1,
                    frequency=5,
                    fill_color="EEE8AA",
                 ),
                widget.TextBox("Net", background = colorPurple, foreground=colorBg, fontsize = 10, padding=0), #  nf-fa-microchip
                widget.NetGraph(
                    background = colorPurple, 
                    foreground=colorBg, 
                    border_width=1,
                    width=20, 
                    line_width=1,
                    border_color=colorBg ),

                fcPuntasWidget(colorPurple, colorBg, 0),
                #widget.TextBox(" 婢   墳 ", fontsize=18), # 婢   墳 
                widget.Volume(
                    background = colorBg, fontsize=10, update_interval=0.2,
                    mouse_callbacks = {"Button3": lambda: qtile.cmd_spawn("pavucontrol")}),
                
                # widget.TextBox( "", #  nf-fa-power_off
                #     background = colorBg,
                #     foreground = colorRed,
                #     fontsize = sizeBar - 5,
                #     #mouse_callbacks = lazy.spawn("pcmanfm"),
                #     mouse_callbacks = {
                #         "Button2": powerOff,
                #     },
                # ),
                
                # BOTÓN APAGAR Y CERRAR SESION
                mywidget.PowerOff( 
                    background = colorBg,
                    foreground=colorRed,
                    default_text = '', #  nf-fa-power_off
                    fontsize = sizeBar - 50,
                    countdown_start = 10,    # Tiempo de espera(5)
                    countdown_format = '{}'),
                widget.QuickExit(
                    background = colorBg,
                    foreground=colorOrange,
                    default_text = '  ', #  nf-oct-key
                    fontsize = sizeBar - 5,
                    countdown_format = ' {} '),
            ],
            sizeBar,
            background = [colorBg, colorCl], # Color de fondo de la barra
        ),

        # Barra inferior
        bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.65),
                widget.WindowCount(),
                widget.GroupBox(
                    fontsize = 18, # Tamaño de la fuente
                    active = colorOrange, # Color fuente de grupos activos
                    inactive = colorComment, # Color de fuente de grupo no activo
                    block_highlight_text_color = colorFg, # Color de fuente del grupo seleccionado
                    highlight_method = "block", # Resaltado del grupo seleccionado (border)
                    this_current_screen_border = colorComment, # Color borde del grupo seleccionado (#215578)
                    urgent_alert_method = "line", # Alerta notificaciones urgentes de WM (border)
                    urgent_border = colorYellow, # Color notificaciones urgente
                    urgent_text = colorYellow, # Color notificaciones urgente
                ),
                fcSeparator(),
                widget.TaskList(),
                widget.Systray(),
                # widget.TextBox( "", #  nf-mdi-calendar_clock
                #     background = [colorCl, colorBg,],
                #     foreground = colorGreen,
                #     fontsize = sizeBar - 5,
                #     mouse_callbacks = {
                #         "Button2": powerOff,
                #     },
                # ),

                widget.Clock(foreground=colorGreen, format='%d/%m/%Y - %I:%M %p'),
            ],
            sizeBar,
            background = [ colorCl, colorBg, ] # Color de fondo de la barra con degradado
            #border_width = 10,
            #border_color = colorRed,
            #opacity = 80,
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

# Si programas quieren autominimizarse cuando pierden el foco.
auto_minimize = True

# Por si da problema en java, ventana en blanca o gris.
wmname = "LG3D"

# Mis programas que autoinician
@hook.subscribe.startup_once
def autostart():
    subprocess.call([qtilePath + '/scripts/autostart.sh'])
