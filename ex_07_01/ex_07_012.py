# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#try:
#    open(fname)
#except:
#    print("error")
#    quit()



totalfloat = 0
countline = 0
fh = open("mbox-short.txt")
for line in fh:
    line == line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x=line.find(":")
    flot = float(line[x+1:])
    totalfloat = totalfloat + flot
    countline = countline + 1



print("Average X-DSPAM-Confidence:", totalfloat/countline)
