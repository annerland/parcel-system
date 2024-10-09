from .departments import MailDepartment, RegularDepartment, HeavyDepartment, InsuranceDepartment

class DepartmentFactory:
    def __init__(self):
        self.departments = {
            'mail': MailDepartment(),
            'regular': RegularDepartment(),
            'heavy': HeavyDepartment(),
            'insurance': InsuranceDepartment(),
        }

    def get_department(self, weight, value):
        if value > 1000:
            return self.departments['insurance']
        elif weight <= 1:
            return self.departments['mail']
        elif weight <= 10:
            return self.departments['regular']
        else:
            return self.departments['heavy']

