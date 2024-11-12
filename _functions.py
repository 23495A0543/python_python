# non-return function & parameterized function
def welcome(name, bank):
    print(f"Hello {name}, Happy {bank} Banking")

welcome("Nick", "Paypal")
welcome("Rasool", "Hdfc")
welcome("Akash", "CANARA")
welcome("Anil", "ICICI")

print("-----------------------------------")

# return function & parameterized function
def welcome(name, bank):
   return f"Hello {name}, Happy {bank} Banking"

print(welcome("Dhanjay", "Paypal"))
print(welcome("Mouneesh", "Hdfc"))
print(welcome("Swaroop", "CANARA"))
print(welcome("Varma", "ICICI"))

print("-----------------------------------")




# non-parametrized function & return function
def oneToFive():
  for i in range(1, 6):
    print(i)
  return "done"

print(oneToFive())


# non-parametrized function & non-return function
def oneToFive():
  for i in range(1, 6):
    print(i)

oneToFive() 






# *args
def numbers(a, *args):
    print(f"Numbers are {a}, {args}")

print(numbers(10, 20, 30, 40))
numbers(30, 40)



    
    