def add(a,b):
      return a+b

def multiply(a,b):
      return a*b

def subtract(a,b):
      return a-b

def divide(a,b):
      if(b==0):
            return ("Division is not possible")
      return a/b

def Calculator():
      print("Select your operation: ")
      print("1-> Add")
      print("2-> Subtract")
      print("3-> Multiply")
      print("4-> Divide")
      
      while True:
            choice = input("Enter your choice(1,2,3,4): ")
      
            if choice in ['1','2','3','4']:
                  try:
                     num1 = float(input("Enter a number: "))
                     num2 = float(input("Enter a number: "))
                  except ValueError:
                        print("Invalid input. Wrong inputs")
                        continue
            
                  if choice == '1':
                        print(f"{num1} + {num2} = {add(num1,num2)}")
                  elif choice == '2':
                        print(f"{num1} - {num2} = {subtract(num1,num2)}")
                  elif choice == '3':
                        print(f"{num1} * {num2} = {multiply(num1,num2)}")
                  elif choice == '4':
                        print(f"{num1} / {num2} = {divide(num1,num2)}")
                  
                  
                  next = input("Is another calculation you want?")
                  if next.lower() != 'yes':
                        break
            else:
                  print("Invalid input. Please select a valid operation.")
            
            
            
if __name__ == "__main__":
      Calculator()
            
                        
