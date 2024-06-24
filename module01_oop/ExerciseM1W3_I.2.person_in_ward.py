# class Ward
class Ward():
    def __init__(self, name):
        self.name = name
        self.person_list = []

    def add_person(self, person):
        self.person_list.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        for person in self.person_list:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.person_list:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.person_list.sort(key=lambda x: x.yob)

    def compute_average(self):
        total = 0
        number = 0
        for person in self.person_list:
            if isinstance(person, Teacher):
                total += person.yob
                number += 1
        if number == 0:
            return 0
        return total / number

# class Student
class Student():
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

# class Teacher
class Teacher():
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")

# class Doctor
class Doctor():
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")

# test
student1 = Student('Lam',2000,12)
student1.describe()

teacher1 = Teacher('Oanh',1990,'Math')
teacher1.describe()

teacher2 = Teacher('Phuong',1995,'Physics')
teacher2.describe()

doctor1 = Doctor('Minh',1980,'Neurology')
doctor1.describe()

doctor2 = Doctor('Khánh',1993,'Heart')
doctor2.describe()

ward1 = Ward('Trần Phú')
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors: {ward1.count_doctor()}")

print(f"\nAfter sort age of people in Ward {ward1.name}")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
