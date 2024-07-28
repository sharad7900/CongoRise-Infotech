import random
import string

a = [1,2,3]
random.shuffle(a)
b = a[0]

print("1=Rock\n2=Paper\n3=Scissor\n")
scoreuser = 0
scorecomputer = 0

ask = "Yes"
while ask=="Yes":
    n = int(input("Enter your choice:"))
    if(n==b):
       ask=input("Tie\nYou want to play again?(Yes or No): ")
    elif(n==1 and b==3):
       ask=input("You won!!\nYou want to play again?(Yes or No): ")
       scoreuser +=1
    elif(n==2 and b==1):
        ask=input("You won!!\nYou want to play again?(Yes or No): ")
        scoreuser +=1
    elif(n==3 and b==2):
        ask=input("You won!!\nYou want to play again?(Yes or No): ")
        scoreuser +=1
    else:
        ask=input("You lose!!\nYou want to play again?(Yes or No): ")
        scorecomputer +=1
       
print("\n\nYour Score = ",scoreuser,"\nComputer Score = ",scorecomputer)

    


