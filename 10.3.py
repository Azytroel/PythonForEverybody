fhand=open('mbox.txt')
import string
letterD=dict()
alphabet='abcdefghijklmnopqrstuvwxyz'
for line in fhand:
    line=line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words=line.split()
    for word in words:
        letters=word.split()
        for c in letters:
            for d in c:
                if d in alphabet:
                    letterD[d] = letterD.get(d, 0) + 1
lst=list()
sum=0
b=0
for k,v in letterD.items():
    lst.append((k,v))
    b=v
    sum=sum+b
lst=sorted(lst)

for k,v in lst:
    print(k,v,round(v/sum,3 ))