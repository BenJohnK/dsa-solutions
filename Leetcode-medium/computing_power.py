def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        p = power(x, n/2)
        return p * p
    p = power(x, (n-1)/2)
    return p * p * x


print(pow(4, 5))