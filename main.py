from Student import Student
from MongoStudents import Collection


if __name__ == "__main__":
    collection = Collection.Instance()

    fedor = Student("Fedor", "02.03.02", [])
    achievment = {
        "title": "Выпрыгнул из окна 4 этажа",
        "date": "05.12.2018",
        "description": "Он выжил!",
    }
    fedor.add_achievment(achievment)
    collection.insert_student(fedor.as_dict())

    for note in collection.print_all():
        print(note)
