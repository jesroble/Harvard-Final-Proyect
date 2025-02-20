import random
import os

from Hangman.hangman_text import HANGMAN_PICS, messages
from colorama import init, Fore

init()

def get_word(mode, lan): #gets mode and language
    
    if mode == "PVP":
        word = input(messages[lan]["write_word"]).lower()
        while not word.isalpha():
            word = input(messages[lan]["only_letters"])
        return word
        
    elif mode == "PVE":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filename = "words_en.txt" if lan == "en" else "words_es.txt"
        filepath = os.path.join(current_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                word_list = [line.strip() for line in file.readlines()]
                return random.choice(word_list)
        except FileNotFoundError:
            print(messages[lan]["file_error"].format(filepath)) #doc not found
            exit()

def print_progress(word, g):
    return " ".join([letter if letter in g else "_" for letter in word])

def play_hangman(lan):

    # The player choose between play versus other player or the computer
    mode = input(messages[lan]["choose_mode"]).strip()
    while mode not in ["PVP", "PVE"]:
        mode = input(messages[lan]["wrong_mode"])
    
    word = get_word(mode, lan)
    tries = 6
    guessed_letters = set()
    failed_letters = set()

    #print the progress 
    while tries > 0:
        print("\n--------------------------------")
        print(HANGMAN_PICS[6 - tries])
        print(messages[lan]["word"], print_progress(word, guessed_letters))
        print(messages[lan]["failed_letters"].format(', '.join(failed_letters), tries))
        letter = input(messages[lan]["guess"]).lower()

        # check input errors
        if not letter.isalpha():
            print(messages[lan]["only_letters"])
            continue
        if len(letter) != 1:
            print(messages[lan]["only_one"])
            continue
        if letter in guessed_letters or letter in failed_letters:
            print(messages[lan]["already_written"])
            continue

        if letter in word:
            guessed_letters.add(letter)
        else:
            tries -= 1
            failed_letters.add(letter)
        
        if set(word) <= guessed_letters:
            print("\n--------------------------------")
            print(messages[lan]["win"])
            print(f"{''.join(word)}\n")
            print("--------------------------------")
            return
    
    print("\n--------------------------------")
    print(HANGMAN_PICS[6 - tries])
    print(messages[lan]["game_over"].format(''.join(word)))
    print("--------------------------------")
