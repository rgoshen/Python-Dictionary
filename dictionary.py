import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return f"{word} cannot be found!"

word = input('Enter in word: ')

print(translate(word))
