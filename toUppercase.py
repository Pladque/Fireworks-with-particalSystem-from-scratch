f = open('colors.py', 'r')
f2  = open('colors.txt', 'w')

for line in f.readlines():
    f2.write(line.upper())