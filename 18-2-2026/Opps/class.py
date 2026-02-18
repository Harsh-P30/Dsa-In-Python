# A CLASS is a blueprint or template for creating objects, encapsulating data (attributes) and methods (functions) that operate on that data. Ex   Class Family:

class Car:
    def __init__(self,brand,model):   # __init__ know as constructor and it is the method that call first before another
        self.brand = brand  # here self establish link with object and also know as contaxt
        self.model = model
        
    def full_name(self):
        return f"{self.brand}{self.model}"
        
my_car = Car("toyota","coralla")   # Object and it is an instance of a class.
print(my_car.brand)
print(my_car.full_name()) # to access/call function we have to add parenthesis()

