import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data: 
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {0} instead of {1}. If yes enter 'y'".format(get_close_matches(word, data.keys())[0], word))
        yn = yn.lower()
        if yn == "y": return data[get_close_matches(word, data.keys())[0]]
        else: return "Sorry we couldn't find what you want.."
    else:
        return "This word doesn't exist: "

word = input("Enter the word: ")
print(dictionary(word))