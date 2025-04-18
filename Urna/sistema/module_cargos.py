from Urna.sistema.module_candidato import Candidato

class Presidente(Candidato):
    
    def __init__(self, nome: str, cpf: str, data_nasc: str, num: str, partido: str, propostas: str):
        self._verifica_numero_cargo(num, nome)
        try:
            super().__init__(nome, cpf, data_nasc, num, partido, propostas)
        except Exception as e:
            raise e
        
    def _verifica_numero_cargo(self, valor, nome):
        if len(valor) == 2:
            return True
        else:
            raise NumCandidatoError(f'{nome} tem numero com {str(len(valor))} digitos, mas Presidente recebe 2')

class Governador(Candidato):
    def __init__(self, nome: str, cpf: str, data_nasc: str, num: str, partido: str, propostas: str):
        self._verifica_numero_cargo(num, nome)
        super().__init__(nome, cpf, data_nasc, num, partido, propostas)
        
    def _verifica_numero_cargo(self, valor, nome):
        if len(valor) == 2:
            return True
        else:
            raise NumCandidatoError(f'{nome} tem numero com {str(len(valor))} digitos, mas Governador recebe 2')
        
class DepFederal(Candidato):
    def __init__(self, nome: str, cpf: str, data_nasc: str, num: str, partido: str, propostas: str):
        self._verifica_numero_cargo(num, nome)
        super().__init__(nome, cpf, data_nasc, num, partido, propostas)
        
        
    def _verifica_numero_cargo(self, valor, nome):
        if len(valor) == 4:
            return True
        else:
            raise NumCandidatoError(f'{nome} tem numero com {str(len(valor))} digitos, mas DepFederal recebe 4')
        
class DepEstadual(Candidato):
    def __init__(self, nome: str, cpf: str, data_nasc: str, num: str, partido: str, propostas: str):
        self._verifica_numero_cargo(num, nome)
        super().__init__(nome, cpf, data_nasc, num, partido, propostas)
        
        
    def _verifica_numero_cargo(self, valor, nome):
        if len(valor) == 5:
            return True
        else:
            raise NumCandidatoError(f'{nome} tem numero com {str(len(valor))} digitos, mas DepEstadual recebe 5')
        
class Senador(Candidato):
    def __init__(self, nome: str, cpf: str, data_nasc: str, num: str, partido: str, propostas: str):
        self._verifica_numero_cargo(num, nome)
        super().__init__(nome, cpf, data_nasc, num, partido, propostas)
        
    def _verifica_numero_cargo(self, valor, nome):
        if len(valor) == 3:
            return True
        else:
            raise NumCandidatoError(f'{nome} tem numero com {str(len(valor))} digitos, mas Senador recebe 3')
        
class NumCandidatoError(Exception):
    def __init__(self, msg):
        self.__dado = msg
        
    def __str__(self):
        return "Numero do candidato incompativel: " + self.__dado