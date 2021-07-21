<template>
  <div>
    <a-modal v-model="visible" title="修改密码" :footer="null" width="40%" @cancel="visible_set">
      <a-input-password placeholder="密码" style="width: 100%" v-model="old_password">
        <a-icon slot="prefix" type="lock"></a-icon>
      </a-input-password>
      <br /> <br />
      <a-input-password placeholder="确认密码" style="width: 100%" v-model="new_password">
        <a-icon slot="prefix" type="lock"></a-icon>
      </a-input-password>
      <br /> <br />
      <a-input-password placeholder="确认密码" style="width: 100%" v-model="new_password_">
        <a-icon slot="prefix" type="lock"></a-icon>
      </a-input-password>
      <br /> <br />
      <li style="color: red" v-if="error">{{error_info}}</li>
      <br />
      <a-button type="primary" style="width: 100%" @click="update">修改</a-button>
    </a-modal>
  </div>
</template>

<script>
import {EventBus} from '../event-bus'
import axios from "axios";

export default {
  name: "Password",
  data () {
    return {
      visible: false,
      old_password: '',
      new_password: '',
      new_password_: '',
      error: false,
      error_info: '',
    }
  },
  methods: {
    visible_set: function () {
      this.visible = false
    },
    update: function () {
      if (this.new_password !== this.new_password_) {
        this.error = true
        this.error_info = '两次密码输入不匹配'
        return
      } else if (this.new_password.length < 6) {
        this.error = true
        this.error_info = '密码长度不足六位'
        return
      }
      let _this = this
      this.error = false
      axios.post('http://localhost:8090/user/updatePwd', {
        oldPwd: this.old_password, newPwd: this.new_password
      })
      .then(function (response) {
        console.log(response)
        if (response.data.code === -1) {
          alert(response.data.msg)
        } else {
          _this.visible = false
          _this.old_password = ''
          _this.new_password = ''
          _this.new_password_ = ''
          alert(response.data.msg)
        }
      })
      .catch(function (error) {
        alert('修改失败')
      })
    }
  },
  mounted() {
    EventBus.$on('modify_password', ()=>{
      this.visible = true
    })
  },
}
</script>

<style scoped>

</style>
