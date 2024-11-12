
srinu ={"name":"srinu"},{"branch":"CSE"}
print(srinu)

 

"""
 dictionary -> {}, mutable, unordered, unique
--> cannot use mutable data types as key in dictionary
--> keys can be any data types
--> duplicates are not allowed
"""
details = {}
details["name"] = "suresh Raina"
details[1001] = "id" 
details[("city",)] = "UP"
details[frozenset({"city", "state"})] = ["usa", "UP"]
print(details[1001])
for key in details:
     print(f"{key} -> {details[key]}") 

print()

for key, value in details.items():
    print(f"{key} -> {value}")

details.pop("name")
print(details)