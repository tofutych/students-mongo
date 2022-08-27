from argparse import ArgumentError
from pymongo import MongoClient
from Singleton import Singleton
from bson.json_util import dumps
from typing import List
from bson.objectid import ObjectId


@Singleton
class Collection:
    """Синглтон класс.

    Инстанцирование приведет к созданию базы данных students_db. В созданной БД будет создана коллекция students.
    В классе реализовано базовые методы для работы с объектами.
    """

    def __init__(self) -> None:
        self.db_client = MongoClient("mongodb://localhost:27017")
        self.current_db = self.db_client["students_db"]
        self.collection = self.current_db["students"]

    def print_all(self) -> None:
        """Генератор, возвращающий информацию о каждом студенте."""
        for document in self.collection.find({}):
            yield document

    def insert_student(self, student: dict):

        """Добавляет студента в коллекцию."""
        try:
            self.collection.insert_one(student)
        except ArgumentError:
            print("Wrong argument!")

    def insert_students(self, students: List[dict]):
        """Добавляет список студентов в коллекцию."""
        try:
            self.collection.insert_many(students)
        except ArgumentError:
            print("Wrong argument!")

    def delete_student_by_id(self, id: str):
        """Удалить студента по id."""
        self.collection.delete_one({"_id": ObjectId(id)})
        print(1)

    def add_student_achievment(self, id: str, achievment: dict):
        """Добавляет заслугу студенту."""
        self.collection.update_one(
            {"_id": ObjectId(id)}, {"$push": {"achievments": achievment}}, upsert=True
        )

    def find_by_id(self, id: str):
        """Поиск записи по id."""
        return self.collection.find_one({"_id": ObjectId(id)})

    def dump(self, path: str = "./dumps/collection.json") -> None:
        """
        Сохранить копию коллекции в формате json.
        """
        cursor = self.collection.find({})

        with open(f"{path}", "w") as file:
            file.write("[")
            for document in cursor:
                file.write(dumps(document, ensure_ascii=False))
                file.write(",")
            file.write("]")
