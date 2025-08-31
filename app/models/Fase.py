import random

from app.models.Confronto import Confronto
from app.models.Jogo import Jogo

class Fase:
    def __init__(self, ida_volta, times):
        self.__ida_volta = ida_volta
        self.__times = times
        self.__confrontos = []
        self.__times_classificados = []

    def sortearConfrontos(self):
        random.shuffle(self.__times)
        for i in range(0, len(self.__times) - 1, 2):
            confronto = Confronto(
                self.__times[i],
                self.__times[i + 1],
            )
            self.__confrontos.append(confronto)

    def simularConfrontos(self):
        numeroJogos = 1 if not self.__ida_volta else 2
        for confronto in self.__confrontos:
            for i in range(numeroJogos):
                golsA = random.randint(0, 5)
                golsB = random.randint(0, 5)
                jogo = Jogo(confronto.time1, confronto.time2, golsA, golsB)
                confronto.addJogo(jogo)
                confronto.total_time_a += golsA
                confronto.total_time_b += golsB
        self.defineTimesClassificados()

    def defineTimesClassificados(self):
        self.__times_classificados.clear()
        for confronto in self.__confrontos:
            classificado = confronto.getVencedorConfronto()
            self.__times_classificados.append(classificado)

    def getClassificadosProximaFase(self):
        return self.__times_classificados

    def getJson(self):
        confrontos = []
        times = []
        times_classificados = []

        for confronto in self.__confrontos:
            confrontos.append(confronto.getJson())

        for time in self.__times:
            times.append(time.getJson())

        for time in times_classificados:
            times_classificados.append(time.getJson())

        return {
            'ida_volta': self.__ida_volta,
            'times': times,
            'confrontos': confrontos,
            'times_classificados': times_classificados
        }