class Person:
    def __init__(self, name, age):
        self.name = name   # Public attribute
        self.age = age     # Public attribute

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary  # Private attribute
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive!")

# Create a Teacher object
teacher = Teacher("Mr. Smith", 35, 50000)
print(teacher.name)           # Output: Mr. Smith
print(teacher.get_salary())   # Output: 50000
teacher.set_salary(55000)     # Update salary
print(teacher.get_salary())   # Output: 55000
