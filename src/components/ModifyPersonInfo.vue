<template>
  <div>
    <a-modal v-model="visible" title="个人信息" :footer="null" width="40%" @cancel="visible_set">
      <a-descriptions>
        <a-descriptions-item label="电话" contentEditable=true>
          <br />
          <a-input placeholder="电话" style="width: 80%" v-model="phone" :disabled="true"></a-input>
        </a-descriptions-item>
        <a-descriptions-item label="邮箱">
          <br />
          <a-input placeholder="邮箱" style="width: 80%" v-model="email"></a-input>
        </a-descriptions-item>
        <a-descriptions-item label="用户名">
          <br />
          <a-input placeholder="用户名" style="width: 80%" v-model="username"></a-input>
        </a-descriptions-item>
      </a-descriptions>
      <br />
      <a-button type="primary" style="width: 100%" @click="modify">修改</a-button>
    </a-modal>
  </div>
</template>

<script>
import {EventBus} from '../event-bus'
import axios from "axios"

export default {
  name: "ModifyPersonInfo",
  data () {
    return {
      visible: false,
      phone: '',
      email: '',
      address: '',
      username: ''
    }
  },
  methods: {
    visible_set: function () {
      this.visible = false
    },
    modify: function () {
      axios.post('http://localhost:8090/user/updateInfo', {
        username: this.username,
        email: this.email,
        address: this.address
      }).then (function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    }
  },
  mounted() {
    EventBus.$on('modify_person_info', ()=>{
      this.visible = true
      let _this = this
      axios.get('http://localhost:8090/user/getInfo')
        .then(function (response) {
        _this.phone = response.data.data.phone
        _this.email = response.data.data.email
        _this.username = response.data.data.username
        _this.address = response.data.data.address
      }).catch(function (error) {
        // alert('请先登录')
      })
    })
  }
}
</script>

<style scoped>

</style>

