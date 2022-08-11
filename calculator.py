from art import logo

def add (n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 /n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

def calculator():
  print(logo)
  num1 = float(input("First number: "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  while should_continue:
    chosen_operation = input("What operation do you want to use? ")
    num2 = float(input("Next number: "))
    calculation = operations[chosen_operation]
    answer = calculation(num1, num2)
    print(f"{num1} {chosen_operation} {num2} = {answer}")
  
    if input(f"type 'y' if you want to continue with {answer}, or type 'n' to start again: ") == "y":
      num1 = answer
      should_continue = True
    else:
      should_continue = False 
      print("end")
      calculator()

calculator()