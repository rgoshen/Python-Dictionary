import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def look_up(word):
    lookup_word = word.lower()
    if lookup_word in data:
        return data[lookup_word]
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
