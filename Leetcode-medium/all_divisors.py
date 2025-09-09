import math
n=int(input())

for i in range(1, math.floor(math.sqrt(n))):
    if n%i == 0:
        print(i)

for i in range(math.floor(math.sqrt(n)), 0, -1):
    if n%i == 0:
        print(n//i)
