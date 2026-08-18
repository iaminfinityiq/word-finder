from json import load
from typing import List, Dict
from os import name
from subprocess import call
from sys import exit
from time import sleep
from random import choice

def cls():
    call("cls" if name == "nt" else "clear", shell=True)

def help(tokens: List[str]):
    if len(tokens) != 1:
        print("The command only consists of the word 'help', not anything else")
        return

    print("""Here are the list of commands we have:
[1] help: Get all of the commands
[2] clean: Clears the terminal
[3] find <head>: Find words that start with the head
[4] quit: Quits the program""")

def clean(tokens: List[str]) -> None:
    if len(tokens) != 1:
        print("The command only consists of the word 'clean', not anything else")
        return

    cls()

def find(dictionary: Dict[str, List[str]], tokens: List[str]) -> None:
    if len(tokens) == 1:
        print("It is missing the starting word")
        return

    if len(tokens) != 2:
        print("The command only consists of the word 'find' and one other word, not anything else")
        return

    head: str = tokens[1].lower()
    if head not in dictionary:
        print(f"Unfortunately, there are no words that start with {head}")
        return

    possible_words: List[str] = dictionary[head]
    if possible_words == []:
        print(f"Unfortunately, there are no words that start with {head}")
        return

    if len(possible_words) == 1:
        print(f"There is only 1 word that starts with {head}, which is:")
        formed_word: str = f"{head} {possible_words[0]}"
        border: str = "-" * (len(formed_word) + 4)
        print(f"{border}\n| {formed_word} |\n{border}")
        return

    while True:
        cls()
        user_choice: str = input(f"""There are {len(possible_words)} words that start with {head}. Pick one of the two choices shown:
[1] Get a random word
[2] List all of the possible words

Type a number (1 or 2) corresponding to the choice you want to make: """).strip().lower()
        match user_choice:
            case "1":
                print("The random generated word is:")
                formed_word: str = f"{head} {choice(possible_words)}"
                border: str = "-" * (len(formed_word) + 4)
                print(f"{border}\n| {formed_word} |\n{border}")
                return
            case "2":
                print(f"All of the words that start with {head} are:")
                for i, word in enumerate(possible_words):
                    print(f"[{i+1}] {head} {word}")

                return
            case _:
                print("Invalid choice")
                input("Press enter to continue")

def quit(tokens: List[str]) -> None:
    if len(tokens) != 1:
        print("The command only consists of the word 'quit', not anything else")
        return

    exit(0)

def process_user_input(dictionary: Dict[str, List[str]], user_input: str) -> None:
    tokens: List[str] = user_input.split()
    if tokens == []:
        return
    
    match tokens[0]:
        case "help":
            help(tokens)
        case "clean":
            clean(tokens)
        case "find":
            find(dictionary, tokens)
        case "quit":
            quit(tokens)
        case _:
            print("Invalid command")

def main() -> None:
    cls()
    print("Loading data...")
    sleep(5)
    try:
        with open("filtered.json", encoding="utf-8") as file:
            dictionary: Dict[str, List[str]] = load(file)
    except FileNotFoundError:
        print("Data is not loaded successfully\nPlease make sure that you have the 'filtered.json' file inside this directory by running the 'loader.py' file")
        return

    cls()
    print("""---------------------
| WORD CHAIN FINDER |
---------------------

Welcome to the word chain finder, where you will find words that start with a certain head. This is a counter to DevTrung Mystic's bot on word chain.
Note that not all words are fully imported into this thing. The words here only come from a single source

Let's start by typing 'help' to take a look at the commands""")
    while True:
        user_input: str = input("> ")
        process_user_input(dictionary, user_input)

if __name__ == "__main__":
    main()