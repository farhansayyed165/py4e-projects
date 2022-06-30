hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")



try:
    hf = float(hrs)
except:
    hf = -1
    print ("The data entered might not be in a number or type it in digits")
    quit()
try:
    rf = float(rate)
except:
    rf = -1
    print ("The data entered might not be in a number or type it in digits")
    quit()



if hf > 40:
    oh = (hf - 40)
    print ("Overtime:", oh)
    opay = oh * (rf * 1.5)
    fop = opay + (40 * rf)
    print ("Overtime + Payment:", fop)
if hf <= 40:
     print("Regular;")
     rpay = (hf * rf)
     print("Payment:", rpay)
