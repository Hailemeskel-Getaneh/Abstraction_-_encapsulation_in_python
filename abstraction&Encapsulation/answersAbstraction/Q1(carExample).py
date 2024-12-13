from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
    
    def stop_engine(self):
        print("Car engine stopped.")

# Testing the Car class
car = Car()
car.start_engine()
car.stop_engine()
