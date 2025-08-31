class Time:
    def __init__(self, nome, img):
        self.__nome = nome
        self.__img = img

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome

    def getJson(self):
        return {
            'nome': self.__nome,
            'img': self.__img
        }