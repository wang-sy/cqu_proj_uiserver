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
Vue.prototype.$base_url = '/'

Vue.prototype.$submitOrder = function (goodsList) {
  EventBus.$emit('submitOrder', goodsList)
}

Vue.prototype.$setShoppingCart = function (shoppingCart) {
  const rawShoppingCartInfo = JSON.stringify(shoppingCart)

  localStorage.setItem("teapotShopppingCart", rawShoppingCartInfo)
}

Vue.prototype.$getShoppingCart = function () {
  const rawShoppingCartInfo = localStorage.getItem("teapotShopppingCart")
  if (rawShoppingCartInfo === undefined || rawShoppingCartInfo === null) {
    return []
  }

  return JSON.parse(rawShoppingCartInfo)
}

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
