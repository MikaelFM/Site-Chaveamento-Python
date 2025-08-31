import pickle
import os
from app.models.Time import Time


class EquipeRepository:
    CAMINHO_ARQUIVO = 'times.pkl'

    @staticmethod
    def salvar(lista_times):
        with open(EquipeRepository.CAMINHO_ARQUIVO, 'wb') as f:
            pickle.dump(lista_times, f)

    @staticmethod
    def carregar():
        if not os.path.exists(EquipeRepository.CAMINHO_ARQUIVO):
            return []
        with open(EquipeRepository.CAMINHO_ARQUIVO, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def carregar_json():
        listTimesJson = []
        listTimesObjects = EquipeRepository.carregar()
        for time in listTimesObjects:
            listTimesJson.append(time.getJson())
        return listTimesJson

    @staticmethod
    def carregar_por_index(index):
        times = EquipeRepository.carregar()
        if 0 <= index < len(times):
            return times[index]
        return f'Índice inválido. Nenhum time foi removido.'

    @staticmethod
    def carregar_json_por_index(index):
        times = EquipeRepository.carregar_json()
        if 0 <= index < len(times):
            return times[index]
        return f'Índice inválido. Nenhum time foi removido.'

    @staticmethod
    def remover_por_index(index):
        times = EquipeRepository.carregar()
        if 0 <= index < len(times):
            removido = times.pop(index)
            EquipeRepository.salvar(times)
            return f'Time "{removido}" removido com sucesso.'
        return f'Índice inválido. Nenhum time foi removido.'

    @staticmethod
    def editar_por_index(index, dados):
        equipe = EquipeRepository.carregar()
        if 0 <= index < len(equipe):
            equipe[index] = dados
            EquipeRepository.salvar(equipe)
            return f'Equipe"{equipe[index]}" atualizada com sucesso para {dados}'
        return f'Índice inválido. Nenhuma equipe foi atualizada'

    @staticmethod
    def adicionar(dados):
        equipes = EquipeRepository.carregar()
        equipes.append(dados)
        EquipeRepository.salvar(equipes)
