# ThreatForge Encryption and Decryption Tool

## Overview
This Python module, developed by ThreatForge, provides functionalities for encryption and decryption of text. It includes key generation, key interpretation, encryption, and decryption processes.

## Features
- **Key Generation:**
  - `keyGenerator(outputFile, quote=False)`
    - Generates encryption keys for a given quote or creates a key dictionary with a key for every symbol.
    - Parameters:
      - `outputFile` (str): Path to the output file.
      - `quote` (str, optional): Represents the text you want to translate. If not provided, a key dictionary is generated.

- **Key Interpretation:**
  - `readKeys(filePath)`
    - Interprets keys from a given file.
    - Parameters:
      - `filePath` (str): Path to the file with pre-saved keys.

- **Encryption:**
  - `encripter(quote, outputFile, keys=False)`
    - Encrypts given messages.
    - Parameters:
      - `quote` (str): The text you want to encrypt.
      - `outputFile` (str): Path to save the keys.
      - `keys` (str, optional): Path to a file with pre-saved keys.

- **Decryption:**
  - `decripter(quote, keysPath)`
    - Decrypts a given message.
    - Parameters:
      - `quote` (str): The encrypted text.
      - `keysPath` (str): Path to the file containing the keys.

## Usage
```python
# Example Usage
import Cripter

# Generate keys and save them to a file
keys = Cripter.keyGenerator("output_keys.txt")

# Encrypt a message
quote = "Hello, ThreatForge!"
encrypted_quote = Cripter.encripter(quote, "output_encrypted.txt", keys)

# Decrypt the message
decrypted_quote = Cripter.decripter(encrypted_quote, "output_keys.txt")
print(decrypted_quote)
```



## Contributors

- [Guilherme Soares](https://github.com/Guimbreon)

## License
This ThreatForge Encryption and Decryption Tool is licensed under the MIT. See the [LICENSE](LICENSE) file for details.

