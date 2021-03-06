"""
This program allows the user to enter in a word, proper 
noun or acronym to search in data file and returns definition(s).
Created by: R. Goshen
Date: 10-25-2020
I followed a tutorial from a course named "The Python Mega Course: 
Build 10 Real World Applications" on stackskills.    
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def look_up(word):
    """
    This function looks up a word, proper noun, or acronym in data file
    returns definition(s).
    """
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:      # ensures proper nouns can be found in data.
        return data[word.title()]
    elif word.upper() in data:      # ensures acronyms can be found in data.
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        user_choice = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter 'Y' for yes of 'N' for no: ")
        user_choice = user_choice.upper()

        if user_choice == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif user_choice == "N":
            return f"{word} cannot be found!"
        else:
            return "I am sorry.  I did not understand your entry."
    
    else:
        return f"{word} cannot be found!"

word = input('Enter in word: ')

output = look_up(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
