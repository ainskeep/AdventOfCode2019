import copy
from fractions import Fraction
WIDTH = 0
HEIGHT = 0


cordList = []

with open("input.txt") as File:
    for line in File:
        charList = list(line.strip())

        if cordList == []:
            for i in range(len(charList)):
                cordList.append([charList[i]])
        else:
            for i in range(len(charList)):
                cordList[i].append(charList[i])


HEIGHT = len(cordList)
WIDTH = len(cordList[0])


for y in range(HEIGHT):
    for x in range(WIDTH):
        print(cordList[x][y], end='')
    print('')


class asteroid(Exception):
    pass


def findNumberAsteroids(x, y):
    count = 0
    for i in range(WIDTH):
        for j in range(HEIGHT):

            if x == i and j == y:
                continue

            if cordList[i][j] == '#':
                # pick these cords. Figure out if there are feasible points between this point, and the base
                try:
                    if y == j:
                        # flat -- horizontal
                        if i < x:
                            # look right
                            for k in range(i + 1, x, 1):
                                if cordList[k][j] == '#':
                                    # there is an asteroid in the way
                                    raise asteroid
                        else:
                            # look left
                            for k in range(i - 1, x, -1):
                                if cordList[k][j] == '#':
                                    # there is an asteroid in the way
                                    raise asteroid

                    elif x == i:
                        # Vertical |
                        if j < y:
                            for l in range(j + 1, y, 1):
                                if cordList[i][l] == '#':
                                    # there is an asteroid in the way
                                    raise asteroid
                        else:
                            for l in range(j - 1, y, -1):
                                if cordList[i][l] == '#':
                                    # there is an asteroid in the way
                                    raise asteroid
                    else:
                        slope = Fraction(y - j, x - i)

                        if i <= x and j <= y:
                            # NW quad
                            for k in range(i + 1, x, 1):
                                for l in range(j + 1, y, 1):
                                    if (y - l) == slope * (x - k) and cordList[k][l] == '#':
                                        # there is an asteroid in the way
                                        raise asteroid
                        elif i >= x and j <= y:
                            # NE quad
                            for k in range(i - 1, x, -1):
                                for l in range(j + 1, y, 1):
                                    if (y - l) == slope * (x - k) and cordList[k][l] == '#':
                                        # there is an asteroid in the way
                                        raise asteroid
                        elif i <= x and j >= y:
                            # SW quad
                            for k in range(i + 1, x, 1):
                                for l in range(j - 1, y, -1):
                                    if (y - l) == slope * (x - k) and cordList[k][l] == '#':
                                        # there is an asteroid in the way
                                        raise asteroid
                        elif i >= x and j >= y:
                            # SE quad
                            if j == 3 and i ==4:
                                pass
                            for k in range(i - 1, x, -1):
                                for l in range(j - 1, y, -1):
                                    if (y - l) == slope * (x - k) and cordList[k][l] == '#':
                                        # there is an asteroid in the way
                                        raise asteroid
                except asteroid:
                    continue

                count += 1

    return count


maxAsteroids = -1
maxAsteroidPosition = (0, 0)

copyOfCordList = copy.deepcopy(cordList)


for x in range(WIDTH):
    for y in range(HEIGHT):
        if cordList[x][y] == '#':
            numAsteroids = findNumberAsteroids(x, y)
            copyOfCordList[x][y] = numAsteroids
            if numAsteroids > maxAsteroids:
                maxAsteroidPosition = (x, y)
                maxAsteroids = numAsteroids
        else:
            continue



print(f"MaxAsteroids: {maxAsteroids} at {maxAsteroidPosition}")
'''
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(copyOfCordList[x][y], end='')
    print('')
'''