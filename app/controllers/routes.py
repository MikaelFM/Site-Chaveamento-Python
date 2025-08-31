from app import app
from flask import render_template, request, redirect, url_for
from app.models.Competicao import Competicao
from app.models.Time import Time
from app.repositories.EquipeRepository import EquipeRepository
from app.repositories.CompeticaoRepository import CompeticaoRepository

equipeRepository = EquipeRepository()
competicaoRepository = CompeticaoRepository

### https://youtu.be/cfedNUhQq6Y


@app.route("/")
def competicoes():
    return redirect(url_for('list_competicao'))


###################### Rotas Time ##########################

@app.route("/time/list")
def list_times():
    times = equipeRepository.carregar_json()
    return render_template('time/list.html', times=times)


@app.route("/time/edit/", defaults={'index': None})
@app.route("/time/edit/<index>")
def form_time(index):
    time = {}
    if index:
        index = int(index)
        time = equipeRepository.carregar_json_por_index(index)
        time['index'] = index
    return render_template('time/form.html', time=time)

#Rota para salvar time
@app.route("/time/save", methods=['POST'])
def save_time():
    data = request.json
    index = data['index']
    time = Time(data['nome'], data['img'])
    if index is None:
        equipeRepository.adicionar(time)
    else:
        equipeRepository.editar_por_index(index, time)
    return "", 200

#Rota delete time
@app.route("/time/delete/<index>")
def delete_time(index):
    index = int(index)
    times = EquipeRepository()
    times.remover_por_index(index)
    return redirect(url_for('list_times'))


###################### Rotas Competição ##########################


@app.route("/competicao/list")
def list_competicao():
    competicoes = competicaoRepository.carregar_json()
    return render_template('competicao/list.html', competicoes=competicoes)


#Editar competição
@app.route("/competicao/edit/", defaults={'index': None})
@app.route("/competicao/edit/<index>")
def edit_competicao(index):
    competicao = {}
    times = equipeRepository.carregar_json()
    if index is not None:
        index = int(index)
        competicao = competicaoRepository.carregar_json_por_index(index)
        competicao['index'] = index
    return render_template('competicao/form.html', competicao=competicao, times=times)


@app.route("/competicao/save", methods=['POST'])
def save_competicao():
    data = request.json
    index = data['index']
    times = []
    for time in data['times']:
        times.append(Time(time['nome'], time['img']))
    competicao = Competicao(data['nome'], data['img'], data['quantidade_times'], times, data['ida_volta'], data['final_ida_volta'])
    if index is None:
        competicaoRepository.adicionar(competicao)
    else:
        competicaoRepository.editar_por_index(index, competicao)
    return "", 200


#Deletar competição
@app.route("/competicao/delete/<index>")
def delete_competicao(index):
    index = int(index)
    competicaoRepository.remover_por_index(index)
    return redirect(url_for('list_competicao'))


@app.route("/competicao/view/<index>")
def view_competicao(index):
    index = int(index)
    competicao = CompeticaoRepository.carregar_json_por_index(index)
    competicao['index'] = index
    return render_template('competicao/view.html', competicao=competicao)


#rota para apenas sortear
@app.route("/competicao/sortear/<index>", methods=['GET'])
def sortear_competicao(index):
    index = int(index)
    competicao = CompeticaoRepository.carregar_por_index(index)
    competicao.sortear()
    CompeticaoRepository.editar_por_index(index, competicao)
    return {'competicao': competicao.getJson()}, 200


#rota para simular o campeonato completo
@app.route("/competicao/simular/<index>")
def simular_competicao(index):
    index = int(index)
    competicao = CompeticaoRepository.carregar_por_index(index)
    competicao.simular()
    CompeticaoRepository.editar_por_index(index, competicao)
    return {'competicao': competicao.getJson()}, 200

