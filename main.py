def avg(values_dict):
    all_grades = []
    for grades in values_dict.values():
        all_grades += grades
    return sum(all_grades) / len(all_grades) if all_grades else 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        return avg(self.grades)

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average():.1f}"
        )

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average() < other.average()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average() == other.average()
        return NotImplemented



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
                isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        return avg(self.grades)

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average():.1f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average() < other.average()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average() == other.average()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
                isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )

def average_student_course(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]
    return sum(all_grades) / len(all_grades) if all_grades else 0

def average_lecturer_course(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]
    return sum(all_grades) / len(all_grades) if all_grades else 0

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']

lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'C++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}