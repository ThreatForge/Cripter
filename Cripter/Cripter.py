"""
This module is used when there's a need to encript or decript some text.
"""
import random
import string


def keyGenerator(outputFile,quote = False):
    """
    Generates encription-keys for a given quote or 
    Generates a keyDictionary with a key for every simbol.

    Requires: outputFile str that represents the path to the output file,
    quote str represents what you want to translate -> it's not required if you want to create a "keyDictionary"(a key for every simbol possible)
    Ensures: Keys for the wanted simbols
    """
    #Variable incializations
    everySimbol = string.ascii_letters + string.digits + string.punctuation + " áéíóúâêîôûàèìòùãõäëïöüÁÉÍÓÚÂÊÎÔÛÀÈÌÒÙÃÕÄËÏÖÜ"
    differentSimbols = []
    changedSimbols = {}
    #separate each letter from the "quote"
    if quote == False: #if they don't give the function a quote, it'll generate a dictionary.
        quote = everySimbol
        for simbol in quote:
            if simbol in differentSimbols:
                continue
            else:
                differentSimbols.append(simbol)
    else:
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
    
    with open(outputFile,'w') as file:
        for key in changedSimbols:
            file.write(f"{key} :\n")
            file.write(f"{changedSimbols[key]}\n")
    return changedSimbols

def readKeys(filePath):
    """
    Interprets the keys in a given file.

    Requires: filePath str representing the path to where you have pre-saved keys.
    Ensures: dictionary with simbols as the key and "keys" has the value
    """
    #Variable incializations
    keyDict = {}
    i = 0
    simbol = ""
    #Code
    with open(filePath,"r") as file:
        for item in file:
            if i%2 == 0:
                simbol = item.replace(" :\n","")
            else:
                keyDict[simbol] = item.replace("\n","")
            i += 1
    return keyDict

def encripter(quote, outputFile,keys = False):
    """
    Encripts given messages
    
    Requires: quote str that represents the quote you want to encript,
    outputFile str representing the path to where you want to save your keys,
    keys(optional) str representing the path where you have pre-saved keys.
    Ensures: encripted message.
    """
    #Intializing variables
    new_quote = ""
    #code
    if keys == False:
        keys = keyGenerator(outputFile)
    else:
        keys = readKeys(keys)
    for item in quote:
        new_quote += keys[item]
    return new_quote

def decripter (quote, keysPath):
    """
    Decript a given message

    Requires: quote str that represents an encripted quote,
    keysPath str that represent the path to the file containing the keys
    Ensures: decripted message.
    """
    #Initializing variables
    quoteBreak = []
    new_quote = ""
    #Code
    keys = readKeys(keysPath)
    while len(quote) != 0:
        quoteBreak.append(quote[:5])
        quote = quote[5:]
    for item in quoteBreak:
        for k,v in keys.items():
            if v == item:
                new_quote += k
    return new_quote