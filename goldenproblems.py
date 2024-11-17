""" 
1. Take two inputs, 
	check if their sum is greater than 100 or if one of them is divisible by 10.
"""
'''
num1 =int(input("Enternumber:"))
num2 =int(input("Enternumber:"))
for i in range (num1,num2):
    if num1 + num2 >100 :
    elif num1 % 10 or num2 % 10:
      print(True)
         
else:
    print(False)
    
  
n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2nd number:"))
cond1 = (n1+n2)>100
cond2 = (n1%10==0) or (n2%10==0)
print(cond1 or cond2)
'''
"""
h/w: Take three inputs, 
	check if their sum is greater than 100 or if one of them is divisible by 10.



n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2nd number:"))
n3 = int(input("enter 3rd number:"))
cond1 = (n1+n2)>100
cond2 = (n1%10==0) or (n2%10==0)
print(cond1 or cond2)



2. Take two inputs
	check if both of the numbers are even, both are odd, 
    one is even and other is odd.


n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2nd number:"))
if n1 % 2==0 and n2 %2==0:
         print("Both are even")
elif n1 % 2 !=0 and n2 % 2 !=0:
         print("Both are odd")
         
else:
         print("one is even other one is odd")

"""


""" 
h/w: Take two inputs, check if both of the numbers 
    are even and divided by 5, 
    both are odd and divided by 5, 
    or one of each divided by 5.

n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2nd number:"))
n3 = int(input("enter 3rd number:"))



"""

""" 
3. Take one input
	Increase it by 10, multiply it by 2, and divide it by 5. Print the final result.


num = 6
num += 10
num *=2
num //=5
print(num)



h/w: Take one input
	Power it with 5, subtract it with 0. Print the final result.
number =2
number **=5
number -=0
print(number)

"""

""" 
4. Print numbers from 1 to 10 using a loop.


for i in range (1, 11):
 print(i)
 
 
 

h/w: print numbers from 10 to 1.
"""
 
'''
for srinu in range(10,0,-1):
 print(srinu)
'''

"""
5. Create an empty list and store from 1 to 10 and print it.
arr =[]
for i in range (1,11):
    
  arr.append(i)
print(arr)
"""
"""
h/w: Create an empty list and store from 10 to 1 and print it.

arr=[]
for i in range(10,0,-1):
    arr.append(i)
    
print(arr)  
"""


""" 
6. Take two inputs from the user (both numbers), 
        print their sum, difference, and product.

n1 =int(input("enter 1st number:"))
n2 =int(input("enter 2nd number:"))
print(n1+n2)
print(n1-n2)
print(n1*n2)

"""
""" 
h/w: Take two inputs from the user (both numbers),
        print their sum + difference + product


n1 =int(input("enter 1st number:"))
n2 =int(input("enter 2nd number:"))
a =(n1+n2) +(n1-n2)+(n1*n2)
print(a)
"""

"""
7. Given two variables a and b, swap their values using a temporary variable 
a = 10
b = 20
print("Before swap:",a,b)
c = a
a = b
b = c
print("after swap:",a,b)

"""


"""
h/w: print the id() of both variables before and after swapping.
a = 10
b = 20
print("Before swap:",a,b)
print("ID of a Before swap:",id(a))
print("ID of b Before swap:",id(b))

c = a
a = b
b = c
print("after swap:",a,b)
print("ID of a after swap:",id(a))
print("ID of b after swap:",id(b))

"""
""" 
8. Take a string input, print the first and last character.

n = input("entername:")
m= (n[0],n[-1])
print(m)


h/w: Take a string input, print the second and second last character.

n = input("entername:")
m= (n[1],n[-2])
print(m)

"""
"""
9. Take a multi-line string input(not user input) and
    store it in a variable using triple quotes.
"""

#a = """This is a SRINIVAS Developer"""
#print(a)



"""
h/w: Take a multi-line string input
        print the length of it after storing in variable using triple quotes.

"""
#a = """This is a SRINIVAS Developer"""
#print(len(a))


""" 
10. Concatenate two strings and print their lengths.
a = "srinu"
b = "ram"
c = a+b
print(len(c))
"""

"""
11. Take a sentence from the user, reverse words and print it.
Example: Input: "Hello World" → Output: "World Hello"

sentence = "this is srinu developer".split()
print(sentence)
print(" ".join(sentence[::-1]))
"""

"""
h/w: Take a sentence from the user, 
reverse the words and print along with - between each word.
Example: Input: "Hello World" → Output: "World-Hello"
"""

""" 
12. Take a string input
	convert it to uppercase, and 
    replace all occurrences of the letter 'A' with 'X'.


name = "srinivas"
name =name.upper()
name =name.replace('A','X')
print(name)


h/w: Take a string input
	Replace all lowercase 'a' with 'A'

user =input("entername:")
user =user.lower()
user =user.replace('a','A')
"""

"""
13. Take a sentence, print only non-alpha and non-digit characters.
sentence="srinivas18@gmail.com"
for i in range (len(sentence)):
    charater =sentence[i]
    if not charater.isalpha() and not charater.isdigit():
        print(charater)
"""

"""
h/w: Take a sentence, store alphabets and digits in separate lists.
"""
arr=[]
user = "power1star@gmail.com.co"
for letter in range (len(user)):
    char=user[letter]
    if char.isalpha() :
        arr.append(char)
        print(list(char))
    elif char.isdigit():
        print(list(char))