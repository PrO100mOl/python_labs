from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any, Dict


@dataclass
class Student:
    fio: str
    birthdate: str  # expected format YYYY-MM-DD
    group: str
    gpa: float
    _birthdate_date: date = field(init=False, repr=False)

    def __post_init__(self) -> None:
        try:
            parsed_birthdate = date.fromisoformat(self.birthdate)
        except (TypeError, ValueError) as exc:
            raise ValueError("birthdate must be in YYYY-MM-DD format") from exc

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

        self._birthdate_date = parsed_birthdate

    def age(self) -> int:
        today = date.today()
        years = today.year - self._birthdate_date.year
        if (today.month, today.day) < (self._birthdate_date.month, self._birthdate_date.day):
            years -= 1
        return years

    def to_dict(self) -> Dict[str, Any]:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        required_keys = {"fio", "birthdate", "group", "gpa"}
        if not required_keys.issubset(data):
            missing = required_keys - set(data)
            raise ValueError(f"Missing fields for Student: {', '.join(sorted(missing))}")

        try:
            fio = str(data["fio"])
            birthdate = str(data["birthdate"])
            group = str(data["group"])
            gpa = float(data["gpa"])
        except (TypeError, ValueError) as exc:
            raise ValueError("Invalid field types for Student") from exc

        return cls(fio=fio, birthdate=birthdate, group=group, gpa=gpa)

    def __str__(self) -> str:
        return f"{self.fio} ({self.group}) — born {self.birthdate}, GPA: {self.gpa:.2f}"


if __name__ == "__main__":
    example_student = Student(
        fio="Иванов Иван",
        birthdate="2003-10-10",
        group="БИВТ-21-1",
        gpa=4.5,
    )
    print(example_student)
    print(f"Age: {example_student.age()}")
    print("As dict:", example_student.to_dict())
