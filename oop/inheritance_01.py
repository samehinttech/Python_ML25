"""Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class
(called the child or subclass) to inherit attributes and methods from another class (called the
parent or superclass). This promotes code reusability and establishes a hierarchical relationship
between classes. IMPORTANT REMARKS: 1. Inheritance is defined by specifying the parent class in
parentheses after the child class name. 2. The child class inherits all attributes and methods
from the parent class, allowing it to use them as if they were defined in the child class itself.
3. The child class can override methods from the parent class to provide a specific
implementation. 4. The child class can also add new attributes and methods that are not present
in the parent class. 5. The `super()` function is used to call methods from the parent class,
allowing access to the parent class's methods and attributes. # from more than one parent class.
6. The `isinstance()` function can be used to check if an object is an instance of a specific
class or a subclass thereof. 7. The `issubclass()` function can be used to check if a class is a
subclass of another class."""


# Define the parent class
class Employee:
    def __init__(self, name, position, salary):
        # Initialize the attributes of the class
        self.name = name
        self.position = position
        self.salary = salary

    # Define a method to print employee name and position
    def work(self):
        print(f"{self.name} is working as a {self.position}.")

    # Define a method to print employee salary
    def get_salary(self):
        print(f"{self.name}'s salary is {self.salary}.")


# Define the child class that inherits from Employee
class Manager(Employee):
    # Initialize the Manager class with additional attributes
    def __init__(self, name, position, salary, department):
        # Call the constructor of the parent class
        super().__init__(name, position, salary)
        self.department = department  # New attribute for Manager class

    # Override the work method to provide a specific implementation for Manager
    def work(self):
        print(f"{self.name} is managing the {self.department} department.")

    # Define a new method specific to the Manager class
    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting in the {self.department} department.")


# Create an instance of the Employee class
employee1 = Employee("Sameh", "Developer", 60000)
# Call the work method from Employee class
employee1.work()
# Call the get_salary method from Employee class
employee1.get_salary()
print(f"Is employee1 an instance of Employee? {isinstance(employee1, Employee)}")  # True
print(f"Is employee1 an instance of Manager? {isinstance(employee1, Manager)}")  # False
print()
# Create an instance of the Manager class
manager1 = Manager("Hassan", "Project Manager", 80000, "IT")
# Call the overridden work method from Manager class
manager1.work()
# Call the get_salary method from Employee class (inherited)
manager1.get_salary()
# Call the conduct_meeting method from Manager class
manager1.conduct_meeting()