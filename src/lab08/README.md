# Лабораторная работа 8 — ООП и сериализация студентов

## Модель `Student`
- `fio`, `birthdate` (`YYYY-MM-DD`), `group`, `gpa` (0–5).
- Валидация происходит в `__post_init__`: проверяется формат даты и диапазон среднего балла.
- Методы:
  - `age()` — вычисление количества полных лет по текущей дате.
  - `to_dict()` / `from_dict()` — (де)сериализация в словарь.
  - `__str__()` — компактное текстовое представление.

## Сериализация
Функции расположены в `src/lab08/serialize.py`:
- `students_to_json(students, path)` — сохраняет список `Student` в JSON (создаёт каталоги при необходимости).
- `students_from_json(path)` — читает JSON-массив словарей и создаёт список `Student` с полной валидацией.

## Примеры
### Входные и выходные файлы
- `data/lab08/students_input.json` — данные для импорта.
- `data/lab08/students_output.json` — пример результата сериализации.

### Запуск из интерпретатора
```python
from src.lab08 import Student, students_from_json, students_to_json

students = students_from_json("data/lab08/students_input.json")
print(students[0])          # Иванов Иван Иванович (SE-01) — born 2002-04-15, GPA: 4.50
print(students[0].age())    # Полные годы, рассчитываются от текущей даты

# Сохраняем в новый файл
students_to_json(students, "data/lab08/exported.json")
```

### Пример словаря и восстановления объекта
```python
payload = {
    "fio": "Новый Студент",
    "birthdate": "2004-12-31",
    "group": "BD-01",
    "gpa": 4.2,
}
student = Student.from_dict(payload)
print(student.to_dict())
```

### Ошибки валидации
```python
Student(fio="Тест", birthdate="2004/12/31", group="SE-01", gpa=4)  # ValueError: birthdate must be in YYYY-MM-DD format
Student(fio="Тест", birthdate="2004-12-31", group="SE-01", gpa=5.5)  # ValueError: gpa must be between 0 and 5
```
