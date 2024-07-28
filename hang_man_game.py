name=input("Enter your name: ")
print("\nGood luck!  ",name,"\n")

words = ["ban","generate","page","implicit","training","episode","gradual","pyramid","chart","motif"]

import random

word = random.choice(words)

tries = 10
guess = ''

while tries>0:
    
    length = 0
    
    for char in word:
        if char in guess:
            print(char,end=" ")
        else:
            print("_")
            length +=1
        
    if length==0:
        print("\nYou Won!!\nWord is: ",word)
        break
    choice = input("Enter a character: ")
    if choice in word:
        guess+=choice
    else:
        tries-=1
        print("Wrong choice!! You have ",tries," tries")
        
    if tries==0:
        print("You loose")
    
    
    
    
    
