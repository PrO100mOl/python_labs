

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