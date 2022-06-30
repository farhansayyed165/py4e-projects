name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di = dict()
count = None
wordcount = None

for z in handle:
    if not z.startswith("From"):
        continue
    w = z.split()
    email = w[1]
    di[email] = di.get(email,0) + 1
    print(di)

for aa,bb in di.items():
    if count is None:
        count = bb
        wordcount = aa
        #print(aa,bb)
    if bb > count:
        count = bb
        wordcount = aa
        #print(aa,bb)

print(wordcount, count)
print(di)
