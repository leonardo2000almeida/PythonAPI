from src.model_.Person import Person

class Student(Person):
    registration_number: str

    def __init__(self, name: str, cpf: str, registration_number: str):
        super().__init__(name, cpf)
        self.name = name
        self.cpf = cpf
        self.registration_number = registration_number

    def getRegistrationNumber(self) -> str:
        return self.registration_number

    def setRegistrationNumber(self, registration_number: str):
        self.registration_number = registration_number
