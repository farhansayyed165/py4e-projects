largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == ('done'):
        break
    try:
        realnum = int(num)
    except:
        print('Input Numeric Input Please.')
        continue
    if smallest is None:
        smallest = realnum
    if realnum < smallest:
        smallest = realnum
    if realnum > smallest:
        realnum = smallest  

    if largest is None:
        largest = realnum
    if realnum > largest:
        largest = realnum
    elif realnum > smallest:
        realnum = largest



print('Maximum is', largest)
print('Minium is', smallest)
