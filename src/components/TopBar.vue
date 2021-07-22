<template>
    <main>
      <a-icon class="trigger" type="home"  :theme="choose === 'home' ? 'twoTone' : 'outlined'" @click="to_home('/')" style="margin-left: 4%; font-size: 32px"/>
      <a-icon class="trigger" type="smile" :theme="choose === 'home' ? 'outlined' : 'twoTone'" @click="to_user('/user')" style="font-size: 32px"/>
      <a-input-search placeholder="input search text" enter-button style="width: 40%; margin-top: 1.2%; margin-left: 15%"
                      @search="to_search('/goodslist', search_content)" v-model="search_content"/>
      <div style="display: inline; font-size: 1.2em; float: right; margin-right: 8%">{{username}}</div>
      <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" style="width: 4%; height: 4%; margin-bottom: 2%; float: right"/>
    </main>
</template>

<script>

export default {
    model: {
        prop: 'collapsed',
        event: 'changeMenu',
    },
    data () {
      return {
        choose: 'home',
        username: '未设置用户名',
        search_content: null
      }
    },
    props: {
        // close or not.
        collapsed: Boolean
    },
    methods: {
      to_home(path) {
        this.choose = 'home'
        this.$router.push(path)
      },
      to_user(path) {
        this.choose = 'user'
        this.$router.push(path)
      },
      to_search(path, search_content) {
        this.$router.push({ path: path, query: {searchid: search_content}})
      }
    },
    mounted() {
      let _this = this
      this.$axios.get(this.$base_url + '/user/getInfo')
        .then(function (response) {
          _this.username = response.data.data.username
        }).catch(function (error) {
      })
      this.$event_bus.$on('update_username', (new_name) => {
        _this.username = new_name
      })
      this.$event_bus.$on('login_success', (name) => {
        _this.username = name
      })
    }
}

</script>

<style scoped>
.trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

.trigger:hover {
  color: #1890ff;
}

</style>
