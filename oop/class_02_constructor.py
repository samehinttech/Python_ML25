"""Class constructor is a function called when an object is created. It is used to initialize the
attributes of the class. In Python, the constructor is defined using the `__init__` method. The
`__init__` method is called automatically when a new instance of the class is created. IMPORTANT
REMARKS: 1. The `__init__` method is a special method in Python classes. It is called a
constructor and is used to initialize the attributes of the class. 2. The `self` parameter in the
`__init__` method refers to the instance of the class itself. It is used to access variables and
methods associated with the current object. 3. You can define parameters in the `__init__` method
to pass values when creating an instance of the class. 4. The `__init__` method does not return
any value. It is used only for initialization. 5. You can create multiple instances (objects) of
a class, each with its own set of attributes initialized through the constructor. 6. If you do
not define an `__init__` method, Python will provide a default constructor that does nothing. 7.
You can also define default values for parameters in the `__init__` method. 8. The `__init__`
method can be overloaded by defining multiple constructors with different parameters using
default values or variable-length arguments."""


# Create again the Student class with a constructor
class Student:
    # Define the constructor with parameters
    def __init__(self, name, age):
        # Initialize the attributes of the class
        self.name = name  # Instance variable
        self.age = age  # Instance variable

    def attend_class(self):
        print(f"{self.name} is attending class...")

    def study(self):
        print(f"{self.name} is studying...")

    def take_exam(self):
        print(f"{self.name} is taking an exam...")


# Create instances (objects) of the Student class with parameters
student1 = Student("Sameh", 25)
student2 = Student("Hassan", 26)

# Call methods on the instances
student1.attend_class()
student1.study()
student1.take_exam()
print(f"Student Name: {student1.name}, Age: {student1.age}")
student2.attend_class()
student2.study()
student2.take_exam()
print(f"Student Name: {student2.name}, Age: {student2.age}")


# You can also create an instance without parameters if you define default values in the
# constructor Just like function parameters, you can define default values for the constructor
# parameters as per the next example
class Teacher:
    def __init__(self, name="Unknown", subject="Unknown"):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


# Create instances of the Teacher class
teacher1 = Teacher("Mr. Thomas", "Math")
teacher2 = Teacher()  # Uses default values
teacher1.teach()
teacher2.teach()
print(f"Teacher Name: {teacher1.name}, Subject: {teacher1.subject}")
print(f"Teacher Name: {teacher2.name}, Subject: {teacher2.subject}")