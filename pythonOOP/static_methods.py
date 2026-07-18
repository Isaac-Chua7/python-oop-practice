

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @staticmethod
    def is_valid_position(position):
        valid_positions = {"manager", "sales associate", "receptionist", "accountant", "customer support"}
        if position in valid_positions:
            return True
        else:
            return False

print(Employee.is_valid_position("manager")) #can execute without instantiating object

