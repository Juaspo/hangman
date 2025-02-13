#!/usr/bin/env python3

'''
The program needs to pick a word
The program needs to count how many letters that word contains
replace letters with underscore
Keep track of amount of guesses

----
keep correct letters
keep wrong letters
and keep of when the word is complete

----
Accept user input
It needs to check user input
show correct and incorrect guessed letters
'''

import random


nr_of_tries = 5
the_word = ""
guessed_word = ""
guessed_word_list = []

# Takes in the word and print the equivalent amount of letters in dashes
def print_lines(word1):
    word2 = ""
    print("\n########################################")
    print("Lets play hangman. Guess the word below")
    guessed_word_list.clear()
    for x in word1:
        print("-", end='')
        word2 += "-"
        guessed_word_list.append("-")
    print("")
    return word2

# A function to check if the provided letter exists in the word
def check_match (word, user_input):
    match_found = False
    n = 0

    for x in word:
        if(x == user_input):
            match_found = True
            #print(x, end='')
            guessed_word_list[n] = x
        #else:
            #print("_ ", end='')
        n += 1
        

    if(match_found == True):
        print("A match found on:", user_input)
        return True
    else:
        print("No match found", user_input)
        return False


def check_if_word_complete(word1):
    word2 = ""
    for x in guessed_word_list:
        word2 += x
    print(word2)
    if(word1 == word2):
        return True
    else:
        return False


def shuffle_words(shuffle_list):
    random.shuffle(shuffle_list)
    return(shuffle_list)


word_file = open("words.txt", "rt")
word_list = word_file.readlines()
word_list = shuffle_words(word_list)


for file_line in word_list:
    word_complete = False
    tries = 0
    the_word = file_line.strip()
    guessed_word = print_lines(the_word)

    while tries < nr_of_tries:
        user_guess = input("type in a letter to guess: ")
        if(check_match(the_word, user_guess) is False):
            tries += 1
            print("you have",nr_of_tries-tries, "tries left")
        word_complete = check_if_word_complete(the_word)
        print("______________________________________")
        if(word_complete):
            break

    if(word_complete):
        print("* * * Congratulations * * *")
        print(f"You have manged to guess the correct word [{the_word}]")
    else:
        print("X X X Too bad X X X")
        print(f"You did not guess the correct word [{the_word}]")


word_file.close()
