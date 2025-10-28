# src/lab03/text_stats.py
import sys
from ..lib.text import normalize, tokenize, count_freq, top_n

def main() -> None:
    text = str(sys.stdin.read())
    # text = 'Привет, мир! Привет!!!\n'
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(set(tokens))}")
    print("Топ-5:")
    for w, c in top_n(freq):
        print(f"{w}:{c}")

if __name__ == "__main__":
    main()


# chcp 65001                                                                                     
# >> $env:PYTHONUTF8=1                                                                                                              
# >> $OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)


# cd /home/mol/Desktop/python_labs
# echo 'Привет, мир! Привет!!!\n' | python -m src.lab03.text_stats
