import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/user',
    name: 'User',
    component: () => import("../views/User")
  },
  {
    //商品搜索展示
    path: '/goodslist',
    name: 'GoodsList',
    component: () => import("../views/GoodsList")
  }
]

const router = new VueRouter({
  routes
})

export default router
