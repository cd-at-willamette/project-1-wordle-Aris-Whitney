########################################
# Name:Aris Whitney
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):3
# Description of any added extensions:
########################################

from WordleGraphics import *   #WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import *  #ENGLISH_WORDS, is_english_word
import random

CORRECT_COLOR = "green"
PRESENT_COLOR = "yellow"
MISSING_COLOR = "gray"

def wordle():
    gw = WordleGWindow()
    answer = "GLASS"  
    #milestone 2
    def color_row(row: int, guess: str, answer: str):
        guess = guess.lower()
        answer = answer.lower()
        
        colored_answer = [False] * len(answer)  
        colored_guess = [False] * len(guess)    

       
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)  #green
                colored_answer[i] = True 
                colored_guess[i] = True   


        for i in range(len(guess)):
            if not colored_guess[i] and guess[i] in answer:
                for j in range(len(answer)):
                    if guess[i] == answer[j] and not colored_answer[j] and not colored_guess[i]:
                        gw.set_square_color(row, i, PRESENT_COLOR)  #yellow
                        colored_answer[j] = True  
                        colored_guess[i] = True    
                        break  #this lets us move to the next letter in the row and end loop 

        for i in range(len(guess)):
            if not colored_guess[i]:  
                gw.set_square_color(row, i, MISSING_COLOR)  #gray

    def display_affirmation(guess):
        gw.show_message(f"Good guess: {guess}!")
    #milestone 1
    def enter_action():
        current_row = gw.get_current_row() 
        guess = ""  
        
        for col in range(5): 
            letter = gw.get_square_letter(current_row, col)  
            guess += letter 
        
        guess = guess.upper()  #change to uppercase

        if is_english_word(guess.lower()):  
            color_row(current_row, guess, answer)  
            display_affirmation(guess)  
        else:
            gw.show_message("Not in word list")  

    gw.add_enter_listener(enter_action)  

# Startup boilerplate
if __name__ == "__main__":
    wordle()
