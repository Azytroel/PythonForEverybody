name=input('What is your name?')
print('Hello', name )

hours=float(input('How many hours? '))
r=float(input('How much money per hour? '))
if hours > 40:
    paycheck = (hours - 40) * r * 1.5 + 40 * r
else:
    paycheck = hours * r
print('Your paycheck ',paycheck)

width=17
height=12.0
print(width//2)
print(type(width//2))
print(width/2.0)
print(type(width/2.0))
print(height/3)
print(type(height/3))
print(1+2*6)
print(type(1+2*6))

temp=float(input('What is temperature in Celsius?'))
print('Temperature in fahrenheit ',temp *1.8+32)