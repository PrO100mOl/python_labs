import argparse
from pathlib import Path
import sys

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def ensure_input(path: Path) -> None:
    if not path.exists():
        print(f"Ошибка: входной файл не найден: {path}", file=sys.stderr)
        sys.exit(1)


def prepare_output(path: Path) -> None:
    if path.parent:
        path.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Преобразовать JSON → CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON-файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV-файл")

    p2 = sub.add_parser("csv2json", help="Преобразовать CSV → JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON-файл")

    p3 = sub.add_parser("csv2xlsx", help="Преобразовать CSV → XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX-файл")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        src = Path(args.input)
        dst = Path(args.output)
        ensure_input(src)
        prepare_output(dst)
        try:
            json_to_csv(src, dst)
        except ValueError as e:
            print(f"Ошибка конвертации JSON → CSV: {e}", file=sys.stderr)
            sys.exit(2)

    elif args.cmd == "csv2json":
        src = Path(args.input)
        dst = Path(args.output)
        ensure_input(src)
        prepare_output(dst)
        try:
            csv_to_json(src, dst)
        except ValueError as e:
            print(f"Ошибка конвертации CSV → JSON: {e}", file=sys.stderr)
            sys.exit(2)

    elif args.cmd == "csv2xlsx":
        src = Path(args.input)
        dst = Path(args.output)
        ensure_input(src)
        prepare_output(dst)
        try:
            csv_to_xlsx(src, dst)
        except ValueError as e:
            print(f"Ошибка конвертации CSV → XLSX: {e}", file=sys.stderr)
            sys.exit(2)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
