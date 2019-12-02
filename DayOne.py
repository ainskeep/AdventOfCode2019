import math

FILE_PATH = "C:/Users/Alex Inskeep/PycharmProjects/AdventOfCode/inputFiles/day_one_input.txt"

## PART1 ##
def calcFuleRequirement(x):
    return math.floor(x/3) - 2

total = 0

with open(FILE_PATH) as inFile:
    for line in inFile:
        x = int(line.strip())
        total += calcFuleRequirement(x)

print(f"PART ONE ANSWER: {total}")

## PART 2 ##

total = 0

def calcFuleRequirement(x):
    ans = math.floor(x/3) - 2

    if ans <= 0:
        return 0
    else:
        return ans + calcFuleRequirement(ans)


with open(FILE_PATH) as inFile:
    for line in inFile:
        x = int(line.strip())
        total += calcFuleRequirement(x)

print(f"PART TWO ANSWER: {total}")
