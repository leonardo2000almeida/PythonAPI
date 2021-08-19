class Person(object):
    name: str
    cpf: str

    def __init__(self, name: str, cpf: str):
        self.name = name
        self.cpf = cpf

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getCpf(self) -> str:
        return self.cpf

    def setCpf(self, cpf: str):
        self.cpf = cpf
