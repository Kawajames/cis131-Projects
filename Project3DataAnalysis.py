# File Name: Project3DataAnalysis4.py
# Description: Reads employee and student data from files, displays data per user menu
#              and student academic scores.
# Author: Dakota Kartchner
# Date: 4/30/2025

from abc import ABC, abstractmethod
from datetime import date
import os
import sys

# Set base directory where the text files are stored
base_dir = r"C:\Users\dkawa\Desktop\Project1Employees4"

# Base Class
class Person(ABC):
    @abstractmethod
    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        if isinstance(idNumber, int) and 1000 <= idNumber <= 9999:
            self.idNumber = idNumber
        else:
            raise ValueError("ID must be a 4-digit integer")
        self.emailAddress = emailAddress
        if len(phoneNumber) <= 12:
            self.phoneNumber = phoneNumber
        else:
            raise ValueError("Phone number must be 12 characters or less")

    def __str__(self):
        return f"{self.lastName}, {self.firstName} (ID: {self.idNumber})"

    def __repr__(self):
        return (f"Person({self.firstName!r}, {self.lastName!r}, {self.idNumber!r}, "
                f"{self.emailAddress!r}, {self.phoneNumber!r})")

# Employee Class
class Employee(Person):
    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full", "002": "Part"}

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber,
                 hireDate, classificationValue, roleValue, annualSalary):
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)
        self.hireDate = hireDate
        self.classificationPerson = self._get_key(Employee.classificationDictionary, classificationValue)
        self.rolePerson = self._get_key(Employee.roleDictionary, roleValue)
        if self.classificationPerson is None or self.rolePerson is None:
            raise ValueError("Invalid classification or role")
        if annualSalary < 0:
            raise ValueError("Salary cannot be negative")
        self.annualSalary = round(annualSalary, 2)

    @staticmethod
    def _get_key(dictionary, value):
        for key, val in dictionary.items():
            if val.lower() == value.lower():
                return key
        return None

    def __str__(self):
        d = self.hireDate
        return (f"{self.lastName}, {self.firstName} (ID: {self.idNumber}) | "
                f"{d.month}/{d.day}/{d.year} | {Employee.classificationDictionary[self.classificationPerson]} | "
                f"{Employee.roleDictionary[self.rolePerson]} | Salary: {self.annualSalary:,.2f}")

    def __repr__(self):
        return (f"Employee({self.firstName!r}, {self.lastName!r}, {self.idNumber!r}, "
                f"{self.emailAddress!r}, {self.phoneNumber!r}, {self.hireDate!r}, "
                f"{self.classificationPerson!r}, {self.rolePerson!r}, {self.annualSalary!r})")

# Student Class
class Student(Person):
    # list of courses to track scores for
    courseNameList = ["Art", "Greek", "Latin", "Science", "Mathematics"]

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)
        # dict mapping course names to scores
        self.coursesStudentDict = {}

    def getAcademicData(self):
        # Returns list of strings: LastName, FirstName, ID, then scores in courseNameList order
        data = [self.lastName, self.firstName, str(self.idNumber)]
        for course in Student.courseNameList:
            score = self.coursesStudentDict.get(course, 0)
            data.append(str(score))
        return data

    def __repr__(self):
        return (f"Student({self.firstName!r}, {self.lastName!r}, {self.idNumber!r}, "
                f"{self.emailAddress!r}, {self.phoneNumber!r}, {self.coursesStudentDict!r})")

# Lists to hold data
employeeList = []
studentList = []

# Functions to Read Data
def getEmployees():
    print("\nAdding employees\n")
    try:
        with open(os.path.join(base_dir, "employees.txt"), "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: 'employees.txt' file not found.")
        sys.exit(1)

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 9:
            continue
        try:
            lastName, firstName = parts[0], parts[1]
            idNumber = int(parts[2])
            emailAddress = parts[3]
            phoneNumber = parts[4]
            m, d, y = map(int, parts[5].split("/"))
            hireDate = date(y, m, d)
            classification, role, salary = parts[6], parts[7], float(parts[8])
            emp = Employee(firstName, lastName, idNumber, emailAddress, phoneNumber,
                           hireDate, classification, role, salary)
            employeeList.append(emp)
            print(f"Added employee {firstName} {lastName}")
        except Exception as e:
            print(f"Skipping record due to error: {e}")


