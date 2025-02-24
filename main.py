from Hangman.hangman import play_hangman
from Solvemap.solvemap import solvemap
from messages import messages

from colorama import init, Fore

init()

def main():
    lan = input(Fore.CYAN + "\nChoose language (es/en): " + Fore.RESET).lower()
    while lan not in ["es", "en"]:
        lan = input(Fore.YELLOW + "Choose between es or en: "+ Fore.RESET).lower()
    
    while True:
        game = input(messages[lan]["choose_game"]).lower()

        if game in ["hangman", "ahorcado"]:
            play_hangman(lan)
        elif game in ["map", "mapa"]:
            solvemap(lan)
        elif game in ["e", "s"]:
            exit()
        else:
            print(messages[lan]["wrong_game"])

if __name__ == "__main__":
    main()