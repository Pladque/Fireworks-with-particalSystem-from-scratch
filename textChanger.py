f = open('fireworkMaker.py', 'r')
f2  = open('temp.txt', 'w')

for line in f.readlines():
    f2.write(line.replace("random.", ''))