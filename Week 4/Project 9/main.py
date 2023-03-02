def run():
        confirmation = int(input("You have selected Reverse string encryption\n Would you like to: \n 1) Encrypt \n 2) Decrypt\n 3) Brute Force\n"))
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
                   
    for i in translatedPossibilities:
        print(i)
    
run()

#Myxq1k32_)iy4)m1kmuon)wo