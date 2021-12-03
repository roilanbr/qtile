def fcThemeColor(variante):
    global colorBg, colorCl, colorComment, colorFg
    global colorRed, colorOrange, colorYellow, colorGreen
    global colorCyan, colorPurple, colorPink

    if variante == "high":             #Tema fuerte
        colorBg =      "#282a36" # Background
        colorCl =      "#44475a" # Current Line
        colorComment = "#6272a4" # Comment
        colorFg =      "#ffffff" # Foreground
        colorRed =     "#ff0000"  # Red
        colorOrange =  "#ff8000"  # Orange
        colorYellow =  "#ffff00"  # Yellow
        colorGreen =   "#00ff00"  # Green
        colorCyan =    "#00ffff"  # Cyan
        colorPurple =  "#8000ff"  # Purple
        colorPink =    "#ff0080"  # Pink

    elif variante == "half":       # Tema medio
        colorBg =      "#21222c" # Background
        colorCl =      "#414558" # Current Line
        colorComment = "#a7abbe" # Comment
        colorFg =      "#f8f8f2" # Foreground
        colorRed =     "#ff4040" # Red
        colorOrange =  "#ff9f40" # Orange
        colorYellow =  "#ffff40" # Yellow
        colorGreen =   "#40ff40" # Green
        colorCyan =    "#40ffff" # Cyan
        colorPurple =  "#9f40ff" # Purple
        colorPink =    "#ff409f" # Pink

    elif variante == "light":      # Tema ligero
        colorBg =      "#21222c" # Background
        colorCl =      "#414558" # Current Line
        colorComment = "#a7abbe" # Comment
        colorFg =      "#f2f2f2" # Foreground
        colorRed =     "#ff8080" # Red
        colorOrange =  "#ffbf80" # Orange
        colorYellow =  "#ffff80" # Yellow
        colorGreen =   "#80ff80" # Green
        colorCyan =    "#80ffff" # Cyan
        colorPurple =  "#bf80ff" # Purple
        colorPink =    "#ff80bf" # Pink

    elif variante == "low":        # Tema claro
        colorBg =      "#21222c" # Background
        colorCl =      "#414558" # Current Line
        colorComment = "#a7abbe" # Comment
        colorFg =      "#f8f8f2" # Foreground
        colorRed =     "#ffbfbf" # Red
        colorOrange =  "#ffdfbf" # Orange
        colorYellow =  "#ffffbf" # Yellow
        colorGreen =   "#bfffbf" # Green
        colorCyan =    "#bfffff" # Cyan
        colorPurple =  "#dfbfff" # Purple
        colorPink =    "#ffbfdf" # Pink

    return [
        colorBg, colorCl, colorComment, colorFg, 
        colorRed, colorOrange, colorYellow, colorGreen, 
        colorCyan, colorPurple, colorPink
    ]

# Rueda Hue/HSV
#100% #ff0000 #ff8000  #ffff00 #80ff00 #00ff00 #00ff80 #00ffff #0080ff #0000ff #8000ff #ff00ff #ff0080
#75%  #ff4040 #ff9f40  #ffff40 #9fff40 #40ff40 #40ff9f #40ffff #409fff #4040ff #9f40ff #ff40ff #ff409f
#60%  #ff5555 #ffb86c  #f1fa8c #000000 #50fa7b #000000 #8be9fd #000000 #000000 #bd93f9 #000000 #ff79c6
#50%  #ff8080 #ffbf80  #ffff80 #bfff80 #80ff80 #80ffbf #80ffff #80bfff #8080ff #bf80ff #ff80ff #ff80bf
#25%  #ffbfbf #ffdfbf  #ffffbf #dfffbf #bfffbf #bfffdf #bfffff #bfdfff #bfbfff #dfbfff #ffbfff #ffbfdf

# Tema Dracula original
# colorBg =      "#282a36"  # Background
# colorFg =      "#f8f8f2"  # Foreground
# colorCl =      "#44475a"  # Current Line
# colorComment = "#6272a4"  # Comment
# colorCyan =    "#8be9fd"  # Cyan
# colorGreen =   "#50fa7b"  # Green
# colorYellow =  "#f1fa8c"  # Yellow
# colorOrange =  "#ffb86c"  # Orange
# colorRed =     "#ff5555"  # Red
# colorPink =    "#ff79c6"  # Pink
# colorPurple =  "#bd93f9"  # Purple