f= open('consts.py', 'r')

new_lines = []
for x, line in enumerate(f.readlines()):
    new_lines.append([])
    new_lines[x] = line.replace(' ', '')
    new_lines[x] =  new_lines[x].replace('\t', '')

f= open('colors.py', 'w')

for line in new_lines:
    f.write(line)