def getStudents():
    print("\nAdding students\n")
    try:
        with open(os.path.join(base_dir, "students.txt"), "r") as file:
            lines = file.readlines()[1:]
    except FileNotFoundError:
        print("Error: 'students.txt' file not found.")
        sys.exit(1)

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 5:
            continue
        try:
            lastName, firstName = parts[0], parts[1]
            idNumber = int(parts[2])
            emailAddress = parts[3]
            phoneNumber = parts[4]
            stu = Student(firstName, lastName, idNumber, emailAddress, phoneNumber)
            studentList.append(stu)
            print(f"Added student {firstName} {lastName}")
        except Exception as e:
            print(f"Skipping record due to error: {e}")


def getStudentScores():
    print("\nAdding student scores\n")
    try:
        with open(os.path.join(base_dir, "scores.txt"), "r") as file:
            lines = file.readlines()[1:]
    except FileNotFoundError:
        print("Error: 'scores.txt' file not found.")
        sys.exit(1)

    # map id to students object for quicker lookup
    student_dict = {stu.idNumber: stu for stu in studentList}
    for line in lines:
        parts = line.strip().split()
        if len(parts) < len(Student.courseNameList) + 1:
            continue
        try:
            idNumber = int(parts[0])
            scores = list(map(int, parts[1:1 + len(Student.courseNameList)]))
            stu = student_dict.get(idNumber)
            if stu:
                for course, score in zip(Student.courseNameList, scores):
                    if course in Student.courseNameList:
                        stu.coursesStudentDict[course] = score
                print(f"Added scores for {stu.firstName} {stu.lastName}")
        except Exception as e:
            print(f"Skipping record due to error: {e}")

# Display Functions
def displayEmployment():
    print("\nEmployee Employment Information\n")
    header = (f"{'LastName':15}{'FirstName':15}{'ID':8}{'Email':30}" \
              f"{'Phone':15}{'HireDate':12}{'Classif':15}{'Role':10}{'Salary':10}")
    print(header)
    print("-" * len(header))
    for emp in employeeList:
        hd = f"{emp.hireDate.month}/{emp.hireDate.day}/{emp.hireDate.year}"
        classification = Employee.classificationDictionary.get(emp.classificationPerson, "N/A")
        role = Employee.roleDictionary.get(emp.rolePerson, "N/A")
        print(f"{emp.lastName:15}{emp.firstName:15}{emp.idNumber:<8}{emp.emailAddress:30}"\
              f"{emp.phoneNumber:15}{hd:12}{classification:15}{role:10}{emp.annualSalary:10.2f}")


def displayEmployeeContact():
    print("\nEmployee Contact Information\n")
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}{'Email':30}{'Phone':15}"
    print(header)
    print("-" * len(header))
    for emp in employeeList:
        print(f"{emp.lastName:15}{emp.firstName:15}{emp.idNumber:<8}{emp.emailAddress:30}{emp.phoneNumber:15}")


def displayStudentContact():
    print("\nStudent Contact Information\n")
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}{'Email':30}{'Phone':15}"
    print(header)
    print("-" * len(header))
    for stu in studentList:
        print(f"{stu.lastName:15}{stu.firstName:15}{stu.idNumber:<8}{stu.emailAddress:30}{stu.phoneNumber:15}")


def displayAllContacts():
    print("\nAll Person Contact Information\n")
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}{'Email':30}{'Phone':15}"
    print(header)
    print("-" * len(header))
    for person in employeeList + studentList:
        print(f"{person.lastName:15}{person.firstName:15}{person.idNumber:<8}{person.emailAddress:30}{person.phoneNumber:15}")


def displayStudentScores():
    print("\nStudent Academic Scores\n")
    # header
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}"
    for course in Student.courseNameList:
        header += f"{course:12}"
    print(header)
    print("-" * len(header))
    # rows
    for stu in studentList:
        data = stu.getAcademicData()
        row = f"{data[0]:15}{data[1]:15}{data[2]:<8}"
        for score in data[3:]:
            row += f"{score:<12}"
        print(row)

