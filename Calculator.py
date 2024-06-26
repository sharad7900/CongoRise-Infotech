operator = input("Enter which operation you want:")

num1 = int(input("\nEnter 1st value: "))
num2 = int(input("\nEnter 2nd value: "))

if(operator=='+'):
      print("\n\nAnswer is:",num1+num2)
elif(operator=='-'):
      print("\n\nAnswer is:",num1-num2)
elif(operator=='*'):
      print("\n\nAnswer is:",num1*num2)
elif(operator=='/'):
      print("\n\nAnswer is:",num1/num2)
else:
      print("Wrong input!")