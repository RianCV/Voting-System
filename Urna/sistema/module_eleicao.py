from Urna.sistema.module_partido import Partido
from Urna.sistema.module_urna import Urna
from Urna.sistema.module_cargos import *

class Eleicao():
    def __init__(self, caminho_arq: str):
        self._candidatos = []
        self._partidos = []
        self._urnas = []
        self.caminho_arq = caminho_arq
        self._carrega_eleicao()
        
    
    @property
    def caminho_arq(self):
        return self.__caminho_arq
    
    @caminho_arq.setter
    def caminho_arq(self, value):
            self.__caminho_arq = value
    
    def _carrega_eleicao(self):
        erros = ""
        with open(self.__caminho_arq, "r") as file:
            for line in file:
                if("adicionar_partido" in line):
                    splitted_line = line.split(",")
                    cnpj = splitted_line[0][19:].replace(".", "").replace("/", "").replace("-", "")
                    nome = splitted_line[1][1:]
                    numero = splitted_line[2][1:].rstrip('\n')
                    try:
                        self._partidos.append(Partido(nome, cnpj, numero))
                    except ValueError as e:
                        erros += f'{str(e)} \n'
                    continue
                        
                    
                if("adicionar_pessoa" in line):
                    splitted_line = line.split(",")
                    nome = splitted_line[0][18:]
                    cpf = splitted_line[1][1:]
                    if(len(cpf) != 11):
                        erros += f'{nome} tem tamanho de cpf diferente de 11! \n'
                        continue
                    data_nasc = splitted_line[2][1:].rstrip('\n')
                    with open(self.__caminho_arq, "r") as file2:
                        for line in file2:
                            if("adicionar_candidato" in line):
                                splitted_line2 = line.split(",")
                                if(splitted_line2[0][21:] == cpf):
                                    numero = splitted_line2[1][1:]
                                    partido = splitted_line2[2][1:]
                                    propostas = splitted_line2[3][1:]
                                    cargo = splitted_line2[4][1:].rstrip('\n')
                                    
                                    if(cargo == "DepFederal"):
                                        try:
                                            self._candidatos.append(DepFederal(nome, cpf, data_nasc, numero, partido, propostas))
                                        except Exception as e:
                                            erros += f'{str(e)} \n'
                                    elif(cargo == "DepEstadual"):
                                        try:
                                            self._candidatos.append(DepEstadual(nome, cpf, data_nasc, numero, partido, propostas))
                                        except Exception as e:
                                            erros += f'{str(e)} \n'
                                    elif(cargo == "Governador"):
                                        try:
                                            self._candidatos.append(Governador(nome, cpf, data_nasc, numero, partido, propostas))
                                        except Exception as e:
                                            erros += f'{str(e)} \n'
                                    elif(cargo == "Presidente"):
                                        try:
                                            self._candidatos.append(Presidente(nome, cpf, data_nasc, numero, partido, propostas))
                                        except Exception as e:
                                            erros += f'{str(e)} \n'
                                    elif(cargo == "Senador"):
                                        try:
                                            self._candidatos.append(Senador(nome, cpf, data_nasc, numero, partido, propostas))
                                        except Exception as e:
                                            erros += f'{str(e)} \n'
                                    else:
                                        erros += f"Cargo ({cargo}) nao existe! \n"
        with open("saida/erros_log.txt", "w") as file:
            file.write(erros)
                    
    
    def cria_urna(self, arq_caminho: str):
        urna = Urna()
        urna.carrega_urna(arq_caminho)
        self._urnas.append(urna)
        
    def gera_boletim(self):
        with open("saida/boletimUrna.txt", "w") as file:
            for urna in self._urnas:
                file.write(urna.imprime_boletim(self._candidatos) + '\n')
                
    def gera_contabilizacao(self):
        saida = f'RESULTADO ELEIÇÃO------------QUANTIDADE ELEITORES: {self._urnas[0]._votos[0].get_total_votos()}\n'
        resultado_final_votacao = {}
        for urna in self._urnas:
            if(len(resultado_final_votacao) == 0):
                resultado_final_votacao = urna._dict_votos
            else:
                for chave, valor in urna._dict_votos.items():
                    for chave_interna, valor_interno in valor.items():
                        resultado_final_votacao[chave][chave_interna] += valor_interno
        for cargo, dicionario_interno in resultado_final_votacao.items():
            saida += f'Cargo: {cargo}, Candidato(s) mais votado(s): '
            maior = 0
            for candidato in dicionario_interno:
                if(dicionario_interno[candidato] > maior):
                    maior = dicionario_interno[candidato]
            empate = False
            for candidato in dicionario_interno:
                if(dicionario_interno[candidato] == maior and (empate == False)):
                    saida += f'{candidato} N: {self.get_numero(candidato)}, votos: {dicionario_interno[candidato]}'
                    empate = True
                    continue
                if(dicionario_interno[candidato] == maior and (empate == True)):
                    saida += f', {candidato} {self.get_numero(candidato)}, votos: {dicionario_interno[candidato]}'
            saida += '\n'
        with open("saida/contabilizacao.txt", 'w') as file:
            file.write(saida)
    
    
    def get_numero(self, nome):
        for candidato in self._candidatos:
            if(candidato.nome == nome):
                return candidato.numero
