f = open('main.py', 'r')
f2  = open('temp.txt', 'w')

for line in f.readlines():
    f2.write(line.replace("random.", ''))