def getStudentAcademicReport(student):
    scores = [student.coursesStudentDict.get(course, 0) for course in Student.courseNameList]
    high = max(scores)
    low = min(scores)
    average = round(sum(scores) / len(scores), 1)
    grade = ("A" if average >= 90 else
             "B" if average >= 80 else
             "C" if average >= 70 else
             "D" if average >= 60 else "F")
    return [student.lastName, student.firstName, student.idNumber] + scores + [high, low, average, grade]

def displayFullStudentAcademicReport():
    print("\nFull Student Academic Report\n")
    # Header
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}"
    for course in Student.courseNameList:
        header += f"{course:12}"
    header += f"{'High':8}{'Low':8}{'Average':10}{'Grade':6}"
    print(header)
    print("-" * len(header))
    
    # Student data rows
    for stu in studentList:
        data = getStudentAcademicReport(stu)
        row = f"{data[0]:15}{data[1]:15}{data[2]:<8}"
        for score in data[3:-4]:
            row += f"{score:<12}"
        row += f"{data[-4]:<8}{data[-3]:<8}{data[-2]:<10}{data[-1]:<6}"
        print(row)

    # Summary statistics
    print()
    print(f"{'High':<30}", end="")
    for course in Student.courseNameList:
        scores = [stu.coursesStudentDict.get(course, 0) for stu in studentList]
        print(f"{max(scores):<12}", end="")
    print()

    print(f"{'Low':<30}", end="")
    for course in Student.courseNameList:
        scores = [stu.coursesStudentDict.get(course, 0) for stu in studentList]
        print(f"{min(scores):<12}", end="")
    print()

    print(f"{'Average':<30}", end="")
    for course in Student.courseNameList:
        scores = [stu.coursesStudentDict.get(course, 0) for stu in studentList]
        avg = round(sum(scores) / len(scores), 1)
        print(f"{avg:<12}", end="")
    print()

def displayIndividualStudentReport():
    print("\nIndividual Student Academic Report\n")
    try:
        studentID = int(input("Enter Student ID (-1 to exit): ").strip())
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return

    if studentID == -1:
        return

    student = next((s for s in studentList if s.idNumber == studentID), None)
    if not student:
        print("That is not an ID we have on record.")
        return

    # Header
    header = f"{'LastName':15}{'FirstName':15}{'ID':8}"
    for course in Student.courseNameList:
        header += f"{course:12}"
    header += f"{'High':8}{'Low':8}{'Average':10}{'Grade':6}"
    print(header)
    print("-" * len(header))

    # Report row
    data = getStudentAcademicReport(student)
    row = f"{data[0]:15}{data[1]:15}{data[2]:<8}"
    for score in data[3:-4]:
        row += f"{score:<12}"
    row += f"{data[-4]:<8}{data[-3]:<8}{data[-2]:<10}{data[-1]:<6}"
    print(row)
    
# Menu Function
def createMenu():
    while True:
        print("\nPlease select an option below\n")
        print("1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        print("4. Display Student Contact Information")
        print("5. Display All Person Contact Information")
        print("6. Display Full Academic Report")
        print("7. Display Academic Report for one Student")
        print("8. Display Honor Roll")
        choice = input("\n> ").strip()

        if choice == "1":
            print("\nThank you for using the system.\nNow exiting the program.")
            sys.exit(0)
        elif choice == "2":
            displayEmployment()
        elif choice == "3":
            displayEmployeeContact()
        elif choice == "4":
            displayStudentContact()
        elif choice == "5":
            displayAllContacts()
        elif choice == "6":
            displayFullStudentAcademicReport()
        elif choice == "7":
            lookUpStudentAcademicRecord()
        elif choice == "8":
            getHonorRoll()
        else:
            print(f"\nI am sorry, {choice} is not an option.")

# Main Function
def main():
    print("Starting application…")
    getEmployees()
    getStudents()
    getStudentScores()
    createMenu()

if __name__ == "__main__":
    main()
