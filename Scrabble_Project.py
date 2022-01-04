import time
import datetime
import random
from english_words import english_words_lower_alpha_set

player_score = 0 #initialize score

player_name = input("Please give me your name: ") #address the player

#the bottom variables will be used for providing the usable letters
letter_to_score_pairs = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z":10}
given_random_numbers = [random.randint(0, 26) for i in range(8)]
alphabet = list(letter_to_score_pairs.keys())
given_letters = [alphabet[i] for i in given_random_numbers]

print("""
Alright, {}. This program will provide you with 7 random letters. After which, if you're ready, you will have 10 seconds to type out as many words as you can.
You will earn points only if your words contains the given letters. 
- each letter has their own point value, but don't worry too much about that.
- The words must be in English.
- everything must be lowercase
- no punctuation is necessary

This is the first project that I will be doing without my hand being held. If somebody happens upon this program and finds it to be shitty, then that person would be right.
oh, and your score will be initialized to 0. You can only gain points, not lose points.
 """.format(player_name))

ready_or_not = input("are you ready, {}? type either 'yes' or 'Yes': ".format(player_name))

if ready_or_not == "yes" or ready_or_not == "Yes":
    print("alright, {}. the letters youre confined to are: ".format(player_name), given_letters)
else:
    print("well rerun this program once you are. and don't waste my time :(")
    quit()