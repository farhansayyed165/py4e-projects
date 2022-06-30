fhand = input("Enter File name: ")
try:
    open(fhand)
except:
    print("There is no such file:", fhand)
    quit()

countline = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        x = line.find(':')
        a = float(line[x+1:])
        total = float(total) + float(a)
        countline = countline + 1


avg = float(total/countline)
print("Average spam confidence:",avg)
