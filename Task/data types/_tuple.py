names =("srinu","karthik",)
print(names[1]) 
print(names)


# # tuple (), ordered, immutable
# arr = ("code",1, 1, 2, 3)
# print(arr.count(1))
# print(arr)

data = [(1, "srinu", "USA"), (2, "srinu", "USA")]
srinu_cnt = 0
for bio in range(len(data)):
    if data[bio][1] == "srinu":
        srinu_cnt += 1
print(srinu_cnt)




data = [(1, "srinu", "usa"), (2, "ram", "america")]
for user in range(len(data)):
    print(data[user][0]) # (1, 'srinu,'usa')
    
    
    
    data = [
    (1, "david warner", "australia", 100000), 
    (2, "ab de viliers", "south africa", 50000),
    (12, "kl rahul", "india", 200),
    (10, "ms dhoni", "india", 4000)
	]
data.sort(key=lambda x:x[2], reverse=True)
for user in range(len(data)):
    print(*data[user])