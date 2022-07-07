#7.1
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    line=line.upper()
    print(line)
#7.2
file=input('Name of file?\n')
#fhand = open('mbox-short.txt')
fhand = open(file)
spam=0
count=0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        place = line.find(':')+1
        num=float(line[place:])
        spam=spam+num
        count=count+1
print(spam/count)
#7.3
file=input('Name of file?\n')
if file=='trele morele':
    print('TRELE MORELE - co aq bzdury!')
    quit()
#fhand = open('mbox-short.txt')
fhand = open(file)
count=0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject'):
        count=count+1
print('There are',count, 'messages')
