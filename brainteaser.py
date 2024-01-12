"""
Description: This game will have 10 rounds back to back. You will be presented with one word and two options. 
You must select the font colour of the given word. 
For example: the given word is "white", then given option are "white" or "black". Here, the correct answer is "black", 
because player is expected to choose the colour of the font.  
"""

import random  #import random module to generate random numbers 
from colorama import Fore, Style  #import colours 

def select_random_numbers():               #this function will generate three random numbers
    while True:                            #loop will go on until we get three randomly selected distinct numbers
        num1 = random.randint(0, 5)        #num1 to randomly select a word from the word list
        num2 = random.randint(0, 5)        #num2 to randomly select a colour from the color list
        num3 = random.randint(0, 5)
        if num1 != num2 and num1 != num3 and num2 != num3 and num1 != num2 != num3:
            break
    return num1, num2, num3

def print_random_word_and_options(word_list, color_list, num1, num2, num3): #this function takes word list, color list, and three random numbers as input
    random_word = word_list[num1]     #to select random word from the list                                           
    random_color = color_list[num2]   #to select random font from the list

    print(random_color + random_word + Style.RESET_ALL) #prints a randomly selected word in a randomly selected color

    list = [word_list[num3], word_list[num2]] #to print two options 
    random.shuffle(list)                     #to ensure randomness in the list
    print(list[1], "or", list[0])

    return list

def play_game():
    
    word_list = ["green", "white", "red", "purple", "blue", "yellow"] # List of words
    color_list = [Fore.GREEN, Fore.WHITE, Fore.RED, Fore.MAGENTA, Fore.BLUE, Fore.YELLOW] # List of font
    rounds = 0
    score = 0

    while rounds < 10:
        #we are calling the function that generates three random numbers for selecting words and colors
        num1, num2, num3 = select_random_numbers()

        #we are calling the function to print a random word and two options for the player to choose the color
        word_options = print_random_word_and_options(word_list, color_list, num1, num2, num3)
        #ask for player's answer
        ans = input("a or b: ")
        #this dictionary with 'a' and 'b' as keys and corresponding word options
        new_list = {"a": word_options[1], "b": word_options[0]}
        # Check if player's choice is valid or not
        if ans in ["a", "b"]:
            # Find the index of the colour in the color_list
            color_index = color_list.index(color_list[num2])
            # Check if the player's choice matches the color of the word
            if new_list[ans] == word_list[color_index]:
                print("correct")
                score += 1
            else:
                print("wrong")
        else:
            print("Invalid input! Please choose 'a' or 'b'.")

        rounds += 1 ## Increment the round 

    print("Your score:", score, "/", rounds)  # Print the final score after completing 10 rounds

# Run the game
play_game()
