from replit import clear

from art import logo
print(logo)
#ADD
def add(n1, n2):
  return n1 + n2
#SUB
def sub(n1,n2):
  return n1 - n2
#MUL 
def mul(n1,n2):
  return n1*n2
#DIV
def div(n1,n2):
  return n1/n2
operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}
def calculator():
  clear()
  num1 = float(input("Enter the first number\n"))
  for symb in operations:
    print(symb)
  should_continue = True
  while should_continue:
    operation_symb = input("Pick an operation: ")
    num2 = float(input("Enter the next number\n"))
    calculation_fun = operations[operation_symb]
    answer = calculation_fun(num1,num2)
    print(f"{num1} {operation_symb} {num2} = {answer}")
    if (input(f"Choose 'y' to calculate with {answer} 'r' to restart : ")).lower() == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
      
calculator()
  
  
