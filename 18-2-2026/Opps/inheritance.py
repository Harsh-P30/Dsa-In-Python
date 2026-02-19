# Inheritance 

class Parent:
    def __init__(self,name):
        self.name=name
    def Return(self):
        return self.name
    
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)  # super is a function that connect parent class to child and give access
        self.age=age
        
    def Return(self):
        return f"{self.name} {self.age}"
    
class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address
        
    def Info(self):
        return f"{self.name} {self.age} {self.address}"
    
    
child = Child("harsh",45)
print(child.Return())


info = GrandChild("Harsh",45, "Rakh")
print(info.Info())