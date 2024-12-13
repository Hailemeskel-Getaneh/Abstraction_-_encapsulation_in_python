![Example Image](../images/abstraction.jpg)



---

# **Abstraction in Python**

## **What is Abstraction?**

Abstraction is a way to hide the implementation details of a system and show only the essential features to the user. It focuses on **what an object can do** rather than **how it does it**.  

In Python, abstraction is implemented using **abstract classes** and **abstract methods**.

---

### **Why Use Abstraction?**
1. **Simplifies Complexity**: Users only see what’s necessary.  
2. **Increases Flexibility**: The implementation can be changed without affecting the user.  
3. **Promotes Reusability**: Common functionality is defined in a base class for reuse.  
4. **Ensures Consistency**: All derived classes follow the same structure.

---

## **How to Implement Abstraction in Python?**

Abstraction in Python is achieved using the `ABC` module (short for *Abstract Base Classes*).

### **Steps to Implement Abstraction**

1. Import the `ABC` module.  
2. Create a class that inherits from `ABC`.  
3. Use the `@abstractmethod` decorator to declare abstract methods.

---

### **Example: Abstraction in a Student Management System**

Let’s create a simple example of abstraction to demonstrate a **Student Management System**.

#### **Step 1: Create an Abstract Base Class**

We create an abstract class `Student` to define the basic structure of a student. This includes methods like `enroll()` and `get_grade()` but without their implementation.

```python
from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def enroll(self):
        pass

    @abstractmethod
    def get_grade(self):
        pass
```

- **Abstract Class (`Student`)**: Cannot be instantiated directly.
- **Abstract Methods (`enroll`, `get_grade`)**: Must be implemented by subclasses.

---

#### **Step 2: Create Subclasses**

We now create specific types of students, each providing its own implementation of the abstract methods.

```python
class Undergraduate(Student):
    def enroll(self):
        return f"{self.name} has enrolled in an undergraduate course."

    def get_grade(self):
        return f"{self.name}'s grade: A"

class Graduate(Student):
    def enroll(self):
        return f"{self.name} is working on a research topic."

    def get_grade(self):
        return f"{self.name}'s grade: A+"
```

- **Undergraduate**: Enrolls in courses and gets grades.  
- **Graduate**: Focuses on research and gets grades.

---

#### **Step 3: Use the Subclasses**

Now we create objects of the `Undergraduate` and `Graduate` classes and call their methods.

```python
ug_student = Undergraduate("Alice", 20)
grad_student = Graduate("Bob", 25)

print(ug_student.enroll())  # Alice has enrolled in an undergraduate course.
print(ug_student.get_grade())  # Alice's grade: A

print(grad_student.enroll())  # Bob is working on a research topic.
print(grad_student.get_grade())  # Bob's grade: A+
```

---

## **Key Points to Remember**
1. An abstract class cannot be instantiated directly.
2. Abstract methods in the base class must be implemented in the derived class.
3. Abstraction focuses on what an object does, not how it does it.
4. Use the `ABC` module to define abstract classes in Python.

---

## **5 Practice Questions**

1. **Question 1**:  
   Create an abstract class `Vehicle` with methods `start_engine()` and `stop_engine()`. Then create a `Car` class that implements these methods.

2. **Question 2**:  
   Write a program to create an abstract class `Animal` with methods `make_sound()` and `move()`. Implement these in a `Dog` class.

3. **Question 3**:  
   Define an abstract class `Shape` with a method `area()`. Implement this method in `Circle` and `Square` classes.

4. **Question 4**:  
   Create an abstract class `BankAccount` with methods `deposit()` and `withdraw()`. Implement these in a `SavingsAccount` class.

5. **Question 5**:  
   Explain the difference between an abstract method and a regular method. Give an example to demonstrate.

---
---
-----