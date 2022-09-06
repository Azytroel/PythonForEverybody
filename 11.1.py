import re

phrase=input("What you want find? ")
#file=input("Which file? ")
num=0
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if re.search(phrase, line):
        num=num+1
print(num)