<template>
  <div>
    <a-modal v-model="visible" title="登录" :footer="null">
      <a-input placeholder="电话" style="width: 100%" v-model="phone">
        <a-icon slot="prefix" type="user" />
      </a-input>
      <br /> <br />
      <a-input-password placeholder="密码" style="width: 100%" v-model="password">
        <a-icon slot="prefix" type="lock"></a-icon>
      </a-input-password>
      <br /> <br />
      <a-button type="primary" style="width: 100%" @click="login">登录</a-button>
      <br /> <br />
      <a-button type="default" style="width: 100%" @click="register">注册</a-button>
    </a-modal>
  </div>
</template>

<script>
import {EventBus} from '../event-bus'
import axios from "axios"

export default {
  name: 'Login',
  data () {
    return {
      phone: '',
      password: '',
      visible: false
    }
  },
  methods: {
    login: function () {
      let _this = this
      axios.post('http://localhost:8090/user/login', {
        phone: this.phone,
        password: this.password
      })
      .then(function (response) {
        console.log(response)
        if (response.data.code === -1) {
          alert('登录失败，请重试')
        } else {
          _this.visible = false
        }
      })
      .catch(function (error) {
        alert('登录失败，请重试')
      })
    },
    register: function () {
      this.visible = false
      EventBus.$emit('on_register')
    }
  },
  mounted() {
    EventBus.$on('on_login', () => {
      this.visible = true
    })
  },
  beforeCreate() {
    let _this = this
    axios.get('http://localhost:8090/user/getInfo')
      .then(function (response) {
      _this.visible = response.data.code !== 200;
    }).catch(function (error) {
      _this.visible = true
    })
  }
};
</script>
