import re
import math

fhand = open('mbox.txt')
#file=input("Which file? ")
num=[]
for line in fhand:
    match = re.search("New\sRevision:\s(\d+)", line)
    if match:
        num.append(int(match.group(1)))
print(math.trunc((sum(num)/len(num))))
