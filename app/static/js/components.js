Vue.component('vue-sidebar', {
  template: `
    <sidebar>
      <section class="sidebar-header"> 
        <span>Competition</span>
      </section>
      <section class="menu">
        <ul>
<!--          <li :class="{'selected': currentRoute === '/'}">-->
<!--            <i class="fi fi-rr-home"></i><span>Início</span>-->
<!--          </li>-->
          <a href="/time/list">
            <li :class="{'selected': currentRoute === '/time/list'}">
                <i class="fa-solid fa-shield-halved"></i><span>Times</span>
            </li>
          </a>
          <a href="/competicao/list">  
              <li :class="{'selected': currentRoute === '/competicao/list'}">
                <i class="material-symbols-outlined">trophy</i><span>Competições</span>
              </li>
          </a>
        </ul>
      </section>
    </sidebar>
  `,
  data() {
    return {
      currentRoute: window.location.pathname
    };
  }
});


Vue.component('vue-image-picker', {
  props: {
      'img': {
          type: String,
          required: true,
          default: ''
      },
  },
  template: `
    <div>
      <img id="photo" class="photo" style="margin-top: 0" @click="pickImage" :src="src">
      <input id="pick-image" type="file" accept="image/*" style="display: none" @change="onChangeImage()">
    </div>
  `,
  data(){
    return {
        'src': this.img
    }
  },
  methods: {
    pickImage(){
        const input = document.getElementById('pick-image');
        input.click();
    },
    onChangeImage(){
        const input = document.getElementById('pick-image');
        const arquivo = input.files[0];
        const reader = new FileReader();
        reader.onload = () => {
            let base64 = reader.result
            this.src = base64;
            this.$emit('update:img', base64);
        };

        reader.readAsDataURL(arquivo);
    },
  }
});

Vue.component('vue-navbar', {
  props: {
      'img': {
          type: String,
          required: true,
          default: ''
      },
  },
  data() {
    return {
      currentRoute: window.location.pathname
    };
  },
  template: `
    <nav>
        <div class="options">
            <ul>
                <li 
                    :class="{'selected': currentRoute === '/competicao/list'}" 
                    @click="goToRoute('/competicao/list')"
                >
                    Competições
                </li>
                <li 
                    :class="{'selected': currentRoute === '/time/list'}" 
                    @click="goToRoute('/time/list')"
                >
                    Equipes
                </li>
            </ul>
        </div>
    </nav>
  `,
    methods: {
        goToRoute(route){
            window.location.href = route;
        }
    }
});