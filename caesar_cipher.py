
def caesar_cipher ():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    while True:
        result = ""
        text = input("Enter your message: ").lower()
        shift = int(input("Enter shift number: "))
        mode = input ("Encrypt or Decrypt? ").lower()

        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                if mode == "encrypt":
                    new_index = (index + shift) % 26
                elif mode == "decrypt":
                    new_index = (index - shift) % 26
                else:
                    print("Invalid, please select encrypt or decrypt!")
                    result = ""
                    break
                result += alphabet[new_index]
            else: 
                result += char

        if result:
            print("Result: ", result)

        while True:
            again = input("Do you want to try again? (yes/no): ").lower()
            if again == "yes":
                break
            elif again == "no":
                print("Goodbye!")
                return
            else:
                print("Invalid input, please enter 'yes' or 'no' only.")
        

def main():
    caesar_cipher ()

if __name__ == "__main__":
    main()