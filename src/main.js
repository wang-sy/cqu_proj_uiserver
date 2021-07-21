import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import './plugins/ant-design-vue.js'

Vue.config.productionTip = false
axios.defaults.withCredentials = true

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
