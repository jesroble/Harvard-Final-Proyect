from colorama import Fore

HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========""",
]

#dictionary in both languages
messages = {
    "en": 
    {
        "choose_mode": Fore.CYAN + "\nChoose game mode: PVP or PVE: " + Fore.RESET,
        "wrong_mode": Fore.YELLOW + "Wrong mode, choose between PVP or PVE: " + Fore.RESET,
        "write_word": Fore.CYAN + "\nWrite the word to guess: " + Fore.RESET,
        "only_letters": Fore.YELLOW + "Write only alphabetic characters: " + Fore.RESET,
        "file_error": Fore.RED + "\nError. {} not found" + Fore.RESET,
        "word": Fore.GREEN + "\nWord: " + Fore.RESET,
        "failed_letters": Fore.RED + "\nFailed letters: {}      Tries remaining {}" + Fore.RESET,
        "guess": Fore.CYAN + "Guess a letter: " + Fore.RESET,
        "only_one": Fore.YELLOW + "Write only one letter." + Fore.RESET,
        "already_written": Fore.YELLOW + "You have already written that letter." + Fore.RESET,
        "win": Fore.GREEN + "\nCongratulations, you guessed the word!" + Fore.RESET,
        "game_over": Fore.MAGENTA + "\nGame over! The word was: {}\n" + Fore.RESET,
    },
    "es": 
    {
        "choose_mode": Fore.CYAN + "\nElige el modo de juego: PVP o PVE: " + Fore.RESET,
        "wrong_mode": Fore.YELLOW + "Modo incorrecto, elige entre PVP o PVE: " + Fore.RESET,
        "write_word": Fore.CYAN + "\nEscribe la palabra a adivinar: " + Fore.RESET,
        "only_letters": Fore.YELLOW + "Escribe solo caracteres alfabéticos: " + Fore.RESET,
        "file_error": Fore.RED + "\nError. {} no encontrado" + Fore.RESET,
        "word": Fore.GREEN + "\nPalabra: " + Fore.RESET,
        "failed_letters": Fore.RED + "\nLetras fallidas: {}      Intentos restantes: {}" + Fore.RESET,
        "guess": Fore.CYAN + "Adivina una letra: " + Fore.RESET,
        "only_one": Fore.YELLOW + "Escribe solo una letra." + Fore.RESET,
        "already_written": Fore.YELLOW + "Ya has escrito esa letra." + Fore.RESET,
        "win": Fore.GREEN + "\n¡Felicidades, adivinaste la palabra!" + Fore.RESET,
        "game_over": Fore.MAGENTA + "\n¡Juego terminado! La palabra era: {}\n" + Fore.RESET,
    }
}