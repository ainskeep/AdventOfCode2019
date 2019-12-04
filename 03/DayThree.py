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

# part 2

# I needed to rewrite the buildSet into a buildDict

def buildCordDict(lineString):
    lineDict = {(0, 0): 0}
    curLoc = [0,0]
    totalSteps = 0
    for dirSet in lineString.split(','):
        if dirSet.startswith('R'):
            steps = int(dirSet.replace('R', ''))
            for x in range(1, steps+1):
                lineDict[(curLoc[0]+x, curLoc[1])] = totalSteps + x
            curLoc[0] += steps
            totalSteps += steps
        elif dirSet.startswith('D'):
            steps = int(dirSet.replace('D', ''))
            for y in range(1, steps+1):
                lineDict[(curLoc[0], curLoc[1]-y)] = totalSteps+y
            curLoc[1] -= steps
            totalSteps += steps
        elif dirSet.startswith('L'):
            steps = int(dirSet.replace('L', ''))
            for x in range(1, steps+1):
                lineDict[(curLoc[0]-x, curLoc[1])] = totalSteps + x
            curLoc[0] -= steps
            totalSteps += steps
        elif dirSet.startswith('U'):
            steps = int(dirSet.replace('U', ''))
            for y in range(1, steps+1):
                lineDict[(curLoc[0], curLoc[1] + y)] = totalSteps + y
            curLoc[1] += steps
            totalSteps += steps
        else:
            print(f"unrecognized input: {dirSet}")

    return lineDict

lineList = []

with open(FILE_PATH) as inFile:
    for line in inFile:
        lineList.append(line.strip())

LineOneDict = buildCordDict(lineList[0])
LineTwoDict = buildCordDict(lineList[1])

keyIntersection = set(LineOneDict.keys()) & set(LineTwoDict.keys())

minDistance = -1

for key in keyIntersection:
    if minDistance == -1 and key != (0, 0):
        minDistance = LineOneDict[key] + LineTwoDict[key]

    if LineOneDict[key] + LineTwoDict[key] < minDistance and key != (0, 0):
        minDistance = LineOneDict[key] + LineTwoDict[key]

print(f"Min Line distance: {minDistance}")
