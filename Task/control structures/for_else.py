

# for-else
for i in range(5):
    data = int(input("Enter Number: "))
    if data < 0:
        print("Negatives Entered, Terminating Entire Loop")
        break
else:
    print("No Negative values Entered")
