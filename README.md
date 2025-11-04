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


## Лабораторная работа 3


### Задание 1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    
    if yo2e:
        for i in range(len(text)):
            if text[i] == "ё":
                text = text[:i]+"е"+text[i+1:]
            elif text[i] == "Ё":
                text = text[:i]+"Е"+text[i+1:]
    if casefold:
        text = text.casefold()
    
    text = " ".join(text.split())
    return text

# Если casefold=True — привести к casefold (лучше, чем lower для Юникода).
# Если yo2e=True — заменить все ё/Ё на е/Е.
# Убрать невидимые управляющие символы (например, \t, \r) → заменить на пробелы, схлопнуть повторяющиеся пробелы в один.

import re

def tokenize(text: str) -> list[str]:
    g = ''
    # h = 0
    for i in range(len(text)):
        # if h == 1:
        #     h = 0
        #     continue
        if text[i]+"g" == "\g":
            text = text[:i]+"  "+text[i+2:]
            # h=1
        elif not(re.fullmatch(r"[\w-]", text[i])):
            text = text[:i]+" "+text[i+1:]
    text = text.split()
    return text


# Разбить на «слова» по небуквенно-цифровым разделителям.
# В качестве слова считаем последовательности символов \w (буквы/цифры/подчёркивание) плюс дефис внутри слова (например, по-настоящему).
# Числа (например, 2025) считаем словами.

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for t in tokens:
        if t in freq:
            freq[t.replace("ё","е")] += 1
        else:
            freq[t.replace("ё","е")] = 1
    return dict(sorted(freq.items()))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    pairs: list[tuple[int, str]] = []
    for w, c in freq.items():
        pairs.append((-c, w))  
    pairs.sort() 
    result: list[tuple[str, int]] = []
    i = 0
    for c, w in pairs:
        if i >= n:
            break
        result.append((w, -c))
        i += 1
    return result


# Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова.
```


### Задание 2
```python
from ..lib.text import normalize, tokenize, count_freq, top_n

# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3,"b":2,"c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]

print("OK")


# cd /home/mol/Desktop/python_labs                                       main        
# python -m src.lab03.test_text
```
![Картинка 1](./images/lab03/test_text.png)


### Задание 3
```python
# src/lab03/text_stats.py
import sys
from ..lib.text import normalize, tokenize, count_freq, top_n

def main() -> None:
    text = str(sys.stdin.read())
    # text2 = 'Привет, мир! Привет!!!\n'
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ-5:")
    for w, c in sorted(freq.items())[::-1]:
        print(f"{w}:{c}")

if __name__ == "__main__":
    main()
```
![Картинка 1](./images/lab03/text_stats.png)


## Лабораторная работа 4

### Задание 1
```python
from src.lib.text import normalize, tokenize, count_freq, top_n

from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

txt = read_text("data/lab04/input.txt")  # должен вернуть строку
print(txt)
write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV
```
![Картинка 1](./images/lab04/io_txt_csv1.png)
![Картинка 2](./images/lab04/lab4_input.png)
![Картинка 3](./images/lab04/lab4_check.png)

### Задание 2
```python
from src.lab04.io_txt_csv import read_text, write_csv
from ..lib.text import normalize, tokenize, count_freq, top_n


txt = read_text("data/lab04/input.txt")
if txt == "":
    print()
    op = [("word","count")]
    write_csv(op, "data/lab04/check.csv")
else:
    text = txt
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ-5:")
    op = [("word","count")]
    for w, c in top_n(freq):
        op.append((w,c))
        print(f"{w}:{c}")

    write_csv(op, "data/lab04/check.csv")
```
![Картинка 1](./images/lab04/text_report.png)
![Картинка 2](./images/lab04/report_check.png)



## Лабораторная работа 5

### Задание 1
```python
from pathlib import Path
import json
import csv
from typing import Any

