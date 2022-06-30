name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
bige = None
bigcount = None
for line in handle:
    if not line.startswith("From"):
        continue
    i = line.split()
    email = i[1]
    d[email] = d.get(email,0) + 1

for k, v in d.items():
    if bigcount is None:
        bigcount = v
        #print("None", bigcount , bige)
    elif bigcount < v:
        bigcount = v
        bige = k
        #print("small", bigcount , bige)
print(bige)
