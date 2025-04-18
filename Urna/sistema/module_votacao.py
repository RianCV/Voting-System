class Votacao():
    
    __total_votos = 0
    
    @classmethod
    def incrementa_voto(cls):
        cls.__total_votos += 1
    
    def get_total_votos(cls):
        return cls.__total_votos
    
    
    def __init__(self, id_votacao: str, depEstadual: str,
                                        depFederal: str, senador: str, governador: str, presidente: str):
        self.incrementa_voto()
        self.id_votacao = id_votacao
        self.depEstadual = depEstadual
        self.depFederal = depFederal
        self.senador = senador
        self.governador = governador
        self.presidente = presidente
    

    @property
    def id_votacao(self):
        return self._id_votacao

    @id_votacao.setter
    def id_votacao(self, value):
        self._id_votacao = value

    @property
    def depEstadual(self):
        return self._depEstadual

    @depEstadual.setter
    def depEstadual(self, value):
        self._depEstadual = value

    @property
    def depFederal(self):
        return self._depFederal

    @depFederal.setter
    def depFederal(self, value):
        self._depFederal = value

    @property
    def senador(self):
        return self._senador

    @senador.setter
    def senador(self, value):
        self._senador = value

    @property
    def governador(self):
        return self._governador

    @governador.setter
    def governador(self, value):
        self._governador = value

    @property
    def presidente(self):
        return self._presidente

    @presidente.setter
    def presidente(self, value):
        self._presidente = value

    def __str__(self):
        return (f"Votacao:\n"
                f"ID Votacao: {self.id_votacao}\n"
                f"Deputado Estadual: {self.depEstadual}\n"
                f"Deputado Federal: {self.depFederal}\n"
                f"Senador: {self.senador}\n"
                f"Governador: {self.governador}\n"
                f"Presidente: {self.presidente}")