# from src.lib.text import normalize, tokenize, count_freq, top_n

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    p_json = Path(json_path)
    p_csv = Path(csv_path)

    # if tokenize(p_json)[-1].lower() != "json" or tokenize(p_csv)[-1].lower() != "csv":
    if p_json.suffix.lower() != ".json" or p_csv.suffix.lower() != ".csv":
        raise ValueError("Неверный тип файла: ожидаются .json (вход) и .csv (выход).")

    with p_json.open(encoding="utf-8") as jf:
        try:
            data: Any = json.load(jf)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный JSON: {e}") from e

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура (нужен непустой список объектов).")

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"JSON должен быть списком словарей; элемент #{i} имеет тип {type(item).__name__}.")

    keys: set[str] = set()
    for obj in data:
        keys.update(obj.keys())
    fieldnames = sorted(keys)

    with p_csv.open("w", newline="", encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for obj in data:
            row = {k: obj.get(k, "") for k in fieldnames}
            writer.writerow(row)


def _sniff_dialect(sample: str) -> csv.Dialect:
    try:
        return csv.Sniffer().sniff(sample, delimiters=",;")
    except csv.Error:
        return csv.get_dialect("excel")

def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    p_csv = Path(csv_path)
    p_json = Path(json_path)

    if p_csv.suffix.lower() != ".csv" or p_json.suffix.lower() != ".json":
        raise ValueError("Неверный тип файла: ожидаются .csv (вход) и .json (выход).")

    with p_csv.open(encoding="utf-8") as f:
        sample = f.read(4096)
        if not sample.strip():
            raise ValueError("Пустой CSV.")
        f.seek(0)
        dialect = _sniff_dialect(sample)
        reader = csv.DictReader(f, dialect=dialect)

        if not reader.fieldnames or all((h or "").strip() == "" for h in reader.fieldnames):
            raise ValueError("CSV без заголовка.")

        rows = [{k: (v if v is not None else "") for k, v in row.items()} for row in reader]

    if len(rows) == 0:
        raise ValueError("CSV не содержит строк данных.")

    with p_json.open("w", encoding="utf-8") as jf:
        json.dump(rows, jf, ensure_ascii=False, indent=2)



json_to_csv('data/samples/people.json','data/out/people_from_json.csv')
csv_to_json('data/samples/people.csv','data/out/people_from_csv.json')
```
![Картинка 1](./images/lab05/people.json.png)
![Картинка 2](./images/lab05/people_from_json.csv.png)
![Картинка 3](./images/lab05/people.csv.png)
![Картинка 4](./images/lab05/people_from_csv.json.png)



### Задание 1
```python
from pathlib import Path
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    p_csv = Path(csv_path)
    p_xlsx = Path(xlsx_path)

    if p_csv.suffix.lower() != ".csv" or p_xlsx.suffix.lower() != ".xlsx":
        raise ValueError("Неверный тип файла: ожидаются .csv (вход) и .xlsx (выход).")

    with p_csv.open(encoding="utf-8") as f:
        sample = f.read(4096)
        if not sample.strip():
            raise ValueError("Пустой CSV.")
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;")
        except csv.Error:
            dialect = csv.get_dialect("excel")
        reader = csv.reader(f, dialect=dialect)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV пуст.")
    header = rows[0]
    if not header or all((h or "").strip() == "" for h in header):
        raise ValueError("CSV без заголовка.")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # Автоширина колонок
    col_widths = [0] * len(header)
    for row in rows:
        for i, cell in enumerate(row):
            length = len(str(cell)) if cell is not None else 0
            if i >= len(col_widths):
                col_widths.extend([0] * (i + 1 - len(col_widths)))
            if length > col_widths[i]:
                col_widths[i] = length

    for i, width in enumerate(col_widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = max(8, width)

    wb.save(p_xlsx)

csv_to_xlsx('data/samples/people.csv','data/out/people.xlsx')
```
![Картинка 1](./images/lab05/people.csv.png)
![Картинка 2](./images/lab05/people.xlsx.png)












