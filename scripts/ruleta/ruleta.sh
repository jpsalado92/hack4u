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

function martingala() {
    echo -e "\n${yellowColour}[+]${endColour}${grayColour} Dinero actual:${endColour} ${yellowColour}$money€${endColour}"
    echo -en "${yellowColour}[+]${endColour}${grayColour} ¿Cuánto dinero quieres apostar? -> ${endColour}" && read initial_bet
    echo -en "${yellowColour}[+]${endColour}${grayColour} ¿A qué deseas apostar continuamente (par/impar)? -> ${endColour}" && read par_impar
    echo -en "${yellowColour}[+]${endColour}${grayColour} Vamos a jugar con la catidad de: ${endColour}${yellowColour}$initial_bet€${endColour} ${grayColour}a${endColour} ${yellowColour}$par_impar${endColour}\n"
    tput civis
    backup_bet=$initial_bet
    while true; do
        money=$(($money - $initial_bet))
        echo -e "\n${yellowColour}[+]${endColour}${grayColour} Has apostado ${yellowColour}$initial_bet€${grayColour} y te quedan ${yellowColour}$money€${endColour}"
        random_number="$(($RANDOM % 37))"
        echo -e "${yellowColour}[+]${endColour}${grayColour} Ha salido el ${blueColour}$random_number${endColour}"

        if [[ $par_impar == "par" ]]; then
            if [[ "$(("$random_number" % 2))" -eq 0 ]]; then
                if [[ "$random_number" -eq 0 ]]; then
                    echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido el 0, ${redColour}por lo tanto perdemos${endColour}"
                    win=0
                else
                    echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número par, ${greenColour}¡ganamos!${endColour}"
                    win=1
                fi
            else
                echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número impar, ${redColour}por lo tanto perdemos${endColour}"
                win=0

            fi
        fi

        if [[ $par_impar == "impar" ]]; then
            if [[ "$(("$random_number" % 2))" -eq 0 ]]; then
                if [[ "$random_number" -eq 0 ]]; then
                    echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido el 0, ${redColour}por lo tanto perdemos${endColour}"
                    win=0
                else
                    echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número par, ${redColour}por lo tanto perdemos${endColour}"
                    win=0
                fi
            else
                echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número impar, ${greenColour}¡ganamos!${endColour}"
                win=1
            fi
        fi

        if [[ $win == "1" ]]; then
            money=$(("$money" + "$initial_bet" * 2))
            initial_bet=$backup_bet
        else
            initial_bet=$(("$initial_bet" * 2))
        fi

        echo -e "${yellowColour}[+]${endColour}${grayColour} Te quedan${endColour} ${yellowColour}$money€${endColour}"

        if [[ $money -le 0 ]]; then
            break
        fi
    done

    tput cnorm

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
    if [ "$technique" == "martingala" ]; then
        echo -e "\n${yellowColour}[+]${endColour} Voy a jugar con ${purpleColour}$money€${endColour} usando la tecnica ${purpleColour}$technique${endColour}\n"
        martingala
    elif [ "$technique" == "inverseLabrouchere" ]; then
        echo "w"
    else
        echo -e "${redColour}[+] La tecnica proporcionada no existe.${endColour}\n"
    fi
else
    helpPanel
fi
# "inverseLabrouchere"
