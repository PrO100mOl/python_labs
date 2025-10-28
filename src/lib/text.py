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
        if (text[i]+"g") == r"\g":
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


# print( normalize("ПрИвЕт\nМИр\t") == "привет мир")
# print( normalize("ёжик, Ёлка") == "ежик, елка")

# print( tokenize("привет, мир!") == ["привет", "мир"])
# print( tokenize("по-настоящему круто") == ["по-настоящему", "круто"])
# print( tokenize("2025 год") == ["2025", "год"])

# freq = count_freq(["a","b","a","c","b","a"])
# print( freq == {"a":3,"b":2,"c":1})
# print( top_n(freq, 2) == [("a",3), ("b",2)])

# freq2 = count_freq(["bb","aa","bb","aa","cc"])
# print( top_n(freq2, 2) == [("aa",2), ("bb",2)])
