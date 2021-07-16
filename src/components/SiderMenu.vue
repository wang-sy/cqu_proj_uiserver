<template>
    <main>
        <div class="logo" />
        <a-menu theme="dark" mode="inline" :default-selected-keys="['1']">
            <a-menu-item key="1" @click="to_path('/')">
                <a-icon type="home" />
                <span>主页</span>
            </a-menu-item>
            <a-menu-item key="2"  @click="to_path('/user')">
                <a-icon type="user" />
                <span>我的</span>
            </a-menu-item>
        </a-menu>
    </main>
</template>

<script>

export default {
    methods: {
        to_path(path) {
            this.$router.push(path)
        }
    }
}

</script>

<style scoped>
.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}

</style>
