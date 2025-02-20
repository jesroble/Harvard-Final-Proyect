from colorama import Fore, init

init()

messages = {
    "en": 
    {
        "choose_game": Fore.CYAN + "\nWhich game do you want to play? \n-Hangman   -Map \n-game3    -game4\n\n Or write \"e\" to exit: " + Fore.RESET,
        "wrong_game": Fore.YELLOW + "\nChoose between the given options" + Fore.RESET,
    },
    "es": 
    {
        "choose_game": Fore.CYAN + "\n¿A que juego quieres jugar? \n-Ahorcado     -Mapa \n-game3       -game4\n\n O escribe \"s\" para salir: " + Fore.RESET,
        "wrong_game": Fore.YELLOW + "\nElige entre las opciones dadas" + Fore.RESET
    }
}