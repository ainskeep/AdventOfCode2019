import math

FILE_PATH = "input.txt"

## PART1 ##
def calcFuelRequirement(x):
    return math.floor(x/3) - 2

total = 0

with open(FILE_PATH) as inFile:
    for line in inFile:
        x = int(line.strip())
        total += calcFuelRequirement(x)

print(f"PART ONE ANSWER: {total}")

## PART 2 ##

total = 0

def calcFuelRequirement(x):
    ans = math.floor(x/3) - 2

    if ans <= 0:
        return 0
    else:
        return ans + calcFuelRequirement(ans)


with open(FILE_PATH) as inFile:
    for line in inFile:
        x = int(line.strip())
        total += calcFuelRequirement(x)

print(f"PART TWO ANSWER: {total}")
