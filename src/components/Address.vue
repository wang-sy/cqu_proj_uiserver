<template>
  <div>
    <a-modal v-model="visible" title="地址信息" :footer="null" width="50%" @cancel="visible_set">
      <a-button type="primary" @click="add_address">增加收货地址</a-button>
      <a-button type="primary" @click="upload_address" style="float: right">确定</a-button>
      <a-table rowKey="address" :columns="columns" :data-source="addresses" :scroll="{ x: 600}" bordered style="margin-top: 2%">
        <template v-for="i in columns" :slot="i.dataIndex" slot-scope="text, record">
          <a-input :key="i.dataIndex" contenteditable="true" @blur.capture="e => change_address(e.target.value, record)" v-model="text" style="width: 80%"></a-input>
        </template>
        <template slot="delete" slot-scope="text, record">
          <a-popconfirm v-if="addresses.length" title="确定删除收货地址？" @confirm="() => delete_address(record)">
            <a>删除</a>
          </a-popconfirm>
        </template>
      </a-table>
    </a-modal>
  </div>
</template>

<script>

export default {
  name: "Address",
  data () {
    return {
      visible: false,
      username: '',
      email: '',
      columns: [
        {title: '收货地址', align: 'center', dataIndex: 'address', key: 'address', scopedSlots: {customRender: 'address'}},
        {width: 100, dataIndex: 'delete', align: 'center', fixed: 'right', scopedSlots: {customRender: 'delete'}}
      ],
      addresses: []
    }
  },
  methods: {
    delete_address:function (record) {
      this.addresses.splice(this.addresses.indexOf(record), 1)
    },
    add_address:function () {
      this.addresses.push({address: '请输入地址'})
    },
    change_address:function (new_record, old_record) {
      this.addresses[this.addresses.indexOf(old_record)].address = new_record
    },
    visible_set: function () {
      this.visible = false
    },
    upload_address: function () {
      let addresses_ = []
      for (var i=0; i<this.addresses.length; i++) {
        addresses_.push(this.addresses[i].address)
      }
      this.$axios.post(this.$base_url + 'api/user/updateInfo', {
        username: this.username,
        email: this.email,
        address: addresses_
      }).then (function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error)
      })
    }
  },
  mounted() {
    this.$event_bus.$on('modify_address', ()=>{
      let _this = this
      this.$axios.get(this.$base_url + 'api/user/getInfo')
        .then(function (response) {
          if (response.data.code === -1) {
            alert(response.data.msg)
            return
          }
          _this.visible = true
          _this.email = response.data.data.email
          _this.username = response.data.data.username
          let addresses_ = response.data.data.address
          _this.addresses = []
          for (var i=0; i<addresses_.length; i++) {
            _this.addresses.push({'address': addresses_[i]})
        }
      }).catch(function (error) {
        alert('请先登录')
      })
    })
  }
}
</script>

<style scoped>

</style>
