from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List

from src.lab08.models import Student


class Group:

    header = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str | Path):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            with self.path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(self.header)

    def _validate_header(self, fieldnames: Iterable[str] | None) -> None:
        if list(fieldnames or []) != self.header:
            raise ValueError(
            )

    def _read_all(self) -> List[Student]:
        with self.path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self._validate_header(reader.fieldnames)
            students: List[Student] = []
            for row in reader:
                if not row:
                    continue
                students.append(
                    Student.from_dict(
                        {
                            "fio": row.get("fio", ""),
                            "birthdate": row.get("birthdate", ""),
                            "group": row.get("group", ""),
                            "gpa": row.get("gpa", 0),
                        }
                    )
                )
            return students

    def _write_students(self, students: Iterable[Student]) -> None:
        with self.path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.header)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())

    def list(self) -> List[Student]:

        return self._read_all()

    def add(self, student: Student) -> None:

        if not isinstance(student, Student):
            raise TypeError("add() expects a Student instance")

        students = self._read_all()
        students.append(student)
        self._write_students(students)

    def find(self, substr: str) -> List[Student]:

        needle = substr.lower()
        return [s for s in self._read_all() if needle in s.fio.lower()]

    def remove(self, fio: str) -> int:

        students = self._read_all()
        remaining = [s for s in students if s.fio != fio]
        removed = len(students) - len(remaining)
        if removed:
            self._write_students(remaining)
        return removed

    def update(self, fio: str, **fields) -> bool:

        students = self._read_all()
        updated = False
        for idx, student in enumerate(students):
            if student.fio == fio:
                data = student.to_dict()
                data.update(fields)
                students[idx] = Student.from_dict(data)
                updated = True
                break
        if updated:
            self._write_students(students)
        return updated

    def stats(self) -> dict:

        students = self._read_all()
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        gpas = [s.gpa for s in students]
        groups_count: dict[str, int] = {}
        for student in students:
            groups_count[student.group] = groups_count.get(student.group, 0) + 1

        top_students = sorted(students, key=lambda s: s.gpa, reverse=True)[:5]
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups_count,
            "top_5_students": [
                {"fio": s.fio, "gpa": s.gpa} for s in top_students
            ],
        }


if __name__ == "__main__":
    demo_path = Path("data/lab09/students_demo.csv")
    group = Group(demo_path)

    group._write_students([]) 
    group.add(Student("Иванов Иван", "2003-10-10", "БИВТ-21-1", 4.3))
    group.add(Student("Петров Петр", "2002-05-12", "БИВТ-21-2", 4.7))
    group.add(Student("Сидорова Анна", "2004-07-01", "БИВТ-21-1", 4.9))

    print("All students:")
    for s in group.list():
        print(" -", s)

    print("\nFind 'Иван':")
    for s in group.find("Иван"):
        print(" *", s)

    print("\nUpdating GPA for Петров Петр to 4.9...")
    group.update("Петров Петр", gpa=4.9)
    print("Updated entry:")
    for s in group.find("Петров"):
        print(" *", s)

    print("\nRemoving Сидорова Анна")
    group.remove("Сидорова Анна")
    for s in group.list():
        print(" -", s)

    print("\nStats:")
    print(group.stats())
