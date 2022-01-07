import time
import random
from english_words import english_words_set

player_score = 0 #initialize score

player_name = input("Please give me your name: ") #address the player

#the bottom variables will be used for providing the usable letters
letter_to_score_pairs = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z":10}
given_random_numbers = [random.randint(0, 25) for i in range(8)]
alphabet = list(letter_to_score_pairs.keys())
given_letters = [alphabet[i] for i in given_random_numbers]

#is the word a real english word?
def is_it_a_word(word):
    if (word in english_words_set) == True:
        return True
    else:
        return False

#is the word made from the hopelessly random list of letters?
def does_the_word_have_letters_from_list(word):
    for char in word:
        if (char not in given_letters):
            return False
        else:
            continue
    return True

#bad luck or lack of skill?
def scramble_list():
    new_random_numbers = [random.randint(0, 25) for i in range(8)]
    new_letters_after_scramble = [alphabet[i] for i in new_random_numbers]
    print("New Letters: ", new_letters_after_scramble)
    return new_letters_after_scramble

#let the player move forward
def update_score(word):
    points_gained = 0
    for char in word:
        points_gained += letter_to_score_pairs[char]
    return points_gained

#greet the player
print("""
Alright, {}. This program will provide you with 7 random letters. After which, if you're ready, you will have 10 seconds to type out as many words as you can.
You will earn points only if your words contains the given letters. 
- each letter has their own point value, but don't worry too much about that.
- The words must be in English.
- everything must be lowercase
- no punctuation is necessary
- you may also type "sp" (for "scramble please") in order to refresh your letter list if you got an unlucky draw
        *to scramble the list more than once, you must type "sp" again and hit <Enter> twice.

This is the first project that I will be doing without my hand being held. If somebody happens upon this program and finds it to be shitty, then that person would be right.
oh, and your score will be initialized to 0. You can only gain points, not lose points.
 """.format(player_name))

#decide if the program will run
ready_or_not = input("are you ready, {}? type either 'yes' or 'Yes': ".format(player_name))
if ready_or_not == "yes" or ready_or_not == "Yes":
    print("alright, {}. the letters youre confined to are: ".format(player_name), given_letters)
else:
    print("what? sorry, I cant hear you beyond me being extremely dissatisfied with you. toodles ;)")
    quit()

print("The timer will be activated and you will type as many words as possible using your given letters. Remember to type 'sp' to refresh your letters")
time.sleep(10)
print("start typing!!")

timer_begin = time.time()

while (time.time() - timer_begin < 10):
    player_word = input()
    if (player_word == "sp"):
        given_letters = scramble_list()
        player_word = input()
        continue
    if (is_it_a_word(player_word) == True):
        if (does_the_word_have_letters_from_list(player_word) == True):
            player_score += update_score(player_word)
        else:
            print("nope :/")
            continue
    else:
        print("try again")

if (player_score < 10):
    print(player_score)
    print("wow lol.")
elif (10 <= player_score < 50):
    print(player_score)
    print("cool :)")
else:
    print(player_score)
    print("you figured out the loophole and managed to type quickly enough, right? I haven't accounted for that in my code yet but I will figure that out later.")
