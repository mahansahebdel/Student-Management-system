class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentManagementSystem:
    FILE_NAME = "students.txt"

    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            name = input("Enter student name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")

            age = int(input("Enter student age: "))
            if age <= 0:
                raise ValueError("Age must be a positive number.")
            elif 1300 < age < 1403:
                raise ValueError("Enter your age, not your birth year")

            grade = input("Enter student grade: ").strip()
            if not grade:
                raise ValueError("Grade cannot be empty.")

            student = Student(name, age, grade)
            self.students.append(student)

            
            with open(self.FILE_NAME, 'a') as file:
                file.write(f"{student.name},{student.age},{student.grade}\n")

            print("Student added successfully.\n")
        except ValueError as ve:
            print(f"Input Error: {ve}\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

    def view_students(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                print("\nSaved Students:")
                lines = file.readlines()
                if not lines:
                    print("No student records found.")
                for line in lines:
                    name, age, grade = line.strip().split(',')
                    print(f"Name: {name}, Age: {age}, Grade: {grade}")
            print()
        except FileNotFoundError:
            print("Student file not found. No data to show.\n")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}\n")

def main():
    function = StudentManagementSystem()

    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            function.add_student()
        elif choice == '2':
            function.view_students()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
