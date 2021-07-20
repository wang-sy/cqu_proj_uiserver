<template>
  <div ref="treeWrap">
    <a-card title="订单列表">
      <a-collapse v-model="activeKey">
        <a-collapse-panel key="1" header="未完成的订单">
          <a-list
          class="Order_List"
          :loading="loading"
          item-layout="horizontal"
          :data-source="list_completed"
          >
            <div
              v-if="showLoadingMore"
              slot="loadMore"
              :style="{ textAlign: 'center', marginTop: '12px', height: '32px', lineHeight: '32px' }"
            >
              <a-spin v-if="loadingMore" />
              <a-button v-else @click="onLoadMore_list_completed">
                加载更多
              </a-button>
            </div>
            <a-list-item slot="renderItem" slot-scope="item, index">
              <a slot="actions" @click="show_window(index, 1)">查看订单</a>
              <a slot="actions" @click="delete_list_completed(index)">删除订单</a>
              <a-list-item-meta
                :description="'描述:'+item.description+' 总价格:￥'+item.totalPrice+' 订单编号:'+item.list_id"
              >
                <a slot="title" href="https://www.antdv.com/">{{ item.name }}</a>
              </a-list-item-meta>
              <div class="Word_Color">进行中</div>
            </a-list-item>
          </a-list>
        </a-collapse-panel>
        <a-collapse-panel key="2" header="已完成的订单" :disabled="false">
          <a-list
          class="Order_List"
          :loading="loading"
          item-layout="horizontal"
          :data-source="list_incompleted"
          >
            <div
              v-if="showLoadingMore"
              slot="loadMore"
              :style="{ textAlign: 'center', marginTop: '12px', height: '32px', lineHeight: '32px' }"
            >
              <a-spin v-if="loadingMore" />
              <a-button v-else @click="onLoadMore_list_incompleted">
                加载更多
              </a-button>
            </div>
            <a-list-item slot="renderItem" slot-scope="item, index">
              <a slot="actions" @click="show_window(index, 2)">查看订单</a>
              <a slot="actions" @click="delete_list_incompleted(index)">删除订单</a>
              <a-list-item-meta
                :description="'描述:'+item.description+' 总价格:￥'+item.totalPrice+' 订单编号:'+item.list_id"
              >
                <a slot="title" href="https://www.antdv.com/">{{ item.name }}</a>
              </a-list-item-meta>
              <div>已完成</div>
            </a-list-item>
          </a-list>
        </a-collapse-panel>
      </a-collapse>
    </a-card>
    <OrderDetails :show="show" :list_data="cur_list_data" @hidden="hide_window"></OrderDetails>
  </div>
</template>

<script>
import OrderDetails from './OrderDetails.vue'

let list_completed = [
  {
    name: '七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:1,
  },
  {
    name: 'Ant Design Title 1',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:1
  },
  {
    name: 'ROG竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:1
  },
  {
    name: '七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:1,
  },
  {
    name: 'Ant Design Title 1',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:1
  },
  {
    name: 'ROG竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:1
  },
]
let list_incompleted = [
  {
    name: '七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:3
  },
  {
    name: 'Ant Design Title 1',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:3
  },
  {
    name: 'ROG竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    list_id: "12345",
    totalPrice: 475,
    statue:3
  }
]

export default {
  data() {
    return {
      loading: false,
      loadingMore: false,
      showLoadingMore: true,
      list_completed: list_completed,
      list_incompleted: list_incompleted,
      activeKey: 1,
      show: false,
      cur_list_data: {}
    };
  },
  components:{
    OrderDetails
  },
  mounted () {
    let _this = this;
    document.addEventListener('mouseup',(e) =>{
      let tree = this.$refs.treeWrap
      if (tree) {
      if (!tree.contains(e.target)) {
          this.show = false
        }
      }
    })      
  },
  methods: {
    onLoadMore_list_completed() {
      this.loadingMore = true;
      this.list_completed = this.list_completed.concat(list_completed);
      this.loadingMore = false;
    },
    onLoadMore_list_incompleted() {
      this.loadingMore = true;
      this.list_incompleted = this.list_incompleted.concat(list_incompleted);
      this.loadingMore = false;
    },
    delete_list_completed(index){
      this.list_completed.splice(index,1)
    },
    delete_list_incompleted(index){
      this.list_incompleted.splice(index,1)
    },
    hide_window() {
      this.show = false
    },
    show_window(index, i) {
      this.show = true
      if(i == 1)
        this.cur_list_data = this.list_completed[index]
      else
        this.cur_list_data = this.list_incompleted[index]
    }
  },
};
</script>

<style>
.Order_List {
  min-height: 300px;
}
.Word_Color{
  color: rgb(37, 133, 223)
}
</style>
