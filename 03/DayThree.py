FILE_PATH = "input.txt"


def buildCordSet(lineString):
    lineSet = {(0, 0)}
    curLoc = [0,0]
    for dirSet in lineString.split(','):
        if dirSet.startswith('R'):
            steps = int(dirSet.replace('R', ''))
            for x in range(1, steps+1):
                lineSet.add((curLoc[0]+x, curLoc[1]))
            curLoc[0] = curLoc[0] + steps

        elif dirSet.startswith('D'):
            steps = int(dirSet.replace('D', ''))
            for y in range(1, steps+1):
                lineSet.add((curLoc[0], curLoc[1]-y))
            curLoc[1] = curLoc[1] - steps

        elif dirSet.startswith('L'):
            steps = int(dirSet.replace('L', ''))
            for x in range(1, steps+1):
                lineSet.add((curLoc[0]-x, curLoc[1]))
            curLoc[0] = curLoc[0] - steps

        elif dirSet.startswith('U'):
            steps = int(dirSet.replace('U', ''))
            for y in range(1, steps+1):
                lineSet.add((curLoc[0], curLoc[1]+y))
            curLoc[1] = curLoc[1] + steps
        else:
            print(f"unrecognized input: {dirSet}")

    return lineSet

lineList = []

with open(FILE_PATH) as inFile:
    for line in inFile:
        lineList.append(line.strip())

LineOneSet = buildCordSet(lineList[0])
LineTwoSet = buildCordSet(lineList[1])

crossings = LineOneSet.intersection(LineTwoSet)

minCord = (9999999999, 999999999999)

for cord in crossings:
    if abs(cord[0]) + abs(cord[1]) < abs(minCord[0]) + abs(minCord[1]) and cord != (0, 0):
        minCord = cord

print(f"PART One: Minimum Cord: {minCord}. Manhattan Distance: {abs(minCord[0]) + abs(minCord[1])}")

# Above, I'm preserving the way I solved part 1, but I need to do it a bit differently in order to solve part 2
# Sets are not the best way to solve part 2

# part 2


def buildCordSet2(lineString):
    lineSet = {(0, 0, 0)}
    curLoc = [0,0]
    totalSteps = 0
    for dirSet in lineString.split(','):
        if dirSet.startswith('R'):
            steps = int(dirSet.replace('R', ''))
            for x in range(1, steps+1):
                lineSet.add((curLoc[0]+x, curLoc[1], totalSteps+x))
            curLoc[0] += steps
            totalSteps += steps
        elif dirSet.startswith('D'):
            steps = int(dirSet.replace('D', ''))
            for y in range(1, steps+1):
                lineSet.add((curLoc[0], curLoc[1]-y, totalSteps+y))
            curLoc[1] = curLoc[1] - steps
            curLoc[0] += steps
            totalSteps += steps
        elif dirSet.startswith('L'):
            steps = int(dirSet.replace('L', ''))
            for x in range(1, steps+1):
                lineSet.add((curLoc[0]-x, curLoc[1], totalSteps+x))
            curLoc[0] -= steps
            totalSteps += steps
        elif dirSet.startswith('U'):
            steps = int(dirSet.replace('U', ''))
            for y in range(1, steps+1):
                lineSet.add((curLoc[0], curLoc[1]+y, totalSteps+y))
            curLoc[1] += steps
            totalSteps += steps
        else:
            print(f"unrecognized input: {dirSet}")

    return lineSet

lineList = []

with open(FILE_PATH) as inFile:
    for line in inFile:
        lineList.append(line.strip())

LineOneSet = buildCordSet2(lineList[0])
LineTwoSet = buildCordSet2(lineList[1])

minCord = (0, 0, 999999999999)

for cordOne in LineOneSet:
    for cordTwo in LineTwoSet:
        if cordOne[0] == cordTwo[0] and cordOne[1] == cordTwo[1]:
            if cordOne[2] + cordTwo[2] < minCord[2]:
                minCord = cordOne

print(f"PART 2: Minimum Cord: {minCord}. Line Distance: {minCord[2]}")
