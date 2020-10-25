import json

data = json.load(open("data.json"))

def look_up(word):
    lookup_word = word.lower()
    if lookup_word in data:
        return data[lookup_word]
    else:
        return f"{word} cannot be found!"

word = input('Enter in word: ')

print(look_up(word))
