# Лабораторная работа 7

## Содержимое
- `tests/test_text.py` — проверки `normalize`, `tokenize`, `count_freq`, `top_n` из `src/lib/text.py` с базовыми и граничными сценариями, а также проверкой сортировки при равной частоте.
- `tests/test_json_csv.py` — позитивные и негативные сценарии для `json_to_csv` и `csv_to_json` из `src/lab05/json_csv.py` с использованием временных файлов.
- `pyproject.toml` — конфигурация для `pytest` и `black`.

## Команды для проверки
```bash
# форматирование
black .

# автотесты
pytest -ra

# покрытие
pytest --cov=src --cov-report=term-missing
```
