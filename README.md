# простомол уно

## Лабораторная работа 1

### Задание 1
```python
имя = str(input("Имя:"))
возраст = int(input("Возраст:"))
print(f"Привет, {имя}! Через год тебе будет {возраст+1}.")
```

### Задание 2
```python
имя = float(input("a:").replace(",","."))
возраст = float(input("b:").replace(",","."))
print(f"sum={имя+возраст}; avg={round((имя+возраст)/2,2)}")
```
![Картинка 1](./images/lab01/02_sum_avg.png)


### Задание 3
```python
price= int(input("price="))
discount=int(input("discount="))
vat=int(input("vat="))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base} ₽"
      f"\nНДС:               {vat_amount} ₽"
      f"\nИтого к оплате:    {total} ₽")
```
![Картинка 1](./images/lab01/03_discount_vat.png)


### Задание 4
```python
Минуты=int(input("Минуты: "))
print(Минуты//60,":",Минуты%60,sep="")
```
![Картинка 1](./images/lab01/04_minutes_to_hhmm.png)


### Задание 5
```python
f =str(input("ФИО:"))
g = f.split()
h = ""
for i in g:
    h+=i[0]
j = f.split(" ")
k= 0
jj=0
for i in j:
    if len(i)!=0:
        k+=1
        jj+=len(i)
print(f"Инициалы: {h}."
      f"\nДлина (символов): {jj+2}")

```
![Картинка 1](./images/lab01/05_initials_and_len.py.png)


### Задание 6
```python
f = int(input())
q,w=0,0
for i in range(f):
    _,_,_,g = input().split()
    if g == "True":
        q+=1
    else:
        w+=1
print(q,w)
```
![Картинка 1](./images/lab01/06.png)


### Задание 7
```python
i = str(input())
q,w=0,0
for t in range(len(i)):
    if i[t].upper() == i[t]:
        q = t
        break

for t in range(len(i)):
    if i[t] in ['0',"1","2","3","4","5",'6',"7","8","9"]:
        w = t+1
        break
print(i[q:len(i):w-q])
```
![Картинка 1](./images/lab01/07.png)

## Лабораторная работа 2

### Задание 1
```python
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
```
![Картинка 1](./images/lab02/01_arrays.png)

### Задание 2
```python
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

```
![Картинка 1](./images/lab02/02_matrix.png)


### Задание 3
```python
def format_record(rec: tuple[str, str, float]) -> str:
    for i in range(len(rec)-1):
        if len(rec[i])==0:
            return "ValueError"
    if type(rec[2]) != float:
        return "TypeError"
    
    fio = rec[0].split()

    if len(fio) == 1:
        return "ValueError"
    
    inic = str(fio[0][0].upper())+str(fio[0][1:])+" "
    for i in range(1, len(fio)):
        inic= inic+str(fio[i][0].upper())+"."
    
    round = "{:.2f}".format(rec[2])

    return f"{inic}, гр. {rec[1]}, GPA {round}"


# Вернуть строку вида:
# Иванов И.И., гр. BIVT-25, GPA 4.60
# Правила:

#     ФИО может быть «Фамилия Имя Отчество» или «Фамилия Имя» — инициалы формируются из 1–2 имён (в верхнем регистре).
#     Лишние пробелы нужно убрать (strip, «схлопнуть» внутри).
#     GPA печатается с 2 знаками (округление правилами Python).


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)), "→ 'Иванов И.И., гр. BIVT-25, GPA 4.60'")
print(format_record(("Петров Пётр", "IKBO-12", 5.0)), "→ 'Петров П., гр. IKBO-12, GPA 5.00'")
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)), "→ 'Петров П.П., гр. IKBO-12, GPA 5.00'")
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)), "→ 'Сидорова А.С., гр. ABB-01, GPA 4.00'")
# Некорректные записи (пустое ФИО, пустая группа, неверный тип GPA) → ValueError/TypeError по усмотрению (описать в докстринге).
print(format_record(("", "ABB-01", 3.999)), "→ 'ValueError'")
print(format_record(("Петров", "ABB-01", 3.999)), "→ 'ValueError'")
print(format_record(("Петров Пётр", "", 5.0)), "→ 'ValueError'")
print(format_record(("Петров Пётр", "IKBO-12", 5)), "→ 'TypeError'")
```
![Картинка 1](./images/lab02/03_tuples.png)
