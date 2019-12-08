HEIGHT = 6
WIDTH = 25

lines = []

with open("08/input.txt") as File:
    for line in File:
        lines.append(line)

inputText = lines[0]

picture = []

splitIntoRows = [inputText[i:i+WIDTH] for i in range(0, len(inputText), WIDTH)]

for i in range( int(len(inputText)/(HEIGHT*WIDTH))  ) :
    layer = []

    for j in range(HEIGHT):
        layer.append( splitIntoRows[i*HEIGHT + j] )
    
    picture.append(layer)


numZeroes = HEIGHT*WIDTH * 99
position = -1

for i in range(len(picture)):
    layer = picture[i]
    stringLayer = ""

    stringLayer = stringLayer.join(layer)

    if stringLayer.count('0') < numZeroes:
        position = i
        numZeroes = stringLayer.count('0')
        ans = stringLayer.count('1') * stringLayer.count('2')


print(f"The answer to part one is: {ans}")

image = []

for i in range(HEIGHT):
    row = []
    for j in range(WIDTH):
        char = -1
        breakLoop = False
        for layer in picture:
            char = int(layer[i][j])
            if char == 0 or char == 1:
                break
        
        row.append(char)

    image.append(row)

for row in image:
    row= row[:]
    for pix in row:
        print(pix,end=",")

    print("")
