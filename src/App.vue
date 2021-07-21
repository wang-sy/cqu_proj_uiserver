<template>
  <a-layout id="components-layout-demo-custom-trigger" class="page_container">
    <Login></Login>
    <Register></Register>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0; height: 12%">
        <top-bar v-model="collapsed" style="margin-top: 1%"></top-bar>
      </a-layout-header>
      <a-layout-content
        :style="{ margin: '10px 10px', padding: '10px', minHeight: '280px' }"
      >
        <router-view></router-view>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>
import TopBar from './components/TopBar'
import Login from './components/Login'
import Register from './components/Register'

export default {
  components: {
    TopBar,
    Login,
    Register
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
