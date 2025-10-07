

def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []:
        return []
    for i in range(1,len(mat)):
        if len(mat[i]) != len(mat[i-1]):
            return ("ValueError")

    strok = len(mat)
    tabs = len(mat[0])
    resmat = []
    for i in range(tabs):
        resmat.append([0]*strok)
    for x in range(strok):
        for y in range(tabs):
            resmat[y][x] = mat[x][y]
    return resmat
# Поменять строки и столбцы местами. Пустая матрица [] → [].
# Если матрица «рваная» (строки разной длины) — ValueError.

def row_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(1,len(mat)):
        if len(mat[i]) != len(mat[i-1]):
            return ("ValueError")
    resmat = []
    o=0
    for i in mat:
        for t in i:
            o+=t
        resmat.append(o)
        o = 0
    return resmat
# Сумма по каждой строке. Требуется прямоугольность (см. выше).

def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(1,len(mat)):
        if len(mat[i]) != len(mat[i-1]):
            return ("ValueError")
    strok = len(mat)
    tabs = len(mat[0])
    resmat = []
    o = 0
    for i in range(tabs):
        for t in range(strok):
            o+=mat[t][i]
        resmat.append(o)
        o = 0
    return resmat
# Сумма по каждому столбцу. Требуется прямоугольность.

transpose

print(transpose([[1, 2, 3]])," → [[1], [2], [3]]")
print(transpose([[1], [2], [3]])," → [[1, 2, 3]]")
print(transpose([[1, 2], [3, 4]])," → [[1, 3], [2, 4]]")
print(transpose([])," → []")
print(transpose([[1, 2], [3]])," → ValueError (рваная матрица)")

row_sums

print(row_sums([[1, 2, 3], [4, 5, 6]])," → [6, 15]")
print(row_sums([[-1, 1], [10, -10]])," → [0, 0]")
print(row_sums([[0, 0], [0, 0]])," → [0, 0]")
print(row_sums([[1, 2], [3]])," → ValueError (рваная)")

col_sums

print(col_sums([[1, 2, 3], [4, 5, 6]])," → [5, 7, 9]")
print(col_sums([[-1, 1], [10, -10]])," → [9, -9]")
print(col_sums([[0, 0], [0, 0]])," → [0, 0]")
print(col_sums([[1, 2], [3]])," → ValueError (рваная)")
