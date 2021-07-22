import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import { EventBus } from './event-bus'
import './plugins/ant-design-vue.js'

Vue.config.productionTip = false
axios.defaults.withCredentials = true

Vue.prototype.$submitOrder = function (goodsList) {
  EventBus.$emit('submitOrder', goodsList)
}

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
