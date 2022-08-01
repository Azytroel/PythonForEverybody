fhand = open('romeo.txt','r')
words=[]
for line in fhand:
        for word in line.split():
            if word not in words:
                words.append(word)

print(sorted(words))

fhand=open('mbox-short.txt')
count=0
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From ') : continue
    words=line.split()
    email=words[1]
    print(email)
    count=count+1
    pieces=email.split('@')
print(count)
values=list()
while True:
    inp=input('Write a number until is done: ')
    if inp=='done': break
    value=float(inp)
    values.append(value)
print('Max: ', max(values), 'and min: ', min(values))