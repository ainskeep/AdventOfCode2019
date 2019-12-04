inputLow = 134564
inputHigh = 585159

def neverDecreasesAndHasDouble(x):
    intList = [int(d) for d in str(x)]
    lastDigit = -1
    hasDouble = False
    for digit in intList:
        if digit == lastDigit:
            hasDouble = True

        if digit >= lastDigit:
            lastDigit = digit
        else:
            return False

    # if we make it this far, never decreases is true
    return hasDouble

passwordList = []

for i in range(inputLow, inputHigh+1):
    if neverDecreasesAndHasDouble(i):
        passwordList.append(i)

print(f"PART ONE: The number of possible passwords is: {len(passwordList)}")

# PART 2

def neverDecreasesAndHasDouble2(x):
    intList = [int(d) for d in str(x)]
    lastDigit = -1
    hasDouble = False
    for i in range(6):
        digit = intList[i]


        if digit >= lastDigit:
            lastDigit = digit
        else:
            return False

    if intList[0] == intList[1] and intList[1] != intList[2]:
        return True

    if intList[1] == intList[2] and intList[2] != intList[3] and intList[0] != intList[1]:
        return True
    if intList[2] == intList[3] and intList[3] != intList[4] and intList[1] != intList[2]:
        return True
    if intList[3] == intList[4] and intList[4] != intList[5] and intList[2] != intList[3]:
        return True

    if intList[4] == intList[5] and intList[3] != intList[4]:
        return True

    return False

passwordList = []

for i in range(inputLow, inputHigh+1):
    if neverDecreasesAndHasDouble2(i):
        passwordList.append(i)

print(f"PART Two: The number of possible passwords is: {len(passwordList)}")

