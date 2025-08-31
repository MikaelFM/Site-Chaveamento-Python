const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        time: {
            'index': null,
            'nome': '',
            'img': '',
            ...time
        },
    },
    computed: {
        canSubmit() {
            return this.time.nome.trim().length > 0;
        }
    },
    methods: {
        save(){
            axios.post('/time/save', {
                ...this.time
            })
            .then(function (response) {
                window.location.href = '/time/list'
            })
            .catch(function (error) {
                console.error(error);
            });
        },
        cancel(){
            window.location.href = '/time/list';
        }
    }
})