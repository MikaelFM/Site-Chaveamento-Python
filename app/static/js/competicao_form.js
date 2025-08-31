const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        competicao: {
            'index': null,
            'img': '',
            'nome': '',
            'quantidade_times': '',
            'formato_jogos': '',
            'formato_final': 'jogo_unico',
            'times': [],
            ...competicao
        },
        listTimes: times,
        txt_busca_times: '',
        multiSelectActive: false
    },
    computed: {
        canSubmit() {
            return (
                this.competicao.nome.trim().length > 0 &&
                this.competicao.quantidade_times.length > 0 &&
                this.competicao.formato_jogos.length > 0 &&
                this.competicao.formato_final.length > 0 &&
                this.competicao.times.length == this.competicao.quantidade_times
            );
        },
        timesFiltrados(){
            return this.listTimes.filter(t =>
                t.nome.toLowerCase().includes(this.txt_busca_times.toLowerCase()) &&
                this.competicao.times.indexOf(t) === -1
            );
        }
    },
    methods: {
        save(){
            const competicao = this.competicao;
            axios.post('/competicao/save', {
                ...this.competicao,
                'times': this.competicao.times,
                'ida_volta': this.competicao.formato_jogos === 'ida_volta',
                'final_ida_volta': this.competicao.formato_final === 'ida_volta',
            })
            .then(function (response) {
                window.location.href = '/competicao/list'
            })
            .catch(function (error) {
                console.error(error);
            });
        },
        select(event, time){
            event.preventDefault();
            event.stopPropagation();
            this.competicao.times.push(time);
            this.$nextTick(() => {
                this.$refs.inputTimes?.focus();
            });
        },
        remove(time){
            let index = this.competicao.times.indexOf(time);
            this.competicao.times.splice(index, 1);
        },
        onInputKeyDown(event){
            if (event.key === 'Backspace'){
                this.competicao.times.pop();
                return;
            }
            if (event.key === 'Enter'){
                event.preventDefault();
                const teams = this.timesFiltrados;
                if(teams.length){
                    this.competicao.times.push(teams[0]);
                }
                this.txt_busca_times = '';
            }
        },
        cancel(){
            window.location.href = '/competicao/list';
        }
    },
    mounted(){
        const div = document.getElementById("multiselect");
        document.addEventListener("click", (event) => {
            this.multiSelectActive = div.contains(event.target) || div === event.target;
        });
    },
    watch: {
        'competicao.formato_jogos': function (val){
            if(val === 'jogo_unico'){
                this.competicao.formato_final = 'jogo_unico';
            }
        }
    }
})