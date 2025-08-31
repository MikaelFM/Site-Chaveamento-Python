const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        txt_busca: '',
        times: times
    },
    computed: {
        timesFiltrados() {
            return this.times.filter(e => e.nome.toLowerCase().includes(this.txt_busca.toLowerCase()));
        }
    },
})