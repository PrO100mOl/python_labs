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
        raise ValueError(
            "Пустой JSON или неподдерживаемая структура (нужен непустой список объектов)."
        )

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(
                f"JSON должен быть списком словарей; элемент #{i} имеет тип {type(item).__name__}."
            )

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


if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
