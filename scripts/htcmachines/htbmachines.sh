#!/bin/bash

main_url="https://htbmachines.github.io/bundle.js"
#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

declare -r tmp_file="/dev/shm/tmp_file"
declare -r tmp_file2="/dev/shm/tmp_file2"
declare -r tmp_file3="/dev/shm/tmp_file3"

function ctrl_c() {
    echo -e "\n\n${redColour} [!] Saliendo...\n${endColour}"
    tput civis cnorm && exit 1
}
# Ctrl+C
trap ctrl_c INT



function helpPanel() {
    echo -e "\n${yellowColour}[+]${endColour} ${grayColour}Uso:${endColour}"
    echo -e "\t${purpleColour}h)${endColour} ${grayColour}Mostrar panel de ayuda${endColour}"
    echo -e "\t${purpleColour}i)${endColour} ${grayColour}Buscar por IP${endColour}"
    echo -e "\t${purpleColour}m)${endColour} ${grayColour}Buscar por nombre${endColour}"
    echo -e "\t${purpleColour}u)${endColour} ${grayColour}Actualizar datos base${endColour}"
    echo -e "\n"
}

function updateFiles() {
    tput civis
    if [ ! -f bundle.js ]; then
        # El archivo no existe
        echo -e "${yellowColour}[+]${endColour} ${grayColour}Descargando archivos necesarios...${endColour}\n"
        curl -s $main_url > bundle.js
        js-beautify bundle.js > _bundle.js
        mv _bundle.js bundle.js
        echo -e "${yellowColour}[+]${endColour} ${grayColour}Todos los archivos han sido descargados...${endColour}\n"
    else
        # El archivo existe
        echo -e "${yellowColour}[+]${endColour} ${grayColour}Comprobando si hay actualizaciones pendientes...${endColour}\n"
        sleep 2
        curl -s $main_url > bundle_temp.js
        js-beautify bundle_temp.js > _bundle_temp.js
        mv _bundle_temp.js bundle_temp.js

        md5_temp_value=$(md5sum bundle_temp.js | awk '{print $1}')
        md5_original_value=$(md5sum bundle.js | awk '{print $1}')

        if [ "$md5_original_value" == "$md5_temp_value" ]; then
            echo -e "${yellowColour}[+]${endColour} ${grayColour}No hay actualizaciones.${endColour}\n"
        else
            echo -e "${yellowColour}[+]${endColour} ${grayColour}Archivos actualizados.${endColour}\n"
            mv bundle_temp.js bundle.js
        fi
        rm bundle_temp.js
    fi
    tput cnorm
}


function searchMachine() {
    echo -e "${yellowColour}[+]${endColour} ${grayColour}Listando las propiedades de la máquina $machineName...${endColour}\n"
    cat bundle.js | awk "/name: \"$machineName\"/,/resuelta:/" | grep -vE "id:|sku:|resuelta" | tr -d "," | tr -d '"' | sed 's/^ *//'
}
function searchIP() {
    machineName=$(cat bundle.js | grep "ip: \"$machineIP\"" -B 3 | grep "name: " | awk 'NF{print $NF}' | tr -d '"' | tr -d ",")
    echo -e "${yellowColour}[+]${endColour} ${grayColour}La maquina correspondiente para la IP${endColour} ${blueColour}$machineIP${endColour} es ${purpleColour}$machineName${endColour}\n"
}   

declare -i parameter_counter=0

while getopts "hi:m:u" arg; do
    case $arg in
    m)
        machineName=$OPTARG
        ((parameter_counter += 1))
        ;;
    u)
        ((parameter_counter += 2))
        ;;
    i)
        machineIP=$OPTARG
        ((parameter_counter += 3))
        ;;
    h) ;;
    *) ;;
    esac
done

if [ $parameter_counter -eq 1 ]; then
    searchMachine "$machineName"
elif [ $parameter_counter -eq 2 ]; then
    updateFiles
elif [ $parameter_counter -eq 3 ]; then
    searchIP "$machineIP"
else
    helpPanel
fi
