a = 1
s = 0
print ('Enter Numbers to add to the sum.')
print ('Enter 0 to quit.')
while a != 0:
    print ('Current Sum: ', s)
    a = input('Number? ') #raw_input() will not work anymore.
    a = float(a)
    s += a
print ('Total Sum = ',s)
