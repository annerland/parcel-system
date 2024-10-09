from abc import ABC, abstractmethod

class Department(ABC):
    @abstractmethod
    def process(self, parcel):
        pass

class MailDepartment(Department):
    def process(self, parcel):
        print(f"Processing parcel for {parcel['name']} by Mail Department")

class RegularDepartment(Department):
    def process(self, parcel):
        print(f"Processing parcel for {parcel['name']} by Regular Department")

class HeavyDepartment(Department):
    def process(self, parcel):
        print(f"Processing parcel for {parcel['name']} by Heavy Department")

class InsuranceDepartment(Department):
    def process(self, parcel):
        print(f"Processing parcel for {parcel['name']} by Insurance Department")