# lambda  -> anonymous function
def wish(name):
    return f"Hey {name}, Happy Coding"
print(wish("sachin"))
print(wish("virat kholi"))

wishing = lambda name:f"Hey {name}, Happy Coding"
print(wishing("sachin"))
print(wishing("virat kholi"))


def addition(n1, n2):
    return n1 + n2
print(addition(10, 20))

addition = lambda n1, n2: n1 + n2
print(addition(10, 20))



"""  scope
        recursion 
       generator
  
  """ 
def sequence(n):
    if n < 0:
        return n
    print(sequence(n-1))
sequence(5)