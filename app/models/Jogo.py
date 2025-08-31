class Jogo:
    def __init__(self, time_a, time_b, gols_time_a, gols_time_b):
        self.__time_a = time_a
        self.__time_b = time_b
        self.__gols_time_a = gols_time_a
        self.__gols_time_b = gols_time_b

    def getJson(self):
        return {
            'gols_time_a': self.__gols_time_a,
            'gols_time_b': self.__gols_time_b,
        }