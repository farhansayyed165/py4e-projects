score = input("Enter Score: ")

# try and except for str
try:
    s = float(score)
except:
    print("Error, Please enter Numeric Input")
    quit()

# remove try and except and add if <s>
if 0 < s > 1.0:
    print("Error, Please enter correct Numeric Input")
    quit()


# grading system
if 0.9 <= s <= 1.0:
    print("A")
    quit()

if 0.8 <= s <=0.9:
    print("B")
    quit()

if 0.7 <= s<= 0.8:
    print("C")
    quit()

if 0.7 <= s <= 0.6:
    print("D")
    quit()

if s < 0.6:
    print("F")
    quit()
