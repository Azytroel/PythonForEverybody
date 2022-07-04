total = 0
count = 0
while True:
    inp2 = input('Enter a nubmer until is done: ')
    if inp2 == 'done': break
    try:
        inp = float(inp2)
        if inp2 == 'done': break
    except:
        print('Write a number please.')
    if count==0:
        maximum=inp
        minimum=inp
    elif maximum < inp:
        maximum = inp
    elif minimum > inp:
        minimum = inp

    count = count + 1
    total = total + inp
if count == 0:
    print('Total:0 ')
    quit()
else:
    average = total / count
print('Average:', average, 'and Total:', total)
print('Max:', maximum, 'Min', minimum)
