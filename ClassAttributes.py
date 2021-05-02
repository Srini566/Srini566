class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: %s" % self.name, ", Salary: %d" % self.salary)


emp1 = Employee("Zaara", 2000)
emp1.displayEmployee()

emp2 = Employee("Minni", 5000)
emp2.displayEmployee()

print("Total Employee: %d" % Employee.empCount)

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)