fhand=open('mbox-short (1).txt')

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    line[1:]
    words = line.split()
    print(words, len(words))

'''
count =  words
print(len(count))
'''