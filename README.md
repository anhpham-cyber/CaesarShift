# Caesar Cipher Tool

A compact Python Caesar Cipher tool that shifts letters by a user-defined key to encrypt/decrypt messages. Built during FreeCodeCamp Python training—perfect for CTF warmups, red team steganography drills, or blue team labs on classical cipher detection and brute-force attacks
The program allows you to **encrypt or decrypt messages** by shifting letters by a specified number.

---

## Features

- Encrypt messages by shifting letters forward  
- Decrypt messages by shifting letters backward  
- Keeps spaces, numbers, and punctuation unchanged  
- Easy-to-use console interface  
- Allows repeated use without restarting the program  

---

## How It Works

1. The user inputs a message to encrypt or decrypt.  
2. The user provides a **shift number** (how many letters to shift).  
3. The user selects whether to **encrypt or decrypt**.  
4. The program outputs the resulting message.  

The Caesar Cipher works by **shifting each letter** in the alphabet by the shift number.  

For example, with a shift of 3:

a → d

b → e

c → f

## Example Run

Enter your message: hello world

Enter shift number: 3

Encrypt or Decrypt? encrypt

Result: khoor zruog

Do you want to try again? (yes/no): yes

Enter your message: khoor zruog

Enter shift number: 3

Encrypt or Decrypt? decrypt

Result: hello world

Do you want to try again? (yes/no): no

Goodbye!

---

## Requirements

- Python 3.x  
- No external libraries required  

---

## Notes

- The program only shifts **alphabetic characters**. All other characters remain the same.  
- Shift numbers can be larger than 26; the program wraps around the alphabet automatically.  
- This is a beginner-friendly project to practice **loops, conditionals, and string manipulation** in Python.  

---

## Future Improvements

- Add support for **uppercase letters** while preserving case  
- Add a **GUI interface** for easier use  
- Allow **reading from and writing to files** for encryption/decryption  

---

