
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return "ValueError"
    return(min(nums),max(nums))
# Вернуть кортеж (минимум, максимум). Если список пуст — ValueError.

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums.sort()
    return(list(set(nums)))
# Вернуть отсортированный список уникальных значений (по возрастанию).

def flatten(mat: list[list | tuple]) -> list:
    temp = []
    for x in mat:
        for y in x:
            if y == str(y):
                return "TypeError"
            temp.append(y)
    return(temp)
# «Расплющить» список списков/кортежей в один список по строкам (row-major). Если встретилась строка/элемент, который не является списком/кортежем — TypeError.

min_max

print(min_max([3, -1, 5, 5, 0]))# → (-1, 5)
print(min_max([42]))# → (42, 42)
print(min_max([-5, -2, -9]))# → (-9, -2)
print(min_max([]))# → ValueError
print(min_max([1.5, 2, 2.0, -3.1]))# → (-3.1, 2)

unique_sorted

print(unique_sorted([3, 1, 2, 1, 3]))# → [1, 2, 3]
print(unique_sorted([]))# → []
print(unique_sorted([-1, -1, 0, 2, 2]))# → [-1, 0, 2]
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))# → [0, 1.0, 2.5] (допускаем смешение int/float)

flatten

print(flatten([[1, 2], [3, 4]]))# → [1, 2, 3, 4]
print(flatten([[1, 2], (3, 4, 5)]))# → [1, 2, 3, 4, 5]
print(flatten([[1], [], [2, 3]]))# → [1, 2, 3]
print(flatten([[1, 2], "ab"]))# → TypeError («строка не строка строк матрицы»)

