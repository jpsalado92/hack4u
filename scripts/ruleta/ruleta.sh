#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

function ctrl_c() {
    echo -e "\n\n${redColour} [!] Saliendo...\n${endColour}"
    tput civis cnorm && exit 1
}

# Ctrl+C
trap ctrl_c INT

function helpPanel() {
    echo -e "\n${yellowColour}[+]${endColour} ${grayColour}Uso de $0:${endColour}"
    echo -e "\t${purpleColour}h)${endColour} ${grayColour}Mostrar panel de ayuda${endColour}"
    echo -e "\t${purpleColour}t)${endColour} ${grayColour}Indica la tecnica a usar${endColour}"
    echo -e "\t${purpleColour}m)${endColour} ${grayColour}Indica el dinero a apostar${endColour}"
    echo -e "\n"
    exit 1

}

while getopts "m:t:h" arg; do
    case $arg in
    m)
        money=$OPTARG
        ((parameter_counter += 1))
        ;;
    t)
        technique=$OPTARG
        ((parameter_counter += 2))
        ;;
    h)
        helpPanel
        ;;
    *)
        helpPanel
        ;;
    esac
done

if [ "$money" ] && [ "$technique" ]; then 
    if [ "$technique" == "inverseLabrouchere" ]; then
    echo -e "\n${yellowColour}[+]${endColour} Voy a jugar con ${purpleColour}$money${endColour} usando la tecnica ${purpleColour}$technique${endColour}\n"
    elif [ "$technique" == "martingala" ]; then
        echo "w"
    else
        echo -e "${redColour}[+] La tecnica proporcionada no existe.${endColour}\n"
    fi
else
    helpPanel
fi
# "inverseLabrouchere"
