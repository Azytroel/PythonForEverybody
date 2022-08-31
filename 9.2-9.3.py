fhand=open('mbox-short.txt')
days=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From ') : continue
    words=line.split()
    days[words[2]]=days.get(words[2],0)+1
print(days)

#file=input('Enter file name: ')
#fhand=open(file)
fhand=open('mbox-short.txt')
days=dict()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From ') : continue
    words=line.split()
    days[words[1]]=days.get(words[1],0)+1
print(days)
bigemail=None
bigcount=None
smallemail=None
smallcount=None
for email,count in days.items():
    if bigcount is None or bigcount<count:
        bigemail=email
        bigcount=count
    if smallcount is None or smallcount > count:
        smallemail = email
        smallcount = count
emails=list()
for email,count in days.items():
    if count==bigcount and email not in emails:
        emails.append(email)
for email in emails:
    print(email,bigcount)
emails=list()
for email,count in days.items():
    if count== smallcount and email not in emails:
        emails.append(email)
for email in emails:
    print(email, smallcount)

