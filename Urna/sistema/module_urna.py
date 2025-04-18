from Urna.sistema.module_votacao import Votacao
from Urna.sistema.module_cargos import *
# from Urna.sistema.module_cargos import Governador
# from Urna.sistema.module_presidente import Presidente
# from Urna.sistema.module_depFederal import DepFederal
# from Urna.sistema.module_depEstadual import DepEstadual
# from Urna.sistema.module_senador import Senador


class Urna():
    def __init__(self):
        self._id_urna = None
        self._votos = []
        self._dict_votos = {
            "Governador": {},
            "Presidente": {},
            "DepFederal": {},
            "DepEstadual": {},
            "Senador": {}
        }
    
            
    def carrega_urna(self, caminho_arq):
        with open(caminho_arq, 'r') as file:
            lines = file.readlines()
            second_line = lines[1]
            self._id_urna = second_line.split(',')[0][16:]
            for line in lines:
                if("adicionar_voto" in line):
                    splitted_line = line.split(',')
                    id_votacao = splitted_line[1][1:]
                    depEstadual = splitted_line[2][1:]
                    depFederal = splitted_line[3][1:]
                    senador = splitted_line[4][1:]
                    governador = splitted_line[5][1:]
                    presidente = splitted_line[6][1:].rstrip('\n')
                    self._votos.append(Votacao(id_votacao,depEstadual,depFederal,senador,governador,presidente))
        
    def imprime_boletim(self, candidatos_lst: list):
        result = f"-----------------BOLETIM DA URNA {self._id_urna}----------------\n\n"
        result += 'Governador: \n'
        for candidato in candidatos_lst:
            if(isinstance(candidato, Governador)):
                count = 0
                for voto in self._votos:
                    if((voto.governador == candidato.numero)):
                        count += 1
                #adicionar em dicionario
                self._dict_votos["Governador"][candidato.nome] = count
                result += f" Candidato {candidato.nome} (Numero {candidato.numero}) recebeu {count} votos\n"
        result += 'Presidente: \n'
        for candidato in candidatos_lst:
            if(isinstance(candidato, Presidente)):
                count = 0
                for voto in self._votos:
                    if((voto.presidente == candidato.numero)):
                        count += 1
                self._dict_votos["Presidente"][candidato.nome] = count
                result += f" Candidato {candidato.nome} (Numero {candidato.numero}) recebeu {count} votos\n"
        result += 'DepFederal: \n'
        for candidato in candidatos_lst:
            if(isinstance(candidato, DepFederal)):
                count = 0
                for voto in self._votos:
                    if((voto.depFederal == candidato.numero)):
                        count += 1
                self._dict_votos["DepFederal"][candidato.nome] = count
                result += f" Candidato {candidato.nome} (Numero {candidato.numero}) recebeu {count} votos\n"
        result += 'DepEstadual: \n'
        for candidato in candidatos_lst:
            if(isinstance(candidato, DepEstadual)):
                count = 0
                for voto in self._votos:
                    if((voto.depEstadual == candidato.numero)):
                        count += 1
                self._dict_votos["DepEstadual"][candidato.nome] = count
                result += f" Candidato {candidato.nome} (Numero {candidato.numero}) recebeu {count} votos\n"
        result += 'Senador: \n'
        for candidato in candidatos_lst:
            if(isinstance(candidato, Senador)):
                count = 0
                for voto in self._votos:
                    if((voto.senador == candidato.numero)):
                        count += 1
                self._dict_votos["Senador"][candidato.nome] = count
                result += f" Candidato {candidato.nome} (Numero {candidato.numero}) recebeu {count} votos\n"
        return result
            
    def __add__(self, outro):
        if isinstance(outro, Urna):
            new_id = self._id_urna + '_' + outro._id_urna
            new_lista_vots = self._votos + outro._votos
            nova_urna = Urna()
            nova_urna._id_urna = new_id
            nova_urna._votos = new_lista_vots
            return nova_urna