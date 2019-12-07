lineList = []

orbitDict = {}


with open("input.txt") as inFile:
    for line in inFile:
        lineList.append(line.strip())

for line in lineList:
    base, orbitor = line.split(')')

    if base in orbitDict.keys():
        orbitDict[base].append(orbitor)
    else:
        orbitDict[base] = [orbitor]


def howManyOrbit(key, depth):
    i = 0
    if key in orbitDict.keys():
        for orbitKey in orbitDict[key]:
            i += howManyOrbit(orbitKey, depth+1)
        return i + depth
    else:
        return depth

PartOneAns = howManyOrbit("COM", 0)
print(f"Part One: {PartOneAns}")


class Planet:
    def __init__(self, name):
        self.name = name
        self.directOrbitList = []

    def __repr__(self):
        return self.name

def makeBinaryTree(key):
    root = Planet(key)
    if key in orbitDict.keys():
        for orbitKey in orbitDict[key]:
            root.directOrbitList.append(makeBinaryTree(orbitKey))
        return root
    else:
        return root

def pathToPlanet(root, path, target):
    if root == False:
        return False

    path.append(root.name)

    if root.name == target:
        return True

    for node in root.directOrbitList:
        x = pathToPlanet(node, path, target)
        if x:
            return x

    path.pop()
    return False

def distance(root, name1, name2):
    if root:
        #store path to node 1
        path1 = []
        pathToPlanet(root, path1, name1)

        #store path to node 2
        path2 = []
        pathToPlanet(root, path2, name2)

        i = 0

        while i < len(path1) and i < len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i+1
        # get the path length by deducting the
        # intersecting path length (or till LCA)
        return (len(path1) + len(path2) - 2 * i)
    else:
        return 0

COM = makeBinaryTree("COM")


x = distance(COM, "YOU", "SAN") - 2

print(f"Distance between You and Santa: {x}")