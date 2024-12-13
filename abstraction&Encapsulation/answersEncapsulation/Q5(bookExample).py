class Book:
    def __init__(self, title, author, price):
        self.title = title    # Public attribute
        self.author = author  # Public attribute
        self.__price = price  # Private attribute
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive!")

# Create a Book object
book = Book("Python Programming", "John Doe", 29.99)
print(book.get_price())      # Output: 29.99
book.set_price(34.99)        # Update price
print(book.get_price())      # Output: 34.99
