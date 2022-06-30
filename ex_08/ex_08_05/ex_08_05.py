fname = input("Enter File name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
countline = 0
lst = list()
for x in fh:
    if len(x) < 2 or not x.startswith("From "):
        continue
    s = x.split()
    countline = countline + 1
    print(s[1])

print("There were", countline, "lines in the file with From as the first word")
