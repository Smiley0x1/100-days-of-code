money = 0

x = int(input("How much will you put away biweekly?\n"))
for i in range(0, 43):
    for n in range(0,26):
        money+=x
        money*=1.0027
    
print("You'll be",i+18,"and have",int(money))