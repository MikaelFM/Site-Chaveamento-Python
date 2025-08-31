const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        txt_busca: '',
        competicoes: competicoes,
    },
    computed: {
        competicoesFiltradas() {
            return this.competicoes.filter(c => c.nome.toLowerCase().includes(this.txt_busca.toLowerCase()));
        }
    },
    methods: {
        getDescCompeticao(competicao){
            let qtdTimes = competicao.quantidade_times;
            let formatoJogo = competicao.formato_jogos === 'ida_volta' ? 'Jogos Ida e Volta' : 'Jogos Únicos';
            let formatoFinal = competicao.formato_final === 'ida_volta' ? 'Final Ida e Volta' : 'Final Única';
            return `${qtdTimes} Participantes - ${formatoJogo} - ${formatoFinal}`;
        }
    }
})