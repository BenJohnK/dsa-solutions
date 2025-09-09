x=int(input())
n=int(input())
q=x
r=1
while(n != 0):
    if n&1:
        r=r*q
    q = q*q
    n=n//2

print(r)

