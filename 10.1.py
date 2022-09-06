fhand=open('mbox.txt')
domens=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From ') : continue
    words=line.split()
    email = words[1]
    domens[email]=domens.get(email,0)+1
lst=list()
for k,v in domens.items():
    lst.append((k,v))
print(sorted(lst, reverse=True))
lst=sorted(lst,reverse=True)
print(lst[0])
