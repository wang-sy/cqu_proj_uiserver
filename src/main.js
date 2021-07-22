import Vue from 'vue'
import {EventBus} from './event-bus'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import './plugins/ant-design-vue.js'

Vue.config.productionTip = false
axios.defaults.withCredentials = true
Vue.prototype.$event_bus = EventBus
Vue.prototype.$axios = axios
Vue.prototype.$base_url = 'http://114.116.213.123:8081/'

Vue.prototype.$submitOrder = function (goodsList) {
  EventBus.$emit('submitOrder', goodsList)
}

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
