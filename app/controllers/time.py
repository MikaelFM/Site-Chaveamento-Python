from app.models.Time import Time
from app.repositories.EquipeRepository import EquipeRepository

equipeRepository = EquipeRepository()
times = equipeRepository.carregar_json()
if len(times) == 0:
    times([
        Time('SC Internacional', 'https://vetores.org/d/internacional.svg'),
        Time('FC Barcelona','https://upload.wikimedia.org/wikipedia/pt/thumb/4/43/FCBarcelona.svg/2020px-FCBarcelona.svg.png'),
        Time('Grêmio FBPA','https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Gremio_logo.svg/1718px-Gremio_logo.svg.png'),
        Time('EC Juventude','https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/EC_Juventude.svg/1200px-EC_Juventude.svg.png')
    ])

def getTimeByIndex(index):
    time = {}
    if index:
        index = int(index)
        time = equipeRepository.carregar_por_index(index)
        time['index'] = index
    return render_template('time/form.html', time=time)

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
        equipeRepository.adicionar(time)
        return "", 200

    equipeRepository.salvar(time)
    return "", 200

def excluirTime(index):
    equipeRepository.remover_por_index(index)

