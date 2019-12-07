import subprocess
from subprocess import PIPE
from itertools import permutations
from time import sleep

def runIntCode(param1, param2):
    p = subprocess.Popen('./07/intCodeComputer', stdin=PIPE, stdout=PIPE)

    inputToProc = f"{param1}\n{param2}\n".encode("utf-8")
    ans, stderr = p.communicate(inputToProc)

    ans = ans.decode("utf-8").strip().replace("Enter a  value: \n", '')
    return int(ans)

maxPerm = None
localMax = -1
for perm in permutations([0,1,2,3,4]):
    ampAOut = runIntCode(perm[0], 0)

    ampBOut = runIntCode(perm[1], ampAOut)
    ampCOut = runIntCode(perm[2], ampBOut)
    ampDOut = runIntCode(perm[3], ampCOut)
    ampEOut = runIntCode(perm[4], ampDOut)

    if ampEOut > localMax:
        localMax = ampEOut
        maxPerm = perm

print(f"Max Out for Part One is: {localMax}")


def startProgram(param1, param2):
    p = subprocess.Popen('./07/intCodeComputer', stdin=PIPE, stdout=PIPE)
    inputToProc = f"{param1}\n{param2}\n".encode("utf-8")
    p.stdin.write(inputToProc)
    p.stdin.flush()

    p.stdout.readline() #clean out last EnterVal
    p.stdout.readline() #clean out last EnterVal

    ans = p.stdout.readline()
    ans = ans.decode("utf-8").strip().replace("Enter a  value: \n", '')

    p.stdout.readline() #clean out one last EnterVal

    return p, int(ans)

def inputandreturn(p, param1):
    try:
        inputToProc = f"{param1}\n".encode("utf-8")
        p.stdin.write(inputToProc)
        p.stdin.flush()
    except BrokenPipeError:
        print("BrokenPipe")


    ans = p.stdout.readline()
    ans = ans.decode("utf-8").strip().replace("Enter a  value: \n", '')

    if p.stdout.readline().decode("utf-8") != "Enter a  value: \n":
        #this is the last one
        return int(ans), True
        
    return int(ans), False


maxPerm = None
localMax = -1

for perm in permutations([5,6,7,8,9]):

    ampAproc, ampAOut = startProgram(perm[0], 0)
    ampBproc, ampBOut = startProgram(perm[1], ampAOut)
    ampCproc, ampCOut = startProgram(perm[2], ampBOut)
    ampDproc, ampDOut = startProgram(perm[3], ampCOut)
    ampEproc, ampEOut = startProgram(perm[4], ampDOut)

    lastOne = False
    while ampEproc.poll() != 0 and not lastOne:
        ampAOut = inputandreturn(ampAproc, ampEOut)[0]
        ampBOut = inputandreturn(ampBproc, ampAOut)[0]
        ampCOut = inputandreturn(ampCproc, ampBOut)[0]
        ampDOut = inputandreturn(ampDproc, ampCOut)[0]
        ampEOut, lastOne = inputandreturn(ampEproc, ampDOut)

    if ampEOut > localMax:
        localMax = ampEOut
        maxPerm = perm

print(f"Max Out for Part Two is: {localMax}")

