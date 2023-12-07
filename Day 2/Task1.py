import re

total = 0

with open("input.txt", "r") as f:
    for line in f:
        valid = True
        game = re.split(r'[;:]', line.replace(',', ''))
        for i in range(1, len(game)):
            total_red = 0
            total_blue = 0
            total_green = 0
            cubes = game[i].split()
            for j in range(1, len(cubes), 2):
                if cubes[j] == "red":
                    total_red += int(cubes[j-1])
                elif cubes[j] == "blue":
                    total_blue += int(cubes[j-1])
                elif cubes[j] == "green":
                    total_green += int(cubes[j-1]) 
            if (total_red > 12) or (total_blue > 14) or (total_green > 13):
                valid = False
                break
        if valid == True:
            total += int(game[0].split()[1])
print(total)
            