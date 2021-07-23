import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    return word[data]

word = input("Enter the word: ")
print(dictionary(word))