"""Classes are the backbone of Object-Oriented Programming (OOP) in Python, just like in many
other programming languages. A class is a blueprint for creating objects (a particular data
structure), providing initial values for state (member variables or attributes),
and implementations of behavior (member functions or methods).

IMPORTANT REMARKS: 1. Classes are defined using the `class` keyword. Naming conventions suggest
using CamelCase for class names. 2. The `__init__` method is a special method called a
constructor, which is automatically called when a new instance of the class is created. 3. The
`self` parameter in method definitions refers to the instance of the class itself. It is used to
access variables and methods associated with the current object. 4. Methods are functions defined
within a class that operates on instances of the class. 5. Attributes are variables that hold
data associated with a class and its instances. 6. You can create multiple instances (objects) of
a class, each with its own set of attributes. 7. Classes can also have class variables (shared
across all instances) and instance variables (unique to each instance)."""


# Define the class name, just a simple class
class Student:
    # Create a method (function) inside the class
    def attend_class(self):
        print("Attending class...")

    def study(self):
        print("Studying...")

    def take_exam(self):
        print("Taking an exam...")


# Create an instance (object) of the Student class
student1 = Student()
student2 = Student()

# Call methods on the instance
student1.attend_class()
student1.study()
student1.take_exam()
student2.attend_class()
student2.study()
student2.take_exam()

"""- We can add new attributes to the instance - Note that these attributes are not defined in 
the class itself, but we can add them dynamically to the instance - Note that this is the simple 
way to add attributes to an instance, but it's better to define them in the __init__ method"""
student1.name = "Sameh"
student1.age = 25
print(f"Student Name: {student1.name}, Age: {student1.age}")

# Each instance can have its own attributes
student2.name = "Hassan"
student2.age = 26
print(f"Student Name: {student2.name}, Age: {student2.age}")