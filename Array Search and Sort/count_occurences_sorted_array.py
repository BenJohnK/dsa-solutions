# a = [1,2,3,3,3,3,4,5,6]

def count_occurences(lst, x):
    occurences_count = 0
    

lst = list(map(lambda x: int(x), input().split()))
x = int(input())
print(count_occurences(lst, x))
