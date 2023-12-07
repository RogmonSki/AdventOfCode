import re

total = 0

with open("input.txt.", "r") as f:
    for line in f:
        game = ''.join(re.split(r'[;:]', line.replace(',', ''))).split()
        red = 0
        blue = 0
        green = 0
        for j in range(2, len(game)):
            if (game[j]) == "red":
                if int(game[j-1]) > red:
                    red = int(game[j-1])
            elif (game[j]) == "blue":
                if int(game[j-1]) > blue:
                    blue = int(game[j-1])
            elif (game[j]) == "green":
                if int(game[j-1]) > green:
                    green = int(game[j-1])
        power = red * blue * green
        total += power

print(total)      