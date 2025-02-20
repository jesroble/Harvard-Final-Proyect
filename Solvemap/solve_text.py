from colorama import Fore, init

init()

messages = {
    "en": 
    {
        "choose_level": Fore.CYAN + "\nChoose level from 1 to 4: " + Fore.RESET,
        "wrong_level": Fore.YELLOW + "Error: Choose level from 1 to 4: " + Fore.RESET,
        "sprite_error": Fore.RED + "Error: sprite not found" + Fore.RESET,
        "win": Fore.GREEN + "\nCongratulations! You solved the map" + Fore.RESET,
        "cannot_exit": Fore.MAGENTA + "Pick all coins before exit" + Fore.RESET
    },
    "es":
    {
        "choose_level": Fore.CYAN + "\nElige un nivel del 1 al 4: " + Fore.RESET,
        "wrong_level": Fore.YELLOW + "Error: Elige un nivel del 1 al 4: " + Fore.RESET,
        "sprite_error": Fore.RED + "Error: sprite no encontrado" + Fore.RESET,
        "win": Fore.GREEN + "\n¡Felicidades! Has resuelto el mapa" + Fore.RESET,
        "cannot_exit": Fore.MAGENTA + "Recoge todas las monedas antes de salir" + Fore.RESET
    }
}