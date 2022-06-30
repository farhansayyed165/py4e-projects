fname = input("Enter File Name: ")
try:
    fhand = open(fname)
except:
    print("I think the file you are looking for is not there :/")
    quit()
aah = list()
for rl in fhand:
    for i in rl.split():
        if not i in aah:
            aah.append(i)
    aah.sort()


print(aah)
