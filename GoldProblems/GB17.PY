"""
17. Repeatedly asks for user input until they type "quit". (use while loop). 
    if they enter digit, print the numbers from 1 to n(user entered digit).
"""

while True:
   user =input("enter:")
   if user == "quit":
       break 
   if user.isdigit():
       n = int(user)
       for i in range(1,n+1):
        print(i)
        
        
 