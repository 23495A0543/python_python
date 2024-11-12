


#---------------------------------#int-> float------------------------------------------------



b=300
b = float(b)  #float
print(b, type(b))



#----------------------------------------# int-> str----------------------------------------
a = 30
a = str(30) #str
print(a,type(a))









#========================================#str--->int================================


"""   
wwe cannot directly convert str to int 
we convert that first str to float after that convert float to int
"""


srinu = "543"
srinu = int(srinu)
print(srinu)
#str--->float

srinu = "543"
srinu = float(srinu)
srinu = int(srinu)
print(srinu)


#-------------------------------str-->bool---------------------------------
id = "000"
id =bool(id)
print(id)


name = "0"
name=bool(name)
print(name)
"""here non-zeroes or non-empty becomes true
    zero or empty  -------- Flase
"""



