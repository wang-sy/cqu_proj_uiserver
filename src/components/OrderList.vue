<template>
  <a-card title="订单列表">
    <div>
      <a-collapse v-model="activeKey">
        <a-collapse-panel key="1" header="未完成的订单">
          <a-list
          class="Order_list"
          :loading="loading"
          item-layout="horizontal"
          :data-source="data1"
          >
            <div
              v-if="showLoadingMore"
              slot="loadMore"
              :style="{ textAlign: 'center', marginTop: '12px', height: '32px', lineHeight: '32px' }"
            >
              <a-spin v-if="loadingMore" />
              <a-button v-else @click="onLoadMore1">
                加载更多
              </a-button>
            </div>
            <a-list-item slot="renderItem" slot-scope="item, index">
            <!-- <a-list-item slot="renderItem" slot-scope="item">   -->
              <a slot="actions" href="https://www.baidu.com/">查看订单</a>
              <a slot="actions" @click="deleteItem1(index)">删除订单</a>
              <a-list-item-meta
                :description="'描述:'+item.description+' 单价:￥'+item.price+' 数量:'+item.number+' 总价格:￥'+item.totalPrice"
              >
                <a slot="title" href="https://www.antdv.com/">{{ item.name }}</a>
              </a-list-item-meta>
              <div class="word_color">进行中</div>
            </a-list-item>
          </a-list>
        </a-collapse-panel>
        <a-collapse-panel key="2" header="已完成的订单" :disabled="false">
          <a-list
          class="Order_list"
          :loading="loading"
          item-layout="horizontal"
          :data-source="data2"
          >
            <div
              v-if="showLoadingMore"
              slot="loadMore"
              :style="{ textAlign: 'center', marginTop: '12px', height: '32px', lineHeight: '32px' }"
            >
              <a-spin v-if="loadingMore" />
              <a-button v-else @click="onLoadMore2">
                加载更多
              </a-button>
            </div>
            <a-list-item slot="renderItem" slot-scope="item, index">
            <!-- <a-list-item slot="renderItem" slot-scope="item">   -->
              <a slot="actions" href="https://www.baidu.com/">查看订单</a>
              <a slot="actions" @click="deleteItem2(index)">删除订单</a>
              <a-list-item-meta
                :description="'描述:'+item.description+' 单价:￥'+item.price+' 数量:'+item.number+' 总价格:￥'+item.totalPrice"
              >
                <a slot="title" href="https://www.antdv.com/">{{ item.name }}</a>
              </a-list-item-meta>
              <div>已完成</div>
            </a-list-item>
          </a-list>
        </a-collapse-panel>
      </a-collapse>
    </div>
  </a-card>
</template>

<script>

let data1 = [
  {
    name: '七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    price: 47.5,
    number: 10,
    totalPrice: 475
  },
  {
    name: 'Ant Design Title 1',
    description:"Fuck and Shit",
    price: 47.5,
    number: 10,
    totalPrice: 475
  },
  {
    name: 'ROG竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    price: 47.5,
    number: 10,
    totalPrice: 475
  }
]
let data2 = [
  {
    name: '七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    price: 47.5,
    number: 10,
    totalPrice: 475
  },
  {
    name: 'Ant Design Title 1',
    description:"Fuck and Shit",
    price: 47.5,
    number: 10,
    totalPrice: 475
  },
  {
    name: 'ROG竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description:"Fuck and Shit",
    price: 47.5,
    number: 10,
    totalPrice: 475
  }
]

export default {
  data() {
    return {
      loading: false,
      loadingMore: false,
      showLoadingMore: true,
      data1: data1,
      data2: data2
    };
  },
  methods: {
    onLoadMore1() {
      this.loadingMore = true;
      this.data1 = this.data1.concat(data1);
      this.loadingMore = false;
    },
    onLoadMore2() {
      this.loadingMore = true;
      this.data2 = this.data2.concat(data1);
      this.loadingMore = false;
    },
    deleteItem1(index){
      this.data1.splice(index,1)
    },
    deleteItem2(index){
      this.data2.splice(index,1)
    }
  },
};
</script>

<style>
.Order-list {
  min-height: 350px;
}
.word_color{
  color: rgb(37, 133, 223)
}
</style>