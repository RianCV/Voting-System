from abc import ABC, abstractmethod
from Urna.sistema.module_pessoa import Pessoa

class Candidato(Pessoa, ABC):
    
    def __init__(self, nome: str, cpf: str, data_nasc: str, num: str, partido: str, propostas: str):
        try:
            super().__init__(nome, cpf, data_nasc)
        except Exception as e:
            raise e
        self.numero = num
        self.partido = partido
        self.propostas = propostas
    
    @abstractmethod
    def _verifica_numero_cargo(self, valor, nome):
        pass
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor):
        if(self._verifica_numero_cargo(valor, "")):
            self.__numero = valor
            
    @property
    def propostas(self):
        return self.__propostas
    
    @propostas.setter
    def propostas(self, valor):
            self.__propostas = valor
            
    @property
    def partido(self):
        return self.__partido
    
    @partido.setter
    def partido(self, valor):
        self.__partido = valor