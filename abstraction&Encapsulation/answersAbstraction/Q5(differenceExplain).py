from abc import ABC, abstractmethod

# Abstract class with an abstract method
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # No implementation

    def sleep(self):  # Regular method with implementation
        print("Sleeping...")

# Concrete class implementing the abstract method
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Testing the methods
dog = Dog()
dog.make_sound()  # Calls the implemented abstract method
dog.sleep()  # Calls the regular method
