import csv
import json
from pathlib import Path

import pytest

from src.lab05.json_csv import csv_to_json, json_to_csv


def test_json_to_csv_roundtrip(tmp_path: Path) -> None:
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25, "city": "Paris"},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(src, dst)

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert set(rows[0].keys()) == {"age", "city", "name"}
    assert rows[1]["city"] == "Paris"


def test_csv_to_json_roundtrip(tmp_path: Path) -> None:
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name;age\nAlice;22\nBob;25\n", encoding="utf-8")

    csv_to_json(src, dst)

    data = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) == 2
    assert {"name", "age"} <= data[0].keys()
    assert data[1]["age"] == "25"


def test_json_to_csv_invalid_extension(tmp_path: Path) -> None:
    src = tmp_path / "data.txt"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(src, tmp_path / "out.txt")


def test_json_to_csv_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        json_to_csv(tmp_path / "missing.json", tmp_path / "out.csv")


def test_json_to_csv_invalid_json(tmp_path: Path) -> None:
    src = tmp_path / "broken.json"
    src.write_text("{not a json}", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(src, tmp_path / "out.csv")


def test_json_to_csv_empty_list(tmp_path: Path) -> None:
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(src, tmp_path / "out.csv")


def test_csv_to_json_invalid_extension(tmp_path: Path) -> None:
    src = tmp_path / "input.txt"
    src.write_text("data", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(src, tmp_path / "out.txt")


def test_csv_to_json_empty_file(tmp_path: Path) -> None:
    src = tmp_path / "empty.csv"
    src.write_text("\n", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(src, tmp_path / "out.json")


def test_csv_to_json_no_header(tmp_path: Path) -> None:
    src = tmp_path / "no_header.csv"
    src.write_text(",,\n1,2,3\n", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(src, tmp_path / "out.json")


def test_csv_to_json_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        csv_to_json(tmp_path / "missing.csv", tmp_path / "out.json")
