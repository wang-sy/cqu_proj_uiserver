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
              v-if="showLoadingMore_completed"
              slot="loadMore"
              :style="{ textAlign: 'center', marginTop: '12px', height: '32px', lineHeight: '32px' }"
            >
              <a-spin v-if="loadingMore_completed" />
              <a-button v-else @click="onLoadMore_list_completed">
                加载更多
              </a-button>
            </div>
            <a-list-item slot="renderItem" slot-scope="item, index">
              <a slot="actions" @click="show_window(index, 1)">查看订单</a>
              <a slot="actions" @click="delete_list_completed(index)">删除订单</a>
              <a-list-item-meta
                :description="'描述:'+item.goods+' 总价格:￥'+item.Price"
              >
                <a slot="title" @click="show_window(index, 1)"> 订单:{{ item.orderNum }} </a>
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
              v-if="showLoadingMore_incompleted"
              slot="loadMore"
              :style="{ textAlign: 'center', marginTop: '12px', height: '32px', lineHeight: '32px' }"
            >
              <a-spin v-if="loadingMore_incompleted" />
              <a-button v-else @click="onLoadMore_list_incompleted">
                加载更多
              </a-button>
            </div>
            <a-list-item slot="renderItem" slot-scope="item, index">
              <a slot="actions" @click="show_window(index, 2)">查看订单</a>
              <a slot="actions" @click="delete_list_incompleted(index)">删除订单</a>
              <a-list-item-meta
                :description="'描述:'+item.good+' 总价格:￥'+item.Price"
              >
                <a slot="title" @click="show_window(index, 2)">{{ item.orderNum }}</a>
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
import axios from 'axios';
import OrderDetails from './OrderDetails.vue'

let list_completed = [
  {
    name: ['七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）','Ant Design Title 1'],
    description:"Fuck and Shit",
    goodID: [0, 1],
    list_id: "12345",
    totalPrice: 475,
    statue:0,
  },
  {
    name: ['Ant Design Title 1'],
    description:"Fuck and Shit",
    goodID: 1,
    list_id: "12345",
    totalPrice: 475,
    statue:1
  },
  {
    name: ['ROG竞速3070显卡（吃鸡英雄联盟绝地求生）'],
    description:"Fuck and Shit",
    goodID: 2,
    list_id: "12345",
    totalPrice: 475,
    statue:2
  },
]
let list_incompleted = [
  {
    name: ['七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）'],
    description:"Fuck and Shit",
    goodID: 0,
    list_id: "12345",
    totalPrice: 475,
    statue:3,
  },
  {
    name: ['Ant Design Title 1'],
    description:"Fuck and Shit",
    goodID: 1,
    list_id: "12345",
    totalPrice: 475,
    statue:3
  },
  {
    name: ['ROG竞速3070显卡（吃鸡英雄联盟绝地求生）'],
    description:"Fuck and Shit",
    goodID: 2,
    list_id: "12345",
    totalPrice: 475,
    statue:3
  },
]

export default {
  data() {
    return {
      loading: true,
      loadingMore_completed: false,
      loadingMore_incompleted: false,
      showLoadingMore_completed: false,
      showLoadingMore_incompleted: false,
      list_completed: [],
      list_incompleted: [],
      now_page_completed: 1,
      now_page_incompleted: 1,
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
    this.init()
    this.loading = false
  },
  methods: {
    async init() {
      let _this=this
      axios({
        method: 'POST',
        url: this.$base_url + `/api/order/searchByCustomerIdDo`,
        data: {}
      }).then((res) => {
        if(res.data.length <= 5){
          _this.list_completed = res.data
          _this.showLoadingMore_completed = false
        }
        else {
          _this.list_completed = res.data.slice(0, 5)
          _this.showLoadingMore_completed = true
        }
      }).catch((error) => {
        console.error(error)
      })
      axios({
        method: 'POST',
        url: _this.$base_url + `/api/order/searchByCustomerIdUndo`,
        data: {}
      }).then((res) => {
        if(res.data.length <= 5){
          _this.list_incompleted = res.data
          _this.showLoadingMore_incompleted = false
        }
        else {
          _this.list_incompleted = res.data.slice(0, 5)
          _this.showLoadingMore_incompleted = true
        }
      }).catch((error) => {
        console.error(error)
      })
    },
    onLoadMore_list_completed() {
      this.loadingMore_completed = true;
      this.list_completed = this.list_completed.concat(list_completed);
      let _this=this
      axios({
        method: 'POST',
        url: _this.$base_url+`/api/order/searchByCustomerIdDo`,
        data: {}
      }).then((res) => {
        _this.list_completed = _this.list_completed.concat(res.data.slice(_this.now_page_completed*5, (_this.now_page_completed+1)*5))
        _this.now_page_completed++
        if(res.data.length >= _this.now_page_completed*5){
          _this.showLoadingMore_completed = true
        }
        else {
          _this.showLoadingMore_completed = false
        }
      }).catch((error) => {
        console.error(error)
      })
      this.loadingMore_completed = false;
    },
    onLoadMore_list_incompleted() {
      this.loadingMore_incompleted = true;
      this.list_incompleted = this.list_incompleted.concat(list_incompleted);
      axios({
        method: 'POST',
        url: _this.$base_url+`/api/order/searchByCustomerIdUndo`,
        data: {}
      }).then((res) => {
        _this.list_incompleted = _this.list_incompleted.concat(res.data.slice(_this.now_page_incompleted*5, (_this.now_page_incompleted+1)*5))
        _this.now_page_incompleted++
        if(res.data.length >= _this.now_page_incompleted*5){
          _this.showLoadingMore_incompleted = true
        }
        else {
          _this.showLoadingMore_incompleted = false
        }
      }).catch((error) => {
        console.error(error)
      })
      this.loadingMore_incompleted = false;
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
    },
    toGoodPage(goodID){
      this.$router.push({
        path: "/good",
        query: {
            id: goodID
        } 
      })
    }
  },
};
</script>

<style>
.Order_List {
  min-height: 100px;
}
.Word_Color{
  color: rgb(37, 133, 223)
}
</style>
