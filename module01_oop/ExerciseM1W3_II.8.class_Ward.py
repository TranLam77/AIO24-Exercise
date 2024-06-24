# Phần trắc nghiệm - Câu hỏi 8
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name:str, yob:int, grade:str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        return f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}"

class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        return f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}"

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}"

class Ward:
    def __init__(self, name:str):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person:Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                count += 1
            else :
                continue
        return count

ward1 = Ward(name="Ward1")
student1 = Student(name="studentA", yob=2010 , grade="7")
teacher1 = Teacher(name="teacherA", yob=1969 , subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995 , subject="History")
doctor1 = Doctor(name="doctorA", yob=1945 , specialist="Endocrinologists")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
assert ward1.count_doctor() == 1

doctor2 = Doctor(name ="doctorB", yob=1975, specialist="Cardiologists")
ward1.add_person(doctor2)
ward1.count_doctor()

# Đáp án là c) 2