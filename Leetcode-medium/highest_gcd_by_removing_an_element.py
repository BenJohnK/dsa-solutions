# lst = [12, 15, 18, 24, 30]
#left_lst = [12, -1, -1, -1, 30]

import math

def find_highest_gcd(arr: list) -> int:
    n = len(arr)
    left_list = [-1] * n
    right_list = [-1] * n
    left_list[0] = arr[0]
    left_list[-1] = arr[-1]
    right_list[0] = arr[0]
    right_list[-1] = arr[-1]
    max_gcd = 0
    for i in range(1, n-1):
        current_gcd = math.gcd(arr[i], left_list[i-1])
        left_list[i] = current_gcd
    for i in range(n-2, 0, -1):
        current_gcd = math.gcd(arr[i], right_list[i+1])
        right_list[i] = current_gcd
    for i in range(1, n-1):
        gcd_without_i = math.gcd(left_list[i-1], right_list[i+1])
        if gcd_without_i > max_gcd:
            max_gcd = gcd_without_i
    if right_list[1] > max_gcd:
        max_gcd = right_list[1]
    if left_list[n-2] > max_gcd:
        max_gcd = left_list[n-2]
    return max_gcd

print(find_highest_gcd([12, 15, 18, 24, 30]))