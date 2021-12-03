# Para localizar las configuraciones buscar "MIS", los que e creado:
# MIS MÓDULOS IMPORTADOS
# MIS VARIABLES
# MIS ATAJOS DE TECLADO
# MIS VENTANAS FLOTANTES
# MIS PROGRAMAS QUE AUTOINICIO

# Para los iconos necesita instalar Nerd Fonts
# pacman -S ttf-nerd-fonts-symbols ttf-nerd-fonts-símbolos-mono
# wget https://github.com/ryanoasis/nerd-fonts/archive/v2.1.0.tar.gz

# MÓDULOS IMPORTADOS ----------------------------
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# MIS MÓDULOS IMPORTADOS ========================
import os
import subprocess
from libqtile import qtile, hook
import mywidget     # Widget personalizado


mod = "mod4"
terminal = "alacritty"

# MIS VARIABLES =================================
homeUser = os.path.expanduser('~')
qtilePath = os.path.join(homeUser, ".config", "qtile")

#groups = [ Group(i) for i in ["1", "2", "3", "4"]]
groups = [ Group(i) for i in ["", "", "", ""]]

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
sizeFont = 12 # Tamaño de los texto
sizeBar = 24  # Ancho de la barra(24), coge la altura de la letra si es mayor

# MIS FUNCIONES =================================
# Función para mostrar separador formateado
def fcSeparator():
    return widget.Sep(
        background = colorYellow, # Color del fondo del widget
        foreground = colorRed, # Color del fondo del separador
        linewidth = 5, # Ancho del separador.
        padding =2, # Ancho de los bordes del separador
    )

# Función para dibujar punta formateada en los widget : color/0(izquierda)/1(derecha)
def fcPuntasWidget(colorBgIcon, colorIcon, tipoIcon):
    if tipoIcon == 0:   # Si es 0
        icono = ""  #  nf-fa-caret_left
    else:           # Si es 1
        icono = ""  #  nf-fa-caret_right
    return widget.TextBox(
        text = icono,           # Icono a mostrar
        font = fontSymbols,
        fontsize = sizeBar + 5, # +5 para que ocupe el ancho de la barra
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

# ATAJOS DE TECLADO -----------------------------
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

    # MIS ATAJOS DE TECLADO =====================
    Key([mod], "F1", lazy.spawn("alacritty -t Ayuda -e " + qtilePath + "/scripts/help.sh"), desc="Ayuda atajos de teclado"),
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Lanzardor"),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Explorador"),
    Key([mod], "F2", lazy.spawn("rofi -show run"), desc="Ejecutar"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Cambiar entre ventana flotante/no-flotante"),
]


for i, group in enumerate(groups):
    desktopNumber = str(i+1) # Enumerar los escritorios
    keys.extend([
        Key([mod], desktopNumber, lazy.group[group.name].toscreen(), desc="Switch to group {}".format(group.name)),
        Key([mod, "shift"], desktopNumber, lazy.window.togroup(group.name, switch_group=True), desc="Switch to & move focused window to group {}".format(group.name)),
    ])

