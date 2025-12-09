from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from .models import Student


def students_to_json(students: Iterable[Student], path: str | Path) -> None:
    student_list: List[Student] = list(students)
    if not all(isinstance(student, Student) for student in student_list):
        raise TypeError("students_to_json expects an iterable of Student objects")

    data = [student.to_dict() for student in student_list]
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def students_from_json(path: str | Path) -> List[Student]:
    input_path = Path(path)
    with input_path.open(encoding="utf-8") as file:
        raw_data = json.load(file)

    if not isinstance(raw_data, list):
        raise ValueError("JSON file must contain a list of students")

    students: List[Student] = []
    for entry in raw_data:
        if not isinstance(entry, dict):
            raise ValueError("Each student entry must be an object")
        students.append(Student.from_dict(entry))

    return students


if __name__ == "__main__":
    demo_students = [
        Student("Иванов Иван", "2003-10-10", "БИВТ-21-1", 4.3),
        Student("Петров Петр", "2002-05-12", "БИВТ-21-2", 4.7),
    ]
    output = Path("data/lab08/students_demo.json")
    students_to_json(demo_students, output)
    print(f"Saved {len(demo_students)} students to {output}")
    loaded = students_from_json(output)
    print("Loaded:")
    for student in loaded:
        print(" -", student)
