import math
def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


n = int(input())
n_copy = n

for i in range(2, n+1):
    if is_prime(i):
        while(n%i == 0):
            print(i)
            n = n/i
    else:
        continue