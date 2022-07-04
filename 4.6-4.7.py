#4.6
def computepay(hours, r):
    if hours > 40:
        paycheck = (hours - 40) *r*1.5+40*r
    else:
        paycheck = hours * r
    return(paycheck)
try:
    hours = float(input('How many hours? '))
    r = float(input('How much money per hour? '))
except:
    print('Write a number please.')
print(computepay(hours, r),'\n')
#4.7
def computergrade(value):
    if value>=0.9:
        print('Your mark is 5.0')
    elif value>=0.8:
        print('Your mark is 4.5')
    elif value>=0.7:
        print('Your mark is 4.0')
    elif value>=0.6:
        print('Your mark is 3.5')
    elif value>=0.5:
        print('Your mark is 3.0')
    else:
        print('Your mark is 2.0')
try:
    value=float(input('Write value from 0 to 1\n'))
except:
    print('Write a number.')
if value>1 or value<0:
    print('You are out of scope, write again')
    quit()
computergrade(value)