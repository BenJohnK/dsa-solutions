def set_matrix_zeroes(matrix):
    has_first_row_zero = False
    for x in matrix[0]:
        if x == 0:
            has_first_row_zero = True
    for i in range(1, len(matrix)):
        has_zero = False
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                has_zero = True
                matrix[0][j] = 0
        if has_zero:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[0][j] == 0:
                matrix[i][j] = 0
    if has_first_row_zero:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
            

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

set_matrix_zeroes(matrix)

print(matrix)