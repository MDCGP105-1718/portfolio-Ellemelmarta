# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter_guess in secret_word:
        if letter_guess not in letters_guessed:
            return False
    return True
    #checks to see if letter_guess (the input from user) is in secret_word and returns true if not then false


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ''

    for letter_guess in range (len(secret_word)):
        if secret_word[letter_guess] in letters_guessed:
            guess += secret_word[letter_guess]
            #adding letter guessed to guess if correct
        else:
            guess += ' _ '
            #adding an underscore if the letter space is empty
    return guess



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ''

    #string.ascii_lowercase accounts for all the alphabet in lowercase
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters = available_letters + letter
    return available_letters
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guess_remaining = 6
    mistakes = 0 #set mistakes so i can count each time they get a letter wrong and check
    available_letters = get_available_letters(letters_guessed)

    print ("I want to play a game...")
    print ("Guess the word and make it out alive, the amount of letters in the word is: ", len(secret_word),  " good luck.")

    while mistakes < 6:
        print ("") #printing an empty line making it easier on the eye to read when printed

        if is_word_guessed(secret_word, letters_guessed):
            print (f"Congratulations you guessed the word, the word was: {secret_word}")
            break #otherwise it will go through the loop one more time even when you have won.

        print (f"Your remaining guesses: {guess_remaining}")
        print (f"The letters reamining are: {available_letters}")

        letter_guess = input("Please guess a letter: ") #sets new letter guess off users input each time through the loop

        if letter_guess in letters_guessed:
            print ("You've already guessed this letter lose a guess for not paying attention.")
            guess_remaining -= 1
            mistakes += 1
            print (get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(letter_guess)
            available_letters = get_available_letters(letters_guessed)

            if letter_guess in secret_word:
                print ("Correct guess it was in the word: " + get_guessed_word(secret_word, letters_guessed))
            else:
                print ("Incorrect guess that letter is not in the word: " + get_guessed_word(secret_word, letters_guessed))
                guess_remaining -= 1
                mistakes += 1
    #only way I could find to exit while loop as mistakes == 6 didnt work as the while loop doesnt let it run that far so else statement is easier way to break out when it reaches 6
    else:
        print("")
        print (f"You lost, you ran out of guesses. The word was: {secret_word}")

secret_word = choose_word(wordlist)
hangman(secret_word)
