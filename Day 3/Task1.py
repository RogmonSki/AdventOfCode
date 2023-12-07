from string import punctuation

total = 0
symbols = set(punctuation)
symbols.remove('.')
lines = []

with open("input.txt", "r") as f:
    for line in f:
        lines.append(line)
    
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in symbols:
            if j+1 < len(lines[i]):
                if lines[i][j+1].isdigit():
                    if lines[i][j+3].isdigit():
                        total += int(str(lines[i][j+1]) + str(lines[i][j+2] + str(lines[i][j+3])))
                    else:
                        total += int(str(lines[i][j+1]) + str (lines[i][j+2]))
            if j-1 >= 0:
                if lines[i][j-1].isdigit():
                    if lines[i][j-3].isdigit():
                        total += int(str(lines[i][j-3]) + str(lines[i][j-2]) + str(lines[i][j-1]))
                    else:
                        total += int(str(lines[i][j-2]) + str(lines[i][j-1]))

print(total)
                    