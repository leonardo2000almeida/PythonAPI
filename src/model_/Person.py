class Person(object):
    name: str
    cpf: str

    def __init__(self, name: str, cpf: str):
        self.name = name
        self.cpf = cpf

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_cpf(self) -> str:
        return self.cpf

    def set_cpf(self, cpf: str):
        self.cpf = cpf
