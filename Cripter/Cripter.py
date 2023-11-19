import random
import string

def generateEncryptionKeys(outputFilePath, textToEncrypt=None):
    """
    Generates encryption keys for a given text or creates a key dictionary with a key for every symbol.

    Requires: 
        - outputFilePath (str): Path to the output file.
        - textToEncrypt (str, optional): Text to be translated. If not provided, a key dictionary will be generated.
    
    Ensures: 
        Keys for the desired symbols.
    """
    # Variable initializations
    allSymbols = string.ascii_letters + string.digits + string.punctuation + " áéíóúâêîôûàèìòùãõäëïöüÁÉÍÓÚÂÊÎÔÛÀÈÌÒÙÃÕÄËÏÖÜ"
    uniqueSymbols = []
    symbolMapping = {}

    # Separate each letter from the text
    if textToEncrypt is None:
        textToEncrypt = allSymbols
        for symbol in textToEncrypt:
            if symbol in uniqueSymbols:
                continue
            else:
                uniqueSymbols.append(symbol)
    else:
        for symbol in textToEncrypt:
            if symbol in uniqueSymbols:
                continue
            else:
                uniqueSymbols.append(symbol)

    # Generate random keys for each unique symbol
    for symbol in uniqueSymbols:
        i = 0
        while i == 0:
            newSymbol = "".join(random.choices(allSymbols, k=5))
            if newSymbol not in symbolMapping.values():
                i = 13
                symbolMapping[symbol] = newSymbol

    # Write the generated keys to the output file
    with open(outputFilePath, 'w') as file:
        for key, value in symbolMapping.items():
            file.write(f"{key} :\n")
            file.write(f"{value}\n")

    return symbolMapping

def readKeys(filePath):
    """
    Reads and interprets keys from a given file.

    Requires: 
        - filePath (str): Path to the file containing pre-saved keys.
    
    Ensures: 
        Dictionary with symbols as keys and corresponding keys as values.
    """
    keyDictionary = {}
    count = 0
    symbol = ""

    with open(filePath, "r") as file:
        for line in file:
            if count % 2 == 0:
                symbol = line.replace(" :\n", "")
            else:
                keyDictionary[symbol] = line.replace("\n", "")
            count += 1

    return keyDictionary

def encrypt(text, outputFilePath, keys=None):
    """
    Encrypts given messages.

    Requires: 
        - text (str): The text to be encrypted.
        - outputFilePath (str): Path to save the generated keys.
        - keys (str, optional): Path to a file containing pre-saved keys.
    
    Ensures: 
        Encrypted message.
    """
    newText1 = ""
    newText2 = ""
    index = 0

    # Generate or read keys
    if keys is None:
        keys = generateEncryptionKeys(outputFilePath)
    else:
        keys = readKeys(keys)

    # Encrypt the message
    for char in text:
        newText1 += keys[char][::-1]

    # Rearrange the encrypted message for added security
    for symbol in newText1:
        if index % 2 == 0:
            newText2 += symbol
        else:
            newText2 += symbol
        index += 1

    return newText2

def decrypt(text, keysPath):
    """
    Decrypts a given message.

    Requires: 
        - text (str): The encrypted text.
        - keysPath (str): Path to the file containing the keys.
    
    Ensures: 
        Decrypted message.
    """
    # Initializing variables
    textBreakdown = []
    decryptedText = ""

    # Read keys from the specified file
    keys = readKeys(keysPath)

    # Break down the encrypted text into segments and reverse them
    while len(text) != 0:
        textBreakdown.append(text[:5][::-1])
        text = text[5:]

    # Reconstruct the decrypted text using the keys
    for segment in textBreakdown:
        for key, value in keys.items():
            if value == segment:
                decryptedText += key

    return decryptedText
