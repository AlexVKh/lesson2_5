def get_matrix(n, m, value):
    matrix = []
    if n == 0 or m == 0:
        return matrix
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return(matrix)

n = int(input())
m = int(input())
value = int(input())
matrix_ = get_matrix(n, m, value)
#print(matrix_)

#красивый вывод матрицы
for i in range(n):
    for j in range(m):
        print(matrix_[i][j], end=' ')
    print()

