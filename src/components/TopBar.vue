<template>
    <div>
      <div>
       <a-menu mode="horizontal" :default-selected-keys="['1']" style="margin-left: 5%">
          <a-menu-item key="1" @click="to_user('/')"> <a-icon type="home"/>主页</a-menu-item>
          <a-menu-item key="2" @click="to_user('/user')"> <a-icon type="user"/>我的</a-menu-item>
          <a-input-search placeholder="输入搜索内容" style="width: 30%; margin-left: 18%"
                          @search="to_search('/goodslist', search_content)" v-model="search_content"/>
          <a-avatar :src="avatar" style="width: 3.5%; height: 3.5%; margin-left: 18%; margin-bottom: 0.1%"/>
          <a-popover style="margin-left: 1%">
            <template slot="content">
              <p>你好：{{username}}</p>
            </template>
            <a-button style="border: white">{{username}}</a-button>
          </a-popover>
        </a-menu>
      </div>
    </div>
</template>

<script>
import { EventBus } from '../event-bus'

export default {
    model: {
        prop: 'collapsed',
        event: 'changeMenu',
    },
    data () {
      return {
        choose: 'home',
        username: '未设置用户名',
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
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
        EventBus.$emit('submitSearch',this.to_search)
      }
    },
    mounted() {
      let _this = this
      this.$axios.get(this.$base_url + 'api/user/getInfo')
        .then(function (response) {
          _this.username = response.data.data.username
          _this.avatar = _this.$base_url + response.data.data.avatar_url
        }).catch(function (error) {
      })
      this.$event_bus.$on('update_username', (new_name) => {
        _this.username = new_name
      })
      this.$event_bus.$on('login_success', (name, avatar_url) => {
        _this.username = name
        _this.avatar = avatar_url
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
