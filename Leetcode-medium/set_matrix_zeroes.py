def set_matrix_zeroes(lst):
    track_set = set()
    for i in range(len(lst)):
        has_zero = False
        for j in range(len(lst[i])):
            if lst[i][j] == 0:
                has_zero = True
                track_set.add(j)
        if has_zero:
            for j in range(len(lst[i])):
                lst[i][j] = 0
    print(track_set)
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j in track_set:
                lst[i][j] = 0
    
        


lst = [[1,1,1], [1,0,0], [1,1,1]]

set_matrix_zeroes(lst)
print(lst)