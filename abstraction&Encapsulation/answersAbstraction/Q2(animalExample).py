from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Concrete class
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
    def move(self):
        print("The dog is running.")

# Testing the Dog class
dog = Dog()
dog.make_sound()
dog.move()
