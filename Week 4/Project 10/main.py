import os,sys

def run():
        confirmation = int(input("You have selected reverse string encryption\nCaution, Don't use too large of strings, the program isn't meant to handle that\n Would you like to: \n 1) Encrypt \n 2) Decrypt\n 3) Brute Force\n"))
        if confirmation == 1:
            encrypt(input("Enter string to encrypt:\n"))
        elif confirmation == 2:
            decrypt(input("Enter string to decrypt:\n"))
        elif confirmation == 3:
            bruteForce(input("Enter string to brute force:\n"))
        else:
            print("Invalid input, try again")       
        
def encrypt(message):
    key = int(input("What is the key? (Shift integer)\n"))
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_+{}|:"<>?~`-=[]\\;\',./'
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex= translatedIndex + len(SYMBOLS)
                
            translated= translated + SYMBOLS[translatedIndex]

        else:
                translated = translated + symbol
    print(translated)
        
def decrypt(message):
    
    key = int(input("What is the key? (Shift integer)\n"))
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_+{}|:"<>?~`-=[]\\;\',./'
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            
            translatedIndex = symbolIndex - key
            
            if translatedIndex>= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex<0:
                translatedIndex= translatedIndex + len(SYMBOLS)
            translated= translated + SYMBOLS[translatedIndex]

        else:
                translated = translated + symbol
    print(translated)
    
def bruteForce(message):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_+{}|:"<>?~`-=[]\\;\',./'
    translatedPossibilities = []
    ogmessage = message
    
    for i in range(0,len(SYMBOLS)):
        message = ogmessage
        possibility=''
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex=SYMBOLS.find(symbol)
                
                translatedIndex=symbolIndex - i
                
                if translatedIndex>= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                
                elif translatedIndex<0:
                    translatedIndex= translatedIndex + len(SYMBOLS)
                     
                possibility= possibility + SYMBOLS[translatedIndex]
        translatedPossibilities.append(possibility)
        
    x = int(input("Would you like to search for english matches?\n1:Yes\n2:No\n"))
    if x == 1:
        for i in translatedPossibilities:
            i=i.split(" ")
            if checkCipher(i):
                print("Possible decryption:\t",i)
    if x ==2:
        for i in translatedPossibilities:
            print(i)
    
def checkCipher(cipher):
    #Split string into words, check individual words against dict
    with open("words.txt") as dict:
        for i3 in range(len(cipher)): #breaks cipher into each word
            cipher[i3]=cipher[i3].lower().strip()
            
            for n in dict: #each word in dict
                n=n.lower().strip()
                if (cipher[i3] == n):
                    return True
                    break
            
                
            
                  
    
run()
'''
F-EFWF-EF\/[WF-EF'''