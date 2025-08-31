from app.models.Time import Time
from app.repositories.CompeticaoRepository import CompeticaoRepository

def salvarTime(data):
    index = data['index']
    time = data['time']
    nome_time = time['nome']
    img_time = time['img']

    if nome_time == '':
        return "", 400

    if img_time == '':
        return "", 400

    time = Time(nome_time, img_time)

    if index is None:
        CompeticaoRepository.adicionar(time)
        return "", 200

    CompeticaoRepository.salvar(time)
    return "", 200

def excluirTime(index):
    CompeticaoRepository.remover_por_index(index)




