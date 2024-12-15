# ThreatForge Encryption and Decryption Tool

## Overview
This Python module, developed by ThreatForge, provides functionalities for encryption and decryption of text. It includes key generation, key interpretation, encryption, and decryption processes.
___
## How does the encryption work in the v1

The ThreatForge Encryption and Decryption Tool utilizes a symmetric substitution cipher technique combined with a randomized key generation process to ensure secure message handling. Here's a step-by-step breakdown of the encryption process:

1. **Key Generation**:
    
    - For each unique character in the input text (or a predefined symbol set if no text is provided), a unique random key is generated.
    - Each key is a 5-character string, randomly selected from a pool of symbols (`string.ascii_letters`, digits, punctuation, and accented letters).
    - These keys are stored in a key dictionary, mapping each symbol to its unique encrypted counterpart. The dictionary can either be generated dynamically or read from a saved file.
2. **Text Encryption**:
    
    - Each character in the input text is replaced with its corresponding key from the key dictionary.
    - The keys are reversed (mirrored) during this process for added obfuscation.
3. **Message Reordering**:
    
    - The encrypted text is further rearranged to increase security. While currently each character remains in sequence, a placeholder loop ensures flexibility for future enhancements in rearranging the encrypted symbols.
4. **Output**:
    
    - The encrypted message is returned as a secure string that can only be decrypted with the same key dictionary.

### Example Workflow:

1. **Key Generation**:
    
    - Input Text: `Hello`
    - Generated Key Dictionary (Sample):
        
        ```
        H : aXb3Q
        e : k@Z2L
        l : q*JvP
        o : W#1eF
        ```
        
    - Saved to a specified file.
2. **Encryption**:
    
    - Input Text: `Hello`
    - Step 1: Substitute Characters with Reversed Keys: `Q3bXaL2ZkPvJ*qF1#W`
    - Step 2: (Optional Future Step) Rearrange for More Security.
    - Output Encrypted Text: `Q3bXaL2ZkPvJ*qF1#W`
3. **Decryption**:
    
    - Input Encrypted Text: `Q3bXaL2ZkPvJ*qF1#W`
    - Reverse the Process Using the Same Key Dictionary:
        - Reverse Key Lookup and Text Decoding.
    - Output Decrypted Text: `Hello`

The encryption process is robust, leveraging randomness and symbol diversity to reduce predictability, making it resistant to brute-force and frequency analysis attacks.



___
## Usage

```python
# Example Usage

import Cripter

# Encrypt a message

quote = "Hello, ThreatForge!"

encrypted_quote = Cripter.encrypt(quote, "output_encrypted.txt", "output_keys.txt")

# Decrypt the message

decrypted_quote = Cripter.decrypt(encrypted_quote, "output_keys.txt")

print(decrypted_quote)
```

___

