import pytest

from src.lib.text import count_freq, normalize, tokenize, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source: str, expected: str) -> None:
    assert normalize(source) == expected


def test_normalize_empty() -> None:
    assert normalize("") == ""


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет, мир!", ["привет", "мир"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("повтор? повтор!", ["повтор", "повтор"]),
    ],
)
def test_tokenize_basic(source: str, expected: list[str]) -> None:
    assert tokenize(source) == expected


def test_count_freq_merges_yo() -> None:
    tokens = ["ёж", "еж", "ёж"]
    freq = count_freq(tokens)
    assert freq == {"еж": 3}


def test_count_freq_and_top_n_ordering() -> None:
    tokens = ["b", "a", "b", "c", "a", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_n_tie_breaker_sort_alphabetically() -> None:
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]


@pytest.mark.parametrize(
    "tokens, n, expected",
    [
        (["one"], 5, [("one", 1)]),
        (["x", "y", "z"], 0, []),
    ],
)
def test_top_n_respects_n(tokens: list[str], n: int, expected: list[tuple[str, int]]) -> None:
    freq = count_freq(tokens)
    assert top_n(freq, n) == expected
