text = "X-DSPAM-Confidence:    0.8475";
x = text.find(':')
spacenum = text[x+1:]
spacenum.strip
num = float(spacenum)
print(num)

     



#num = (text[23:])
#print(num)
