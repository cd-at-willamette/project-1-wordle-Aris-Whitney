########################################
# Name:Aris Whitney
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):6.5
# Description of any added extensions:
########################################

from WordleGraphics import *   #WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import *  #ENGLISH_WORDS, is_english_word
import random

CORRECT_COLOR = "green"
PRESENT_COLOR = "yellow"
MISSING_COLOR = "gray"

def random_five_letter_word() -> str:
    random.shuffle(ENGLISH_WORDS)
    for word in ENGLISH_WORDS:
        if len(word) == 5:  # Check for 5-letter words
            return word 

def wordle():
    gw = WordleGWindow()
    answer = random_five_letter_word()  # Get a random 5-letter word   

    def color_row(row: int, guess: str, answer: str):
        guess = guess.lower()
        answer = answer.lower()


        colored_answer = [False] * len(answer)
        colored_guess = [False] * len(guess)
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                gw.set_square_color(row, i, CORRECT_COLOR) #green
                colored_answer[i] = True
                colored_guess[i] = True
                gw.set_key_color(guess[i], CORRECT_COLOR) #milestone 5
        for i in range(len(guess)):
            if not colored_guess[i] and guess[i] in answer:
                for j in range(len(answer)):
                    if guess[i] == answer[j] and not colored_answer[j] and not colored_guess[i]:
                        gw.set_square_color(row, i, PRESENT_COLOR) #yellow
                        colored_answer[j] = True
                        colored_guess[i] = True
                        gw.set_key_color(guess[i], PRESENT_COLOR) #milestone 5
                        break


        for i in range(len(guess)):
            if not colored_guess[i]:
                gw.set_square_color(row, i, MISSING_COLOR) #gray
                gw.set_key_color(guess[i], MISSING_COLOR) #milestone 5

    def display_affirmation(message):
        gw.show_message(message)

    def enter_action():
        current_row = gw.get_current_row() 
        guess = ""  
        
        for col in range(5):  #guess is always 5 letters long
            letter = gw.get_square_letter(current_row, col)  # Get each letter
            guess += letter  #combine multiple strings into 1
        
        guess = guess.upper()  # change to uppercase

        if is_english_word(guess.lower()):  # Check if the guess is in the word list
            color_row(current_row, guess, answer)  # Color the row based on the guess and answer
    #milestone 4        
            # Check if the guess is correct
            if guess.lower() == answer:
                display_affirmation("Congratulations! You've guessed the word!")
                gw.set_current_row(N_ROWS)  # Stop any more guesses
            else:
                # Move to the next row if guesses remain
                if current_row < N_ROWS - 1:  # make sure a next row exists
                    gw.set_current_row(current_row + 1)  # Move to the next row
                else:
                    display_affirmation(f"Game over! The answer was '{answer}'.")
                    gw.show_message(f"The correct answer was: {answer}")
        else:
            gw.show_message("Not in word list")  

    gw.add_enter_listener(enter_action)  

# Startup boilerplate
if __name__ == "__main__":
    wordle()
    wordle()
