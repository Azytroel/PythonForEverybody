#1
fruit = 'banan'
index = len(fruit) - 1
while index != -1:
    letter = fruit[index]
    print(letter)
    index = index - 1
#2
print(fruit[:])# whole variable
#3
def count(word,letter):
    counts = 0
    for i in word:
        if letter == i:
            counts = counts + 1
    return counts
print(count('banana', 'a'))
#4
word='banan'
print(count(word,'a'))
#5
text = 'X-DSPAM-Confidence: 0.8475'
place=text.find(':')+1
print(float(text[place:]))
#6
word='I like banana.'
print(word.replace('banana','oranges'))

