import time
import random
from english_words import english_words_lower_alpha_set

player_score = 0

player_name = input("Please give me your name: ")

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

ready_or_not = input("are you ready {}?: ".format(player_name))