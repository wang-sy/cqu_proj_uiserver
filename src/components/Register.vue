<template>
  <div>
    <a-modal v-model="visible" title="注册" :keyboard="false"
             :okText="ok_text" :footer="null" @cancel="login">
      <a-input placeholder="电话" style="width: 100%" v-model="phone">
        <a-icon slot="prefix" type="phone" style="color: red"/>
      </a-input>
      <br /> <br />
      <a-input placeholder="邮箱" style="width: 100%" v-model="email">
        <a-icon slot="prefix" type="mail" />
      </a-input>
      <br /> <br />
      <a-input placeholder="收货地址" style="width: 100%" v-model="address">
        <a-icon slot="prefix" type="arrow-down" />
      </a-input>
      <br /> <br />
      <a-input placeholder="用户名" style="width: 100%" v-model="uname">
        <a-icon slot="prefix" type="user" />
      </a-input>
      <br /> <br />
      <a-input-password placeholder="密码" style="width: 100%" v-model="password">
        <a-icon slot="prefix" type="lock" style="color: red"></a-icon>
      </a-input-password>
      <br /> <br />
      <a-input-password placeholder="确认密码" style="width: 100%" v-model="password_">
        <a-icon slot="prefix" type="lock" style="color: red"></a-icon>
      </a-input-password>
      <br /> <br />
      <li style="color: red" v-if="error">{{error_info}}</li>
      <br />
      <a-button type="primary" style="width: 100%" @click="register">注册</a-button>
    </a-modal>
  </div>
</template>

<script>
import {EventBus} from '../event-bus'
import axios from 'axios'


export default {
  name: 'Register',
  data () {
    return {
      phone: '',
      email: null,
      address: null,
      uname: null,
      password: '',
      password_: '',
      visible: false,
      ok_text: '注册',
      error: false,
      error_info: '',
    }
  },
  methods: {
    register: function () {
      var  re = /^\d{11}$/
      if (this.phone === '' || this.password === '' || this.password_ === '') {
        this.error = true
        this.error_info = '请输入手机号或密码'
        return
      } else if (this.password !== this.password_) {
        this.error = true
        this.error_info = '两次密码输入错误'
        return
      } else if (re.test(this.phone) === false) {
        this.error = true
        this.error_info = '请输入正确手机号'
        return
      } else if (this.password.length < 6) {
        this.error = true
        this.error_info = '密码长度不足六位'
        return
      }
      this.visible = false
      EventBus.$emit('on_login')
      axios.post('http://localhost:8090/user/register', {
        phone: this.phone, password: this.password, username: this.uname,
        email: this.email, address: this.address
      })
      .then(function (response) {
        console.log(response)
        if (response.data.code === -1) {
          alert('用户已存在')
        } else {
          alert('注册成功')
        }
      })
      .catch(function (error) {
        alert('注册失败')
      })
    },
    login: function () {
      this.visible = false
      EventBus.$emit('on_login')
    }
  },
  mounted() {
    EventBus.$on('on_register', () => {
      console.log('register')
      this.visible = true
    })
  }
};
</script>
