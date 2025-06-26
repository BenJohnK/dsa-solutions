# a = [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,6]

def index_of_first_occurence(lst, element):
    found_index = -1
    low = 0
    high = len(lst) - 1
    while(low <= high):
        mid = (low + high)//2
        if lst[mid] == element:
            found_index = mid
            high = mid - 1
        elif lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return found_index


lst = list(map(lambda x: int(x), input().split(" ")))
element = int(input())
print(index_of_first_occurence(lst, element))
