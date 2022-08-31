#file=input('Enter file name: ')
#fhand=open(file)
fhand=open('mbox-short.txt')
domens=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From ') : continue
    words=line.split()
    email = words[1]
    pieces = email.split('@')
    domens[pieces[1]]=domens.get(pieces[1],0)+1
largest = None
smallest=None
namesL=list()
namesS=list()
for email in domens:
    if largest is None or domens[email] > largest:
        largest = domens[email]
        nameL=email
for email in domens:
    if largest==domens[email] :
        namesL.append(email)
for email in domens:
    if smallest is None or domens[email] <smallest:
        smallest = domens[email]
        nameS=email
for email in domens:
    if smallest==domens[email]:
        namesS.append(email)

print('Max:',namesL, largest)
print('Min:',namesS, smallest)
print(domens)