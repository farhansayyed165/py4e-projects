fname = "regex_sum_1128329.txt"
fhand = open(fname)

lst = []
import re
for line in fhand:
    line = line.rstrip()
    stint = re.findall('[0-9]+', line)
    if len(stint) > 1:
        lst.append(stint)
inin = []
for sublist in lst:
    for s in sublist:
        for t in s.split(', '):
            inin.append(int(t))

print(sum(inin))
