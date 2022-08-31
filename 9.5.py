fhand=open('mbox-short.txt')
home=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From ') : continue
    words=line.split()
    atpos=words[1].find('@')
    sppos=len(words[1])
    host = words[1][atpos + 1: sppos]
    home[host] = home.get(host, 0) + 1
print(home)