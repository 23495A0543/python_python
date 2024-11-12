       
# while loop
name = "python"
current = 0
while current < len(name):
    print(name[current], current)
    current += 1
print("===================================")
name = "python"
current = len(name)-1
while current >= 0:
    print(name[current], current)
    current -= 1