import random

# ----------------------------------------------------
# PROVIDED HELPER FUNCTIONS (DO NOT MODIFY)
# ----------------------------------------------------

def load_words(filename="words.txt"):
    """
    Loads the word list from a file and returns a list of words.
    Each word is assumed to be in lowercase.
    """
    print("Loading word list from file...")
    with open(filename, 'r') as f:
        wordlist = f.read().split()
    print(f"{len(wordlist)} words loaded")
    return wordlist

def choose_word(wordlist):
    """
    wordlist: list of strings
    returns: string, a randomly chosen word from the list
    """
    return random.choice(wordlist)

def scramble_word(secret_word):
    """
    Scrambles the letters of the given secret word and prints the scrambled version.
    Does not return anything.
    """
    letters = list(secret_word)
    random.shuffle(letters)
    scrambled = ''.join(letters)
    print(f"Scrambled word: {scrambled}")

# ----------------------------------------------------
# FUNCTIONS TO IMPLEMENT
# ----------------------------------------------------

# Task 1.1 
def input_check(secret_word):
    # Remove 'pass', fill in your code here
    pass

# Task 1.2
def has_player_won(secret_word, user_guess):
    # Remove 'pass', fill in your code here
    pass

# Task 1.3 
def get_word_progress(secret_word, user_guess):
    # Remove 'pass', fill in your code here
    pass

# Task 2.1, 2.2 
def word_scramble():
    word_list = load_words()
    # Remove 'pass', fill in your code here
    pass


if __name__ == "__main__":
    word_scramble()
