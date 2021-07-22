<template>
    <a-card title="购物车">
        <a-list item-layout="horizontal" :data-source="commoditys">
            <a-list-item
                slot="renderItem"
                slot-scope="item, index"
                :style=" item.selected ?
                'background-color: #fbfbfb' : ''"
            >
                <div style="width: 5%">
                    ·
                    <a-checkbox v-model="item.selected" ></a-checkbox>
                </div>
                <div style="width: 60%">
                    <a-list-item-meta
                        :description="item.description"
                    >
                        <a
                            slot="title"
                            @click="toGoodPage(item.id)"
                            style="font-size: 1.2em"
                        >
                            {{ item.name }}
                        </a>
                        <img
                            slot="avatar"
                            :src="item.figure"
                            @click="toGoodPage(item.id)"
                            style="width: 110px; height: 82px;"
                        />
                    </a-list-item-meta>
                </div>
                <div style="width: 30%">
                    <!-- price -->
                    <h3 style="font-size: 1em">
                        单价：¥ {{ item.pricePerOne }}
                    </h3>
                    <!-- counter -->
                    <h3 style="font-size: 1em">
                        数量：
                        <a-input
                            style="width: 20%"
                            v-model="item.number"
                            size="small"
                            @change="changeNumber(item)"
                        />
                    </h3>
                    <h3 style="font-size: 1em">
                        总价：¥ {{ item.totalPrice }}
                    </h3>
                </div>
                <a-icon style="position: related; right: 100px; width: 5%" type="delete" @click="deleteItem(index)"/>
            </a-list-item>
        </a-list>
        <a-button
            type="primary"
            style="left: 20%; width: 60%; margin-top: 1vh"
            size="large"
            @click="submit"
        >
            下单
        </a-button>
    </a-card>
</template>

<script>
import { EventBus } from '../event-bus';

let commoditys = [
  {
    name: '七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description: "Fuck and Shit",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
    id: 0,
  },
  {
    name: 'Ant Design Title 1',
    description: "Fuck and Shit",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
    id: 0,
  },
  {
    name: 'Ant Design Title 1',
    description: "Fuck and Shit",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
    id: 0,
  },
  {
    name: 'Ant Design Title 1',
    description: "Fuck and Shit",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
    id: 0,
  },
];

export default {
    data() {
        return {
           commoditys: commoditys
        }
    },
    methods: {
        changeNumber(item) {
            if (item.number < 0) {
                item.number = 0
            }

            item.totalPrice = item.number * item.pricePerOne
            this.$getShoppingCart(this.commoditys)
        },
        deleteItem(index) {
            this.commoditys.splice(index,1)
            this.$setShoppingCart(this.commoditys)
        },
        updateSelected(item) {
            item.selected = !item.selected
            this.$getShoppingCart(this.commoditys)
        },
        submit() {
            let selectedGoods = []
            let newList = []

            // 顺序扫描购物车, 删除已选项目
            for (let i = 0; i < this.commoditys.length; i ++) {
                if (this.commoditys[i].selected === true) {
                    selectedGoods.push(this.commoditys[i])
                } else {
                    newList.push(this.commoditys[i])
                }
            }

            this.commoditys = newList
            this.$setShoppingCart(newList)

            this.$submitOrder(selectedGoods)
        },
        toGoodPage(goodID) {
            this.$router.push({
                path: "/good",
                query: {
                    id: goodID
                } 
            })
        }
    },
    // get prices.
    beforeMount() {
        // load commoditys from localStorage
        this.commoditys = this.$getShoppingCart()

        for (let i = 0; i < this.commoditys.length; i ++) {
            this.commoditys[i].totalPrice = this.commoditys[i].number * this.commoditys[i].pricePerOne
        }
    }
}

</script>

<style scoped>
.list-item{
    display: flex;
    width: 100%;
}
</style>
