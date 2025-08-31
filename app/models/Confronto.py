import random


class Confronto:
    def __init__(self, time1, time2):
        self.__jogos = []
        self.time1 = time1
        self.time2 = time2
        self.total_time_a = 0
        self.total_time_b = 0
        self.vencedor = None

    def addJogo(self, jogo):
        self.__jogos.append(jogo)

    def getVencedorConfronto(self):
        if self.total_time_a > self.total_time_b:
            self.vencedor = self.time1
            return self.vencedor
        elif self.total_time_a < self.total_time_b:
            self.vencedor = self.time2
            return self.vencedor
        else:
            self.vencedor - random.choice([self.time1, self.time2])
            return self.vencedor

    def getJson(self):
        jogos = []

        for jogo in self.__jogos:
            jogos.append(jogo.getJson())

        vencedor = None
        if self.vencedor is not None:
            vencedor = self.vencedor.getJson()

        return {
            'time1': self.time1.getJson(),
            'time2': self.time2.getJson(),
            'total_time_a': self.total_time_a,
            'total_time_b': self.total_time_b,
            'vencedor': vencedor,
            'jogos': jogos
        }
