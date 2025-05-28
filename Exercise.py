"""
Exercise:
Submit your work on github for Method overriding, method overloading, and MRO.
MRO is Method Resolution Order, which is the order.
I need two real world examples of each of the above concepts.
"""


# Method Overriding - Example 1

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak() 


# Method Overriding - Example 2

class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

dev = Developer()
dev.work()  


# Method Overloading - Example 1

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))      
print(calc.add(2, 3, 4))   


# Method Overloading - Example 2

class Greeter:
    def greet(self, *names):
        if not names:
            print("Hello!")
        else:
            for name in names:
                print(f"Hello, {name}!")

g = Greeter()
g.greet()               
g.greet("Andrew")         
g.greet("Fahad", "Abdul")    


# MRO (Method Resolution Order) - Example 1

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  
print(D.__mro__) 


# MRO (Method Resolution Order) - Example 2

class Device:
    def start(self):
        print("Device starts")

class Phone(Device):
    def start(self):
        print("Phone starts")

class Camera(Device):
    def start(self):
        print("Camera starts")

class SmartPhone(Phone, Camera):
    pass

sp = SmartPhone()
sp.start()  
print(SmartPhone.__mro__) 