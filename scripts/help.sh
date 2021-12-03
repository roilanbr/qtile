#!/usr/bin/bash

# Obtener ruta al script
dirScripts=$(readlink -f $0)
dirScripts=$(dirname $dirScripts)

source $dirScripts/color # Colores en los textos

echo $underlined$yellow"Atajos de teclado personalizado:"$resetAll && echo

echo "Esta ayuda: ${green} Super + F1 $resetAll"
echo "Ejecutar  : ${green} Super + F2 $resetAll"
echo "Lanzador  : ${green} Super + m  $resetAll"
echo "Explorador: ${green} Super + e  $resetAll"
echo
echo "Ventana flotante: ${green} Super + f  $resetAll"

echo
read -rsp $'Presione una tecla para salir...\n' -n 1