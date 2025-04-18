class Pessoa:
    
    def __init__(self, nome: str, cpf: str, data_nasc: str):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if(not isinstance(valor, str) or (len(valor) > 50)):
            raise ValueError("Nome do candidato incompatível")
        else:
            self._nome = valor
            
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        if(not isinstance(valor, str) or len(valor) != 11 ):
            raise ValueError(f"Numero de cpf incompatível !! (tem tamanho {len(valor)})")
        else:
            self.__cpf = valor
            
    @property
    def data_nasc(self):
        return self.__data_nasc
    
    @data_nasc.setter
    def data_nasc(self, valor):
        if((isinstance(valor, str)) and len(valor) == 10):
            self.__data_nasc = valor
        else:
            raise ValueError(f"{self.nome} nao pode ser criado: Data incompatível {len(valor)}  ---- {valor}")