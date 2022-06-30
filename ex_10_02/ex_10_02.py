fname = input("Enter Filename: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)
di = dict()
lst = []
for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        hr = words[5].split(':')
        di[hr[0]] = di.get(hr[0],0) + 1
    else:
        continue
for k , v in di.items():
    lst.append((k,v))
lst.sort()
for k,v in di.items():
    print(k ,v)
