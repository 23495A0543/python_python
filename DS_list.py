







'''
data structures
  -list
	-index
	-slicing
	-in, not in
	-len
	-count
	-modify
	-append
	-extend
	-insert
	-pop
	-remove
	-concatenate
	-multiply list with scalar
	-max
	-min
	-sum
	-reverse
	-list conversion
	-unpacking
	-enumerate
	-sort(asc, dec)
	-sorted
	-list comparision
	-copy
	-nested lists

'''

names = []
print(f"After initializing names: {names}\n")

names.append("virat kholi")
print(f"After appending 'virat kholi': {names}\n")

names.append("Rohit sharma")
print(f"After appending '': {names}\n")

names.insert(1, "Raina")
print(f"After inserting 'Raina' at index 1: {names}\n")

deleted_name = names.pop()  # you can store popped element
print(f"After popping last element '{deleted_name}': {names}\n")

names.append(deleted_name)
print(f"After appending popped element '{deleted_name}': {names}\n")

names.remove("virat kholi")
print(f"After removing 'virat kholi': {names}\n")


names.insert(2, "Bumrah")
print(f"After inserting 'Bumrah' at index 2: {names}\n")

print(f"Last two elements: {names[-2:]}\n")

print(f"'sachin' in names: {'sachin' in names}\n")

names[2] = names[2].upper()
print(f"After converting index 2 to uppercase: {names}\n")

names.extend(["sachin"])
print(f"After extending with ['sachin']: {names}\n")

names.append(['srinu', 'ms dhoni', 'sachin'])
print(f"After appending ['srinu', ' ms dhoni', 'sachin']: {names}\n")

req = names[-1]
names.pop()
print(f"After popping the last list: {names}\n")

names = names + req 
print(f"After concatenating names & req: {names}\n")

print(f"List created with [0, 1]*5: {[0, 1]*5}\n")

names.sort(reverse=True)
print(f"Descending Order: {names}\n")

names.sort()
print(f"Ascending Order: {names}\n")

print(f"Sum of [1, 2, 3, 4]: {sum([1, 2, 3, 4])}\n")

name = ("CodeWala",)
print(f"List created from tuple: {list(name)}\n")






bio = ["1001", "steeve", "brooklyn"]
_id, *rest = bio
print(f"Remaining elements after unpacking bio: {rest}")