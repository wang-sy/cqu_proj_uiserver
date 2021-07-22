<template>
    <!-- 提交订单对话框 -->
    <a-modal v-model="visiable" :title="'提交订单: ' + orderID " width="80%">
        <!-- 确认商品详情 -->
        <a-list item-layout="horizontal" :data-source="commoditys">
            <a-list-item
                slot="renderItem"
                slot-scope="item"
            >
                <div style="width: 80%">
                    <a-list-item-meta
                        :description="item.description"
                    >
                        <a
                            slot="title"
                            style="font-size: 1.2em"
                            @click="toGoodPage(item.id)"
                        >
                            {{ item.name }}
                        </a>
                        <img
                            slot="avatar"
                            :src="item.figure"
                            :href="'/good?id=' + item.id"
                            style="width: 110px; height: 82px;"
                        />
                    </a-list-item-meta>
                </div>
                <div style="width: 20%">
                    <!-- price -->
                    <h3 style="font-size: 1em">
                        单价：¥ {{ item.pricePerOne }}
                    </h3>
                    <!-- counter -->
                    <h3 style="font-size: 1em">
                        数量： {{item.number}}
                    </h3>
                    <h3 style="font-size: 1em">
                        总价：¥ {{ item.totalPrice }}
                    </h3>
                </div>
            </a-list-item>
        </a-list>
        <a-divider/>
        <b style="float: right; font-size: 1.3em;">商品总价：¥ {{totalPrice}} </b>
        <template slot="footer">
            <a-button type="primary" style="width:100%; position: related" size="large" @click="handleSubmit">去支付</a-button>
        </template>
    </a-modal>
</template>

<script>
import { EventBus } from '../event-bus'

export default {
    data() {
        return {
            visiable: false,
            commoditys: [],
            current: 1,
            footerBottonMsg: '下一步',
            orderID: 0,
            totalPrice: 0,
        }
    },
    mounted() {
        EventBus.$off('submitOrder')
        EventBus.$on('submitOrder', this.initSubmitOrder)
    },
    methods: {
        async initSubmitOrder(goods) {
            this.visiable = true
            this.current = 1
            this.footerBottonMsg = '下一步'
            this.commoditys = goods
            
            let orderInfo = await this.initOrder()
            this.totalPrice = orderInfo.totalPrice
            this.orderID = orderInfo.id

            console.log(this.commoditys)
        },
        toGoodPage(goodID) {
            this.$router.push({
                path: "/good",
                query: {
                    id: goodID
                }
            })
        },
        handleSubmit() {
            console.log("pay")
        },
        async initOrder() {
            let goods = []
            for (let i = 0; i < this.commoditys.length; i ++) {
                goods.push({
                    gid: this.commoditys[i].id,
                    num: this.commoditys[i].number
                })
            }
            
            console.log(goods)

            let data = await this.$axios({
                method: 'POST',
                url: this.$base_url + '/api/order/addOrder',
                data: {
                    goods: goods,
                    address: "重庆大学虎溪校区竹园四栋",
                    phone: "13969003119"
                }
            })
            
            console.log(data)

            return {
                totalPrice: 1000,
                id: 10000,
            } 
        }
    }
}

</script>

<style scoped>

</style>
