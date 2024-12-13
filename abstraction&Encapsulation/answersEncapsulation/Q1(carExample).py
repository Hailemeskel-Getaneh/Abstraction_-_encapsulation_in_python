class Car:
    def __init__(self, make, model):
        self.make = make        # Public attribute
        self._model = model     # Private attribute (by convention)
    
    def get_model(self):
        return self._model
    
    def set_model(self, model):
        self._model = model

# Create a Car object
car = Car("Toyota", "Corolla")
print(car.make)             # Output: Toyota
print(car.get_model())      # Output: Corolla

# Set a new model
car.set_model("Camry")
print(car.get_model())      # Output: Camry
