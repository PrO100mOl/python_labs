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

