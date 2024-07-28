choice = "Y"
import random
while choice=="Y": ## if user not want roll more then loop is breaked
    num = random.randint(1,6) ##import any random number from 1 to 6
    if num==1:
        print("\n---------\n|       |\n|   O   |\n|       |\n---------")
        choice = input("You want to roll again? Y/N: ") ## ask every time to user to roll dice or not
    elif num==2:
        print("\n---------\n|O      |\n|       |\n|      O|\n---------")
        choice = input("You want to roll again? Y/N: ")
    elif num==3:
        print("---------\n|O      |\n|   O   |\n|      O|\n---------")          ##checking all conditions and print your dice
        choice = input("You want to roll again? Y/N: ")
    elif num==4:
        print("---------\n|O     O|\n|       |\n|O     O|\n---------")
        choice = input("You want to roll again? Y/N: ")
    elif num==5:
        print("---------\n|O     O|\n|   O   |\n|O     O|\n---------")
        choice = input("You want to roll again? Y/N: ")
    elif num==6:
        print("---------\n|O     O|\n|O     O|\n|O     O|\n---------")
        choice = input("You want to roll again? Y/N: ")