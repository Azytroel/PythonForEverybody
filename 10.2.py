fhand=open('mbox.txt')
domens=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From ') : continue
    words=line.split()
    hour = words[5]
    hours=hour.split(':')
    domens[hours[0]]=domens.get(hours[0],0)+1
lst=list()
for k,v in domens.items():
    lst.append((k,v))
lst=sorted(lst)
for k,v in lst:
    print(k,v)