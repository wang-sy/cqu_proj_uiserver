<template>
  <a-layout id="components-layout-demo-custom-trigger" class="page_container">
    <Register></Register>
    <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
      <sider-menu></sider-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0">
        <top-bar v-model="collapsed"></top-bar>
      </a-layout-header>
      <a-layout-content
        :style="{ margin: '10px 10px', padding: '10px', minHeight: '280px' }"
      >
        <Login></Login>
        <SubmitOrder></SubmitOrder>
        <router-view></router-view>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>
import SiderMenu from './components/SiderMenu'
import TopBar from './components/TopBar'
import Login from './components/Login'
import Register from './components/Register'
import SubmitOrder from './components/SubmitOrder.vue'

export default {
  components: {
    SiderMenu,
    TopBar,
    Login,
    Register,
    SubmitOrder
  },
  data() {
    return {
      collapsed: false,
    };
  },
};
</script>

<style>
.page_container {
  height: 100%;
}

</style>
