total = 0

with open("input.txt", "r") as f:
    for line in f:
        nums = [x for x in line if x.isdigit()]
        total += int(str(nums[0]) + str(nums[-1]))

print(total)