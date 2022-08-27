from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    """Класс Student.

    Хранит в себе необходимые поля и методы экземпляра класса."""

    name: str
    speciality: str
    achievments: List[dict]

    def as_dict(self) -> dict:
        """Вернуть объект как словарь,
        чтобы потом добавить запись в коллекцию."""
        return {
            "name": self.name,
            "speciality": self.speciality,
            "achievments": self.achievments,
        }

    def add_achievment(self, achievment: dict):
        """Добавляет достижение в список достижений."""
        self.achievments.append(achievment)
