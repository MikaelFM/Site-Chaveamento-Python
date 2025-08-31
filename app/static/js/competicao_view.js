const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        competicao: competicao
    },
    computed: {
        isCompeticaoSorteada(){
            return this.competicao.fases.length > 0;
        },
        isCompeticaoSimulada(){
            return this.competicao.has_campeao;
        },
        descCompeticao(){
            let qtdTimes = this.competicao.quantidade_times;
            let formatoJogo = this.competicao.formato_jogos === 'ida_volta' ? 'Jogos Ida e Volta' : 'Jogos Únicos';
            let formatoFinal = this.competicao.formato_final === 'ida_volta' ? 'Final Ida e Volta' : 'Final Única';
            return `${qtdTimes} Participantes - ${formatoJogo} - ${formatoFinal}`;
        },
        qtdTimesByFase(){
            return [16, 8, 4, 2];
        },
        nomeFases(){
            return ['Oitavas', 'Quartas', 'Semifinal', 'Final']
        },
        getNumFaseInicial(){
            let index = this.qtdTimesByFase.indexOf(parseInt(competicao.quantidade_times));
            return index + 1;
        },
        fases(){
            let fases = [...this.competicao.fases];
            if(!this.isCompeticaoSimulada){
                for(let i = this.getNumFaseInicial + 1; i <= 4; i++){
                    let confrontos = [];
                    for(let q = 0; q < (this.qtdTimesByFase[i - 1])/2; q++){
                        let faseAnterior = this.nomeFases[i - 2];
                        let numInicial = q * 2 + 1;
                        confrontos.push({
                            'time1': {
                                'nome': `Vencedor ${faseAnterior} ${numInicial}`,
                                'img': ''
                            },
                            'time2': {
                                'nome': `Vencedor ${faseAnterior} ${numInicial + 1}`,
                                'img': ''
                            }
                        });
                    }
                    fases.push({ confrontos })
                }
            }
            return fases;
        }
    },
    methods: {
        sortear(){
            let vue_self = this;
            let index = this.competicao.index;
            axios.get(`/competicao/sortear/${index}`)
            .then(function (response) {
                vue_self.competicao = {...vue_self.competicao, ...response.data.competicao};
            })
            .catch(function (error) {
                console.error(error);
            });
        },
        simular(){
            let vue_self = this;
            let index = this.competicao.index;
            axios.get(`/competicao/simular/${index}`)
            .then(function (response) {
                vue_self.competicao = {...vue_self.competicao, ...response.data.competicao};
            })
            .catch(function (error) {
                console.error(error);
            });
        },
    }
})