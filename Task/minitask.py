
""" 
data = [[1001, "steeve", ["brooklyn", "USA", ["captain america"]]]]
extract the captain america from the data and print it in uppercase

OUTPUT:- 
  CAPTAIN AMERICA
"""



data = [[1001, "steeve", ["brooklyn", "USA", ["captain america"]]]]
data = (data)
m = str(data[0][2][2])
print(type(data))
n = m.upper()
print(*n)
























#print(type(m.upper()))

