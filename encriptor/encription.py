"""
This module is used when there's a need to encript or decript some text.
"""
import random
import string

def encripter(quote, outputFile):
    #Variable incializations
    everySimbol = string.ascii_letters + string.digits + string.punctuation
    differentSimbols = []
    changedSimbols = {}
    #separate each letter from the original quote.
    for simbol in quote:
        if simbol in differentSimbols:
            continue
        else:
            differentSimbols.append(simbol)
    for simbol in differentSimbols:
        i = 0
        while i == 0: # if by random, it creates 2 equal values, it'll create another so that we don't have duplicated values
            new_simbol = ""
            for item in random.choices(everySimbol,k = 5):
                new_simbol += item
            if new_simbol not in changedSimbols.values():
                i = 13
                changedSimbols[simbol] = new_simbol
    print(changedSimbols)
        
