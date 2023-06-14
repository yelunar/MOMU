import Vue from 'vue'
import { BootstrapVue } from 'bootstrap-vue'
import App from './App.vue'
import store from './store'
import router from './router'
// import VueYoutube from 'vue-youtube'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { SidebarPlugin } from 'bootstrap-vue'
import { CardPlugin } from 'bootstrap-vue'
// import { ImagePlugin } from 'bootstrap-vue'
import { FormFilePlugin } from 'bootstrap-vue'

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)
Vue.use(SidebarPlugin)
Vue.use(CardPlugin)
// Vue.use(VueYoutube)
// Vue.use(ImagePlugin)
Vue.use(FormFilePlugin)