class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"Name: {self.name} Roll: {self.roll_number}, CGPA: {self.cgpa}"


def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


# Test the function with different input lists of students
students1 = [
        Student("Vasanth", "A001", 3.9),
        Student("Ranjith", "B002", 3.7),
        Student("Santhosh", "C003", 3.5),
        Student("Ragupathi", "D004", 3.2)
    ]
sorted_students1 = sort_students(students1)

for student in sorted_students1:
    print(student)
