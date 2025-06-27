## a = [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,6]


def index_of_last_occurence(lst, element):
    low = 0
    high = len(lst) - 1
    last_index = len(lst) - 1
    while(low<=high):
        mid = (low + high) // 2
        if lst[mid] == element:
            if mid == last_index or lst[mid+1] != lst[mid]:
                return mid
            else:
                low = mid + 1
        elif lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = list(map(lambda x: int(x), input().split(" ")))
element = int(input())

print(index_of_last_occurence(lst, element))