# DISEÑO DE VENTANAS - LAYOUTS
layouts = [
    layout.Columns(
        border_normal=colorCl,
        border_focus=colorRed,
        border_width=2),
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
    # PANTALLA 1 INICIO -------------------------
    Screen(
        #left=bar.Bar( [ funcSep(), ], 20, ), 
        #right=bar.Bar( [ funcSep(), ], 20, ),

        # BARRA SUPERIOR ========================
        top=bar.Bar(
            [
                # WIDGET GRUPO 1 ================
                widget.TextBox("", foreground=colorGreen),
                widget.Prompt( prompt="Run: "),
                widget.Spacer(length = 50), # Para mover los widget a los extremos
                widget.WindowName(foreground=colorPurple, max_chars=20),
                widget.Spacer(), # Para mover los widget a los extremos
                # Velocidad de la red
                widget.Net(background = colorBg, foreground = colorYellow,
                    format = '{down}↓↑{up}', #  nf-oct-dashboard
                    fontsize = sizeBar-10,
                ),

                # WIDGET GRUPO 2 ================
                # Temperatura
                fcPuntasWidget(colorBg, colorOrange, 0),
                widget.ThermalSensor(
                     foreground = colorBg,   # Color fondo
                     background = colorOrange,       # Color texto
                     foreground_alert = colorRed,# Color texto alerta
                     fontsize = sizeBar - 10,
                     tag_sensor = "Temp1",
                     fmt = "  T1:{} ", #  nf-weather-thermometer
                     padding = 0,
                 ),
                widget.ThermalSensor( foreground = colorBg, background = colorOrange, foreground_alert = colorRed,
                     tag_sensor = "Temp1",
                     fmt = " T2:{}",
                     padding = 0,
                 ),
                                
                # Información de la Ram y CPU
                fcPuntasWidget(colorOrange, colorRed, 0),
                widget.Memory(
                    fontsize=sizeBar-10, background = colorRed,foreground = colorBg,foreground_alert = colorRed,
                    format = "||{MemUsed: .0f}{mm} {MemPercent:.0f}% | free:{MemFree: .0f}{mm}", #  nf-fa-ellipsis_v
                ),
                #widget.TextBox("Free:", background=ColorRed, foreground=ColorFg),
                
                widget.Sep(foreground=colorBg, padding =0),
                widget.CPUGraph(
                    background = colorRed,
                    border_color = colorBg,
                    graph_color = colorBg,
                    fill_color = colorYellow,
                    width= 30 ,
                    border_width = 1,
                    line_width = 3,
                    frequency = 5,
                    samples = 50,
                 ),

                # Actualización, Cerrar sesión y Apagar
                fcPuntasWidget(colorRed, colorBg, 0),
                widget.CheckUpdates(
                    background= colorBg,
                    colour_have_updates = colorRed,
                    colour_no_updates = colorGreen,
                    fontsize = sizeBar - 5,
                    display_format = "{updates}",
                    no_update_string = "", #  nf-mdi-autorenew
                    distro = "Arch",
                    mouse_callbacks = {"Button2": lambda: qtile.cmd_spawn("pavucontrol")},
                    update_interval = 1800 # Comprobar act cada 1h
                ),
                widget.QuickExit(
                    background = colorBg,
                    foreground=colorYellow,
                    default_text = '', #  nf-oct-sign_out
                    fontsize = sizeBar - 5,
                    countdown_format = '[{}]'
                ),
                mywidget.PowerOff( # Opciones igual a "QuickExit"
                    background = colorBg,
                    foreground=colorRed,
                    default_text = '', #  nf-fa-power_off
                    fontsize = sizeBar - 50,
                    countdown_start = 8,    # Tiempo de espera(5)
                    countdown_format = '[{}]'
                ),
            ],
            sizeBar, # Ancho de la barra
            background = colorBg, # Color de fondo de la barra
        ),

        # BARRA INFERIOR ========================
        bottom=bar.Bar(
            [
                # WIDGET GRUPO 1 ================
                # Icono Layouts, Escritorios (grupos), Contador de ventanas abiertas y lista de vetanas
                widget.CurrentLayoutIcon(scale=1, background = colorBg),
                widget.GroupBox(
                    background = colorRed,
                    fontsize = sizeBar, # Tamaño de la fuente
                    active = colorYellow, # Color fuente de grupos activos
                    inactive = colorBg, # Color de fuente de grupo no activo
                    block_highlight_text_color = colorYellow, # Color de fuente del grupo seleccionado
                    highlight_method = "block", # Resaltado del grupo seleccionado (border)
                    this_current_screen_border = colorBg, # Color block del grupo seleccionado (#215578)
                    urgent_alert_method = "line", # Alerta notificaciones urgentes de WM (border)
                    urgent_border = colorYellow, # Color notificaciones urgente
                    urgent_text = colorYellow, # Color notificaciones urgente
                ),
                widget.WindowCount(background = colorRed, foreground = colorBg),
                fcPuntasWidget(colorBg, colorRed, 1), # Punta
                widget.TaskList(border=colorPurple, max_title_width=125),
                
                # WIDGET GRUPO 2 ================
                # Bandeja del sistema,
                fcPuntasWidget(colorBg, colorRed, 0), # Punta
                widget.Systray(background = colorRed),

                # WIDGET GRUPO 3 ================
                # Icon Volumen, Fecha y hora y Notificaciónes
                # fcPuntasWidget(colorBg, colorRed, 0), # Punta
                widget.Volume(
                    background=colorRed, foreground=colorBg, fontsize=sizeBar-10, update_interval=0.2, 
                    fmt = " {}",
                    mouse_callbacks = {"Button3": lambda: qtile.cmd_spawn("pavucontrol")}
                ),
                # widget.Sep(foreground=colorFg, padding =0),
                fcPuntasWidget(colorRed, colorBg, 0), # Punta
                widget.Clock(foreground=colorYellow, format="%I:%M", fontsize=sizeBar - 12),
                widget.Clock(foreground=colorFg, format="%d/%m/%Y", fontsize=sizeBar - 12),
                widget.Notify(),
            ],
            sizeBar,
            background = colorBg,
            #border_width = 10,
            #border_color = colorRed,
            #opacity = 80,
        ),
    ), # PANTALLA 1 FIN =========================
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

    # MIS VENTANAS FLOTANTES ====================
    Match(wm_class='Alacritty', title='Ayuda'), # Ayuda atajos de teclado
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Para los programas que se autominimizarse cuando pierden el foco.
auto_minimize = True

# Por si da problema en java, ventana en blanca o gris.
wmname = "LG3D"

# MIS PROGRAMAS QUE AUTOINICIAN =================
@hook.subscribe.startup_once
def autostart():
    subprocess.call([qtilePath + '/scripts/autostart.sh'])
