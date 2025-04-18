class Partido:
    def __init__(self, nome: str, cnpj: str, numero: str):
        self.nome = nome
        self.cnpj = cnpj
        self.numero = numero

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if len(valor) <= 50:
            self.__nome = valor
        else:
            raise ValueError(f"O nome do partido deve ter no máximo 50 caracteres, mas {self.nome} teve {len(valor)}")

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, valor: str):
        if len(valor) <= 14:
            self.__cnpj = valor
        else:
            raise ValueError(f"O CNPJ do partido deve ter um comprimento menor que 14, mas {self.nome} teve {len(self.cnpj)}")

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor: str):
        if len(valor) <= 2:
            self.__numero = valor
        else:
            raise ValueError(f"O número do partido deve ter no máximo 2 caracteres, mas {self.nome} teve {len(self.numero)}")