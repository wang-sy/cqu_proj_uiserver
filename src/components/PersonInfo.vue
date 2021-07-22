<template>
  <div>
    <Address></Address>
    <ModifyPersonInfo></ModifyPersonInfo>
    <Password></Password>
    <a-upload style="display: inline" :show-upload-list='false'
              :action="this.$base_url + 'api/user/uploadAvatar'" @change="upload_avatar" list-type="picture">
      <a-avatar :src=avatar></a-avatar>
    </a-upload>
    <div style="display: inline; font-size: 1.2em; margin-left: 2%">{{username}}</div>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_person_info">更多信息</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_address">收货地址</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="modify_password">修改密码</a>
    <a style="margin-left: 12%; font-size: 1.2em" @click="logout">注销登录</a>
  </div>
</template>

<script>
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
      username: '未设置用户名',
      avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'
    }
  },
  methods: {
    modify_person_info: function () {
      this.$event_bus.$emit('modify_person_info')
    },
    modify_address: function () {
      this.$event_bus.$emit('modify_address')
    },
    modify_password: function () {
      this.$event_bus.$emit('modify_password')
    },
    upload_avatar: function (upload_info) {
      console.log(upload_info)
      // this.avatar = upload_info.file.file.response.data.avatar_url
    },
    logout: function () {
      let _this = this
      this.$axios.get(this.$base_url + 'api/user/logout')
      .then(function (response) {
        if (response.data.code === 200) {
          _this.username = '未设置用户名'
          alert('注销成功')
          location.reload()
        } else {
          alert('注销失败')
        }
      })
      .catch(function (error) {
        alert('注销失败')
      })
    }
  },
  mounted() {
    let _this = this
    this.$axios.get(this.$base_url + 'api/user/getInfo')
        .then(function (response) {
          _this.username = response.data.data.username
          _this.avatar = _this.$base_url + response.data.data.avatar_url
      }).catch(function (error) {
        // alert('请先登录')
      })
    this.$event_bus.$on('update_username', (new_name) => {
      this.username = new_name
    })
    this.$event_bus.$on('login_success', (name, avatar_url) => {
      this.username = name
      this.avatar = avatar_url
    })
  }
}
</script>

<style scoped>


</style>



