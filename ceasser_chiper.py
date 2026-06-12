alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt():
    encryptedText = ""
    for i in range(len(msg)):
        if msg[i] not in alphabets:
            encryptedText = encryptedText + msg[i]
        for j in range(26):
            if msg[i] == alphabets[j]:
                encryptedText += alphabets[(j+shift) % 26]
    return encryptedText

def decrypt():
    decryptedText = ""
    for i in range(len(msg)):
        if msg[i] == " ":
            decryptedText = decryptedText + " "
        for j in range(26):
            if msg[i] == alphabets[j]:
                decryptedText += alphabets[(j - shift) % 26]
    return decryptedText

while quit != "n":

    code = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    msg = input("enter the message:\n").lower()
    shift = int(input("Enter the shift value:\n"))
    quit = "y"

    if code == "encode":
        print(encrypt())
    else:
        print(decrypt())
    quit = input("Do you want to repeat it(Y/n)?\n").lower()