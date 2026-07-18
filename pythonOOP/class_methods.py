
class Employee:
    number_of_employees = 0 
    total_salary = 0

    def __init__(self, name, salary):
        self.name = name 
        self. salary = salary
        Employee.total_salary += salary
        Employee.number_of_employees += 1

    @classmethod
    def get_average_salary(cls):
        if cls.number_of_employees == 0:
            return 0
        else:
            return cls.total_salary/cls.number_of_employees
        

e1 = Employee("Michael Scott", 80000)
e2 = Employee("Kevin Malone", 50000)
e3 = Employee("Creed Bratton", 90000)

print(f"Average Salary: ${Employee.get_average_salary(): 0.2f} USD")
