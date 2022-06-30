largest = None
smallest = None
d = dict()

while True:
    user = input("Enter Number: ")

    if user == ("done" or "Done"):
        break

    try:
        num = int(user)

    except:
        print("Please Enter Numeric Input: ")
        continue
    d[]






#    if smallest is None:
#        smallest = num
#
#    elif num < smallest:
#        smallest = num
#
#    if largest is None:
#        largest = num
#
#    elif num > largest:
#        largest = num


print("Maximum is: ", largest)
print("Minimum is:", smallest)
