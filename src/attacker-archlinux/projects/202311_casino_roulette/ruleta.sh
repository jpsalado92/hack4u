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
    echo -e "\t${purpleColour}t)${endColour} ${grayColour}Indica la tecnica a usar (inverseLabrouchere, martinGala)${endColour}"
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
    loosingStreak="[ "
    play_counter=0
    while true; do
        play_counter=$((play_counter + 1))
        money=$(($money - $initial_bet))
        echo -e "\n${yellowColour}[+]${endColour}${grayColour} Has apostado ${yellowColour}$initial_bet€${grayColour} y te quedan ${yellowColour}$money€${endColour}"
        random_number="$(($RANDOM % 37))"
        echo -e "${yellowColour}[+]${endColour}${grayColour} Ha salido el ${blueColour}$random_number${endColour}"
        handleWinOrLoose

        if [[ $win == "1" ]]; then
            money=$(("$money" + "$initial_bet" * 2))
            initial_bet=$backup_bet
            loosingStreak="["
        else
            initial_bet=$(("$initial_bet" * 2))
            loosingStreak="$loosingStreak $random_number"
        fi

        echo -e "${yellowColour}[+]${endColour}${grayColour} Te quedan${endColour} ${yellowColour}$money€${endColour}"

        if [[ $money -le 0 ]]; then
            echo -e "${redColour}[+] Te has quedado sin dinero despues de $play_counter jugadas.${endColour}"
            loosingStreak="$loosingStreak ]"
            echo -e "${redColour}[+] La cadena de tiros fallidos ha sido $loosingStreak.${endColour}"
            break
        fi
    done
    tput cnorm
}

function inverseLabrouchere() {

    echo -en "${yellowColour}[+]${endColour}${grayColour} ¿A qué deseas apostar continuamente (par/impar)? -> ${endColour}" && read par_impar
    echo -en "\n"
    declare -a my_sequence=(1 2 3 4)


    play_counter=0
    while true; do
        echo -e "\n${yellowColour}[+]${endColour}${grayColour} Dinero actual:${endColour} ${yellowColour}$money€${endColour}"
        play_counter=$((play_counter + 1))
        tput civis
        if [ "${#my_sequence[@]}" -gt 1 ]; then
            initial_bet=$(("${my_sequence[0]}" + "${my_sequence[-1]}"))
        elif [ "${#my_sequence[@]}" -eq 1 ]; then
            initial_bet="${my_sequence[0]}"
        else
            my_sequence=(1 2 3 4)
        fi
        echo -en "${yellowColour}[+]${endColour}${grayColour} Comenzamos con la secuencia ${turquoiseColour}[${my_sequence[*]}]${endColour}\n"

        my_sequence=(${my_sequence[@]})
        money=$(($money - $initial_bet))
        echo -en "${yellowColour}[+]${endColour}${grayColour} Apostamos ${yellowColour}$initial_bet€${endColour} a ${purpleColour}$par_impar${endColour}, nos quedan ${yellowColour}$money€${endColour}\n"
        random_number="$(($RANDOM % 37))"
        echo -e "${yellowColour}[+]${endColour}${grayColour} Ha salido el ${blueColour}$random_number${endColour}"
        handleWinOrLoose

        if [[ $win == "1" ]]; then
            money=$(("$money" + "$initial_bet" * 2))
            my_sequence+=("$initial_bet")
            my_sequence=("${my_sequence[@]}")
            loosingStreak="["
        else
            unset my_sequence[0]
            unset my_sequence[-1] 2>/dev/null
            my_sequence=("${my_sequence[@]}")
            loosingStreak="$loosingStreak $random_number"
        fi
        echo -e "${yellowColour}[+]${endColour}${grayColour} Balance actual:${endColour} ${yellowColour}$money€${endColour}"

        if [[ $money -le 0 ]]; then
            echo -e "${redColour}[+] Te has quedado sin dinero despues de $play_counter jugadas.${endColour}"
            loosingStreak="$loosingStreak ]"
            echo -e "${redColour}[+] La cadena de tiros fallidos ha sido $loosingStreak.${endColour}"
            break
        fi
    done
    tput cnorm
}

function handleWinOrLoose() {
    if [[ $par_impar == "par" ]]; then
        if [[ "$(("$random_number" % 2))" -eq 0 ]]; then
            if [[ "$random_number" -eq 0 ]]; then
                echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido el ${purpleColour}0${endColour}, ${redColour}por lo tanto perdemos${endColour}"
                win=0
            else
                echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número ${purpleColour}par${endColour}, ${greenColour}¡ganamos!${endColour}"
                win=1
            fi
        else
            echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número ${purpleColour}impar${endColour}, ${redColour}por lo tanto perdemos${endColour}"
            win=0

        fi
    fi

    if [[ $par_impar == "impar" ]]; then
        if [[ "$(("$random_number" % 2))" -eq 0 ]]; then
            if [[ "$random_number" -eq 0 ]]; then
                echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido el ${purpleColour}0${endColour}, ${redColour}por lo tanto perdemos${endColour}"
                win=0
            else
                echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número ${purpleColour}par${endColour}, ${redColour}por lo tanto perdemos${endColour}"
                win=0
            fi
        else
            echo -e "${yellowColour}[+]${endColour} ${grayColour}Ha salido un número ${purpleColour}impar${endColour}, ${greenColour}¡ganamos!${endColour}"
            win=1
        fi
    fi
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
    if [ "$technique" == "martinGala" ]; then
        echo -e "\n${yellowColour}[+]${endColour} Voy a jugar con ${purpleColour}$money€${endColour} usando la tecnica ${purpleColour}$technique${endColour}\n"
        martingala
    elif [ "$technique" == "inverseLabrouchere" ]; then
        echo -e "\n${yellowColour}[+]${endColour} Voy a jugar con ${purpleColour}$money€${endColour} usando la tecnica ${purpleColour}$technique${endColour}\n"
        inverseLabrouchere
    else
        echo -e "${redColour}[+] La tecnica proporcionada no existe.${endColour}\n"
    fi
else
    helpPanel
fi
