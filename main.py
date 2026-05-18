import random
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []
        self.avg = 0

    def __str__(self):
        return f"Ученик: {self.name} {self.surname}, Средний балл: {self.avg:.2f}"

    def grade_random(self, count = 5):
        self.grades = [random.randint(1,5) for _ in range(count)]
        self.calculate_average()

    def calculate_average(self):
        self.avg = sum(self.grades) / len(self.grades)

students = [
    Person("Василий", "Петров", 12),
    Person("Анна", "Сидорова", 14),
    Person("Иван", "Иванов", 13),
    Person("Елена", "Смирнова", 12),
    Person("Дмитрий", "Кузнецов", 15)
]

for i in students:
    i.grade_random()
    print(i)



# print(person)
#
# Добавить атрибут grades, в котором будет храниться список оценок.
# Создать список учеников, заполняя оценки случайными числами,
# и вывести информацию о них в порядке убывания среднего балла.
# Заполнение оценок и подсчёт среднего балла вынести в отдельные методы.