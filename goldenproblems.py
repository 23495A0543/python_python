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
    '''
  
n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2nd number:"))
cond1 = (n1+n2)>100
cond2 = (n1%10==0) or (n2%10==0)
print(cond1 or cond2)

"""
h/w: Take three inputs, 
	check if their sum is greater than 100 or if one of them is divisible by 10.

"""

n1 = int(input("enter 1st number:"))
n2 = int(input("enter 2rd number:"))
n3 = int(input("enter 3rd number:"))
cond1 = (n1+n2)>100
cond2 = (n1%10==0) or (n2%10==0)
print(cond1 or cond2)