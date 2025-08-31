import pickle
import os

class CompeticaoRepository:
    CAMINHO_ARQUIVO = 'competicoes.pkl'

    @staticmethod
    def salvar (lista_competicoes):
        with open(CompeticaoRepository.CAMINHO_ARQUIVO, 'wb') as f:
            pickle.dump(lista_competicoes, f)
    
    @staticmethod
    def carregar():
        if not os.path.exists(CompeticaoRepository.CAMINHO_ARQUIVO):
            return []
        with open(CompeticaoRepository.CAMINHO_ARQUIVO, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def carregar_json():
        listCompeticoesJson = []
        listCompeticoesObjects = CompeticaoRepository.carregar()
        for competicao in listCompeticoesObjects:
            listCompeticoesJson.append(competicao.getJson())
        return listCompeticoesJson

    @staticmethod
    def carregar_por_index(index):
        competicoes = CompeticaoRepository.carregar()
        if 0 <= index < len(competicoes):
            return competicoes[index]
        return f'Índice inválido. Nenhuma competicão foi removida.'

    @staticmethod
    def carregar_json_por_index(index):
        competicoes = CompeticaoRepository.carregar_json()
        if 0 <= index < len(competicoes):
            return competicoes[index]
        return f'Índice inválido. Nenhuma competicão foi removida.'

    @staticmethod
    def remover_por_index(index):
        competicao = CompeticaoRepository.carregar()
        if 0 <= index < len(competicao):
            removido = competicao.pop(index)
            CompeticaoRepository.salvar(competicao)
            return f'Competição "{removido}" removido com sucesso.'
        return f'Índice inválido. Nenhum competição foi removida.'

        
    @staticmethod
    def editar_por_index(index,dados):
        competicao = CompeticaoRepository.carregar()
        if 0 <= index < len(competicao):
            competicao[index] = dados
            CompeticaoRepository.salvar(competicao)
            return f'Competição "{competicao[index]}" atualizada com sucesso para {dados}'
        return f'Índice inválido. Nenhuma competição foi atualizada'

    @staticmethod
    def adicionar(dados):
        competicao = CompeticaoRepository.carregar()
        competicao.append(dados)
        CompeticaoRepository.salvar(competicao)