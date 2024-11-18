"""
16. Repeatedly asks for user input until they type "quit" (use while loop).
while True:
 user =input()
 if user == "quit":
    break
print(user)    
"""


"""
h/w: Repeatedly asks for user input until they type "quit" or "QUIT" or "Quit" (use while loop). 

"""
while True:
    name =input()
    name = name.lower()
    if name == "quit":
        break
    print(name)