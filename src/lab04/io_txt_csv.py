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
        g = len(rows[0])
        for r in rows:
            if len(r)!=g:
                return "ValueError"
            w.writerow(r)

txt = read_text("data/lab04/input.txt")  # должен вернуть строку
print(txt)
write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV

# print(read_text("data/lab04/ff.txt", "utf-8"))
# rows = [
#     ("alice", 10),
#     ("bob",   20),
# ]
# write_csv(rows, "data/lab04/gg.csv")

