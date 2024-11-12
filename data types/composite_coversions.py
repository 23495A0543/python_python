#composite type conversions'
 #----------------------list--> tuple------------------------------------

list =[1,3,5,7,9]
list=tuple(list)
list =set(list)

print(list,type(list))


   #---------------------------------------list-->dict---------------------------------------------
details = [("name","srinu"),["branch","CSE"]]
details = dict(details)
print(details)