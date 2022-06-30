fname = input("Enter File Name: ")
if len(fname) < 1: fname = "regex_sum_42.txt"
fhand = open(fname)
lst = list()
import re
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if not len(stuff) < 1:
        lst.append(stuff)

print(lst)

flst = []
inner = []
for sublist in lst:
    for s in sublist:
        for t in s.split(', '):
            inner.append(int(t))



print(sum(inner))
