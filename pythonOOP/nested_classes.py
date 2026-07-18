
class Company:
    def __init__(self, company_name, location):
        self.name = company_name
        self.location = location
        self.employees = []

    class Employee:
        def __init__(self, name, position, salary):
            self.name = name
            self.position = position
            self.salary = salary
    
    def add_new_employee(self, name, position, salary):
        new_employee = self.Employee(name, position, salary)
        self.employees.append(new_employee)

    def list_employees(self):
        print(f"Employees at {self.name}, {self.location}:")
        for e in self.employees:
            print(f"Employee: {e.name}, {e.position}, Salary: {e.salary}")


c1 = Company(company_name="Dunder Mifflin", location="Scranton")

c1.add_new_employee(name="Micheal Scott", position="Manager", salary="120,000")
c1.add_new_employee(name="Pam Beasly", position="Receptionist", salary="60,000")
c1.add_new_employee(name="Jim Halpert", position="Sales Associate", salary="70,000")
c1.add_new_employee(name="Angela Martin", position="Accountant", salary="70,000")
c1.add_new_employee(name="Toby Flenderson", position="H.R. Representative", salary="80,000")

c1.list_employees()
