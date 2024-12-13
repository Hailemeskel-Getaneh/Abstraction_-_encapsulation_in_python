class Student:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name  # Private attribute
        self.__last_name = last_name    # Private attribute
        self._age = age                 # Private attribute (by convention)
    
    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be positive!")

# Create a Student object
student = Student("John", "Doe", 20)
print(student.get_full_name())  # Output: John Doe
