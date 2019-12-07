import subprocess
from subprocess import PIPE

p = subprocess.Popen('./intCodeComputer', stdin=PIPE, stdout=PIPE)

p.communicate(intput='5\n')

print("test")