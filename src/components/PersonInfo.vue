<template>
    <a-layout style="height: 5%">
      <a-layout-sider style="max-width: 100px; min-width: 100px; width: 60px; height: 100px; background: white">
        <a-avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" style="width: 100%; height: 100%"/>
      </a-layout-sider>
      <a-layout style="margin-left: 2%">
        <Header>
          <div style="font-size: 24px; display: inline">用户名：{{user_name}}</div>
        </Header>
        <a-layout-content>
          <div style="margin-top: 1%">
            <a-collapse>
              <a-collapse-panel header="收货地址" key="1">
                <a-button type="primary" @click="addAddress">增加收货地址</a-button>
                <a-table rowKey="address" :columns="columns" :data-source="addresses" :scroll="{ x: 900}" bordered>
                  <template v-for="i in columns" :slot="i.dataIndex" slot-scope="text">
                    <span :key="i.dataIndex" contentEditable=true>{{text}}</span>
                  </template>
                  <template slot="action" slot-scope="text, record">
                    <a-popconfirm v-if="addresses.length" title="确定删除收货地址？" @confirm="() => deleteAddress(record)">
                      <a>删除</a>
                    </a-popconfirm>
                  </template>
                </a-table>
              </a-collapse-panel>
            </a-collapse>
          </div>
        </a-layout-content>
      </a-layout>
    </a-layout>
</template>

<script>

export default {
  name: 'PersonInfo',
  data () {
    return {
      user_name: 'cyy',
      // address: '重庆市重庆大学虎溪校区竹四301',
      columns: [
        {title: '收货地址', align: 'center', dataIndex: 'address', key: 'address', scopedSlots: {customRender: 'address'}},
        {width: 100, title: '操作', dataIndex: 'action', align: 'center', fixed: 'right', scopedSlots: {customRender: 'action'}}
      ],
      addresses: [
        {address: '重庆市重庆大学虎溪校区竹四301'},
        {address: '重庆市重庆大学虎溪校区竹四302'},
        {address: '重庆市重庆大学虎溪校区竹四303'},
      ]
    }
  },
  methods: {
    deleteAddress:function (record) {
      this.addresses.splice(this.addresses.indexOf(record), 1)
    },
    addAddress:function () {
      this.addresses.push({address: '请输入地址'})
    }
  }
}
</script>

<style scoped>


</style>



