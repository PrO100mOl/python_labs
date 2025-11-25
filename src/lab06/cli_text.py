import argparse
from pathlib import Path
import sys

from src.lib.text import normalize, tokenize, count_freq


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов вывести")

    args = parser.parse_args()

    if args.command == "cat":
        path = Path(args.input)
        try:
            with path.open(encoding="utf-8") as f:
                if args.n:
                    for i, line in enumerate(f, start=1):
                        print(f"{i}\t{line.rstrip()}")
                else:
                    for line in f:
                        print(line.rstrip())
        except FileNotFoundError:
            print(f"Ошибка: файл не найден: {path}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "stats":
        path = Path(args.input)
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"Ошибка: файл не найден: {path}", file=sys.stderr)
            sys.exit(1)

        text_norm = normalize(text)
        tokens = tokenize(text_norm)
        freqs = count_freq(tokens)

        if args.top <= 0:
            print("Ошибка: значение --top должно быть > 0", file=sys.stderr)
            sys.exit(2)

        items = sorted(freqs.items(), key=lambda kv: kv[1], reverse=True)[: args.top]
        for word, cnt in items:
            print(f"{word}\t{cnt}")
    else:
        #help
        parser.print_help()


if __name__ == "__main__":
    main()
