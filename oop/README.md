
## Day 2 of Python revision.

# 🐍 Python OOP (Object-Oriented Programming) — Full Notes

## 📘 What is OOP?

**OOP (Object-Oriented Programming)** is a way of structuring code using **classes** and **objects**.  
It helps make code more modular, reusable, and easier to maintain.

---

## 🧩 Core Concepts of OOP in Python

1. **Class** — Blueprint for creating objects  
2. **Object** — Instance of a class  
3. **Encapsulation** — Hiding internal details and exposing only what’s necessary  
4. **Inheritance** — Reusing code by deriving new classes from existing ones  
5. **Polymorphism** — Same interface, different behavior for different objects  

---

## 🧠 1️⃣ Class and Object

A **class** defines properties (variables) and methods (functions).

```python
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I’m {self.age} years old.")

# creating objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.greet()
p2.greet()
```

**Output:**
```
Hello, my name is Alice and I’m 25 years old.
Hello, my name is Bob and I’m 30 years old.
```

---

## 🧬 2️⃣ Inheritance

**Inheritance allows one class (child) to acquire the properties and methods of another (parent).**

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # overriding
        print("Dog barks")

dog = Dog()
dog.speak()
```

**Output:**
```
Dog barks
```

---

## 🔒 3️⃣ Encapsulation

**Encapsulation is the process of **hiding private details** inside a class and controlling access using methods.**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
```

**Output:**
```
1500
```

> Private variables are prefixed with `__` (double underscore).

---

## 🎭 4️⃣ Polymorphism

**Polymorphism means “many forms” — the same method name can perform different actions depending on the object.**

```python
class Bird:
    def sound(self):
        print("Chirp")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Bird(), Dog()]:
    animal.sound()
```

**Output:**
```
Chirp
Bark
```

---

## 🚗 5️⃣ Example — All Concepts Together

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # call parent constructor
        self.model = model

    def drive(self):  # overriding
        print(f"{self.brand} {self.model} is driving smoothly!")

car1 = Car("Tesla", "Model S")
car1.drive()
```

**Output:**
```
Tesla Model S is driving smoothly!
```

---

## 🧭 Summary Table

| Concept | Meaning | Keyword / Example |
|----------|----------|------------------|
| **Class** | Blueprint for objects | `class Person:` |
| **Object** | Instance of a class | `p = Person()` |
| **Constructor** | Initializes attributes | `__init__()` |
| **Inheritance** | Reuse parent code | `class Dog(Animal)` |
| **Encapsulation** | Hide internal data | `self.__balance` |
| **Polymorphism** | Same name, different behavior | Method overriding |

---

## 🧰 Bonus — Built-in OOP Features in Python

- **`isinstance(obj, Class)`** → check if object belongs to class  
- **`issubclass(Child, Parent)`** → check if a class inherits another  
- **`super()`** → call parent methods  
- **Magic Methods** (like `__str__`, `__len__`, `__add__`) support operator overloading  

---

## 🧑‍💻 Practice Ideas

1. Create a **Student Management System** with `Student`, `Course`, and `Teacher` classes.  
2. Create a **Bank System** using `Account`, `SavingsAccount`, and `CurrentAccount`.  
3. Build a **Library System** with `Book`, `Member`, and `Library` classes.  

---

**End of Notes — Python OOP Summary** 🚀
