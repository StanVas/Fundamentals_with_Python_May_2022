class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        Class.__students_count -= 1
        if Class.__students_count >= 0:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(list(map(int, self.grades))) / len(self.grades)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {Class.get_average_grade(self):.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
