<template>
  <div>
    <Address></Address>
    <ModifyPersonInfo></ModifyPersonInfo>
    <Password></Password>
    <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" style="width: 5%; height: 5%"/>
    <div style="display: inline; font-size: 1.2em; margin-left: 2%">{{user_name}}</div>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_person_info">更多信息</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_address">收货地址</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_password">修改密码</a>
  </div>
</template>

<script>
import {EventBus} from '../event-bus'
import Address from './Address'
import ModifyPersonInfo from './ModifyPersonInfo'
import Password from './Password'

export default {
  name: 'PersonInfo',
  components: {
    Password,
    ModifyPersonInfo,
    Address
  },
  data () {
    return {
      user_name: '陈养鱼'
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
    }
  }
}
</script>

<style scoped>


</style>



