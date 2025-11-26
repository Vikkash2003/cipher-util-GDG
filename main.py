def main():
    try:
        keyword = getValidInput("Enter keyword for Encryption: ")
        keyword = keyword.upper()
        
        use_keyed = input("Use keyed alphabet for Vigenere Table? (y/N): ").strip()
        if use_keyed.upper() == 'Y':
            while True:
                vKeyword = getValidInput("Enter keyword for Vigenere Table: ")
                vKeyword = vKeyword.upper().replace(" ", "")
                if not hasDuplicateLetters(vKeyword):
                    break
                print("Keyword cannot contain duplicate letters. Please try again.")
            vTable = createVigenereTable(vKeyword)
        else:
            vTable = createNormalVigenereTable()
        
        vdict = createDict(vTable[0])
        
        try:
            while True:
                choice = input("Encrypt or Decrypt? (E/D): ").upper()
                if choice == 'E':
                    plaintext = getValidInput("Enter plaintext: ").upper()
                    ciphertext = encrypt(plaintext, keyword, vTable, vdict)
                    print("Ciphertext: ", ciphertext.lower())
                # elif choice == 'D':
                #     ciphertext = getValidInput("Enter ciphertext: ").upper()
                #     plaintext = decrypt(ciphertext, keyword, vTable, vdict)
                #     print("Plaintext: ", plaintext.lower())
                elif choice == "EXIT":
                    break
        except KeyboardInterrupt:
            print("\nExiting...")
            raise
    except KeyboardInterrupt:
        print("\nExiting...")
        raise

def encrypt(plaintext, keyword, table, dict):
    ciphertext = ""
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper()
    for key in plaintext:
        ciphertext += table[dict[key]][dict[keyword[0]]]
        keyword = shiftKeyword(keyword, 1)
    return ciphertext


def shiftKeyword(keyword, shift):
    shiftedKeyword = keyword[shift:] + keyword[:shift]
    return shiftedKeyword



def createVigenereTable(keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper()
    for letter in keyword:
        alphabet = alphabet.replace(letter, "")
    alphabet = keyword + alphabet
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return table

def hasDuplicateLetter(text):
    seen = set()
    for char in text:
        if char in seen:
            return True
        seen.add(char)
    return False

def createNormalVigenereTable():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []
    for i in range(26):
        table.append(alphabet[i:] + alphabet[:i])
    return 
    
def validateInput(text):
    for char in text:
        if not (char.isalpha() or char == ' '):
            return False
    return True

def getValidInput(prompt):
    while True:
        try:
            user_input = input(prompt)
            if validateInput(user_input)
                return user_input
            print("CAREFUL:For the keyed alphabet, you need a word that doesn't contain duplicate letters. ")
        except KeyboardInterrupt:
            print("\nExiting...")
            raise




if __name__ == "__main__":
    main()
