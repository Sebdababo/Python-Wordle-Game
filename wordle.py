import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

word_list = ["apple", "beach", "chair", "dance", "eagle", "flute", "grape", "house", "igloo", "juice"] # more words need to be added

def choose_word():
    return random.choice(word_list)

def check_guess(secret_word, guess):
    result = ""
    for i in range(5):
        if guess[i] == secret_word[i]:
            result += f"{Back.GREEN}{Fore.BLACK}{guess[i]}{Style.RESET_ALL}"
        elif guess[i] in secret_word:
            result += f"{Back.YELLOW}{Fore.BLACK}{guess[i]}{Style.RESET_ALL}"
        else:
            result += f"{Back.LIGHTBLACK_EX}{Fore.WHITE}{guess[i]}{Style.RESET_ALL}"
    return result

def play_wordle():
    secret_word = choose_word()
    attempts = 6
    
    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.")
    
    while attempts > 0:
        guess = input(f"Attempt {7 - attempts}/6. Enter your guess: ").lower()
        
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        result = check_guess(secret_word, guess)
        print(result)
        
        if guess == secret_word:
            print(f"Congratulations! You guessed the word {secret_word}!")
            return
        
        attempts -= 1
    
    print(f"Sorry, you've run out of attempts. The word was {secret_word}.")

if __name__ == "__main__":
    play_wordle()