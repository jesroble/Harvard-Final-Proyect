from colorama import Fore, init

init()

messages = {
    "en": 
    {
        "choose_level": Fore.CYAN + "\nChoose level from 1 to 4: " + Fore.RESET,
        "wrong_level": Fore.YELLOW + "Error: Choose level from 1 to 4: " + Fore.RESET,
        "column": Fore.RED + "Error: map closing columns must be walls" + Fore.RESET,
        "row": Fore.RED + "Error: map closing rows must be walls" + Fore.RESET,
        "empty_map": Fore.RED + "Error: map is empty" + Fore.RESET,
        "error_length": Fore.RED + "Error: map dimensions are inconsistent" + Fore.RESET,
        "error_player": Fore.RED + "Error: there must be one player" + Fore.RESET,
        "error_coin": Fore.RED + "Error: there must be at least one coin" + Fore.RESET,
        "error_exit": Fore.RED + "Error: there must be one exit" + Fore.RESET,
        "unsolvable": Fore.RED + "Error: map is unsolvable" + Fore.RESET,
        "sprite_error": Fore.RED + "Error: sprite not found" + Fore.RESET,
        "win": Fore.GREEN + "\nCongratulations! You solved the map" + Fore.RESET,
        "pick_coins": Fore.MAGENTA + "Pick all coins before exit" + Fore.RESET
    },
    
    "es":
    {
        "choose_level": Fore.CYAN + "\nElige nivel del 1 al 4: " + Fore.RESET,
        "wrong_level": Fore.YELLOW + "Error: Elige nivel del 1 al 4: " + Fore.RESET,
        "column": Fore.RED + "Error: las columnas de cierre del mapa deben ser paredes" + Fore.RESET,
        "row": Fore.RED + "Error: las filas de cierre del mapa deben ser paredes" + Fore.RESET,
        "empty_map": Fore.RED + "Error: el mapa está vacío" + Fore.RESET,
        "error_length": Fore.RED + "Error: las dimensiones del mapa son inconsistentes" + Fore.RESET,
        "error_player": Fore.RED + "Error: debe haber un jugador" + Fore.RESET,
        "error_coin": Fore.RED + "Error: debe haber al menos una moneda" + Fore.RESET,
        "error_exit": Fore.RED + "Error: debe haber una salida" + Fore.RESET,
        "unsolvable": Fore.RED + "Error: el mapa no tiene solución" + Fore.RESET,
        "sprite_error": Fore.RED + "Error: sprite no encontrado" + Fore.RESET,
        "win": Fore.GREEN + "\n¡Felicidades! Has resuelto el mapa" + Fore.RESET,
        "pick_coins": Fore.MAGENTA + "Recoge todas las monedas antes de salir" + Fore.RESET
    }
}