hrs = input("Enter Hours: ")
rt = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rt)
except:
    print("Please, Enter Numeric Input")
    quit()

def computepay(hours,rate):
    if hours <= 40:
        print ("Regular")
        rot = hours * rate
        print ("Payment: ", rot)
    if hours > 40:
        oh = hours - 40
        print("Overtime:", oh)
        opay = oh * (rate * 1.5)
        fpay = opay + (40 * rate)
        print ("Payment: ", fpay)


p = computepay(h,r)
print = (p)
