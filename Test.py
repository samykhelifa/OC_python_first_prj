# -*- coding: utf8 -*-

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]
def get_random_quote(my_list):
    # get a random number
    # get a quote from an array
    # show the quote in the interpreter
    rquote = my_list[0]
    print(rquote)
    # pass
user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')
if user_answer == "B":
    pass
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d’humour, je C...")
else:
    # show another quote
    pass

get_random_quote(quotes)
