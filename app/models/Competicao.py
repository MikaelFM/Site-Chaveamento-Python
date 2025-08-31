from app.models.Fase import Fase

class Competicao:
    def __init__(self, nome, img=None, quantidade_times=0, lista_times=[], ida_volta=False, final_ida_volta=False):
        self.__nome = nome
        self.__img = img
        self.__lista_times = lista_times
        self.__ida_volta = ida_volta
        self.__final_ida_volta = final_ida_volta
        self.__fases = []
        self.__campeao = None
        self.__quantidade_times = quantidade_times

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def sortear(self):
        fase = Fase(self.__ida_volta, self.__lista_times)
        fase.sortearConfrontos()
        self.__fases.append(fase)
        return fase

    def simular(self):
        for fase in self.__fases:
            indexLastFase = len(self.__fases) - 1
            self.__fases[indexLastFase].simularConfrontos()
            timesClassificados = self.__fases[indexLastFase].getClassificadosProximaFase()
            if len(timesClassificados) == 1:
                self.__campeao = timesClassificados[0]
                break
            isFinal = len(timesClassificados) == 2
            idaVolta = self.__final_ida_volta if isFinal else self.__ida_volta
            newFase = Fase(idaVolta, timesClassificados)
            newFase.sortearConfrontos()
            self.__fases.append(newFase)

    def getJson(self):
        times = []
        fases = []

        for time in self.__lista_times:
            times.append(time.getJson())

        for fase in self.__fases:
            fases.append(fase.getJson())

        return {
            'nome': self.__nome,
            'img': self.__img,
            'quantidade_times': self.__quantidade_times,
            'formato_jogos': 'ida_volta' if self.__ida_volta else 'jogo_unico',
            'formato_final': 'ida_volta' if self.__final_ida_volta else 'jogo_unico',
            'times': times,
            'fases': fases,
            'has_campeao': self.__campeao is not None
        }
