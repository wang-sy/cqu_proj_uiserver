<template>
  <div>
    <Address></Address>
    <ModifyPersonInfo></ModifyPersonInfo>
    <Password></Password>
    <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" style="width: 5%; height: 5%"/>
    <div style="display: inline; font-size: 1.2em; margin-left: 2%">{{username}}</div>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_person_info">更多信息</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_address">收货地址</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_password">修改密码</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="logout">注销登录</a>
  </div>
</template>

<script>
import {EventBus} from '../event-bus'
import Address from './Address'
import ModifyPersonInfo from './ModifyPersonInfo'
import Password from './Password'
import axios from "axios";

export default {
  name: 'PersonInfo',
  components: {
    Password,
    ModifyPersonInfo,
    Address
  },
  data () {
    return {
      username: '未设置用户名'
    }
  },
  methods: {
    modify_person_info: function () {
      EventBus.$emit('modify_person_info')
    },
    modify_address: function () {
      EventBus.$emit('modify_address')
    },
    modify_password: function () {
      EventBus.$emit('modify_password')
    },
    logout: function () {
      let _this = this
      axios.get('http://localhost:8090/user/logout')
      .then(function (response) {
        if (response.data === 'logout') {
          _this.username = '未设置用户名'
          alert('注销成功')
        }
      })
      .catch(function (error) {
        console.log(error)
      })
    }
  },
  mounted() {
    let _this = this
    axios.get('http://localhost:8090/user/getInfo')
        .then(function (response) {
          _this.username = response.data.data.username
      }).catch(function (error) {
        // alert('请先登录')
      })
    EventBus.$on('update_username', (new_name) => {
      this.username = new_name
    })
  }
}
</script>

<style scoped>


</style>



