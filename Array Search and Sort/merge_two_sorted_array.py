lst1 = [4, 6, 8]
                
lst2 = [5, 7, 9, 10]

def merge_arrays(lst1: list, lst2: list) -> list:
    i = 0
    j = 0
    new_sorted_array = []
    while i < len(lst1) or j < len(lst2):
        if i == len(lst1):
            new_sorted_array.append(lst2[j])
            j += 1
            continue
        elif j == len(lst2):
            new_sorted_array.append(lst1[i])
            i += 1
            continue
        else:
            if lst1[i] < lst2[j]:
                new_sorted_array.append(lst1[i])
                i += 1
            elif lst1[i] > lst2[j]:
                new_sorted_array.append(lst2[j])
                j += 1
            else:
                new_sorted_array.append(lst1[i])
                new_sorted_array.append(lst2[j])
                i += 1
                j += 1
    return new_sorted_array

print(merge_arrays(lst1, lst2))