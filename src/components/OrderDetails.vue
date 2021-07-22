<template>
    <a-modal v-model="show" :title="`订单: `+ list_data.orderNum" :footer="null" width="50%">
        <div>
            <a-steps :current="list_data.statue">
                <a-step title="待付款" />
                <a-step title="待发货" />
                <a-step title="运输中" />
                <a-step title="完成" />
            </a-steps>
        </div>
        <a-divider />
        <div style="margin-top: 24px">
            <a-descriptions>
                <a-descriptions-item label="收件人">
                    {{ list_data.customerId }}
                </a-descriptions-item>
                <a-descriptions-item label="联系方式">
                    {{ list_data.phone }}
                </a-descriptions-item>
                <a-descriptions-item label="收件地址">
                    {{ list_data.address }}
                </a-descriptions-item>
                <a-descriptions-item label="订单编号">
                    {{ list_data.orderNum }}
                </a-descriptions-item>
                <a-descriptions-item label="订单价格">
                    ￥{{ list_data.price }}
                </a-descriptions-item>
                <a-descriptions-item label="创建时间">
                    {{ list_data.time }}
                </a-descriptions-item>
                <a-descriptions-item label="快递信息">
                    {{ list_data.mailProvider }}  快递单号:{{ list_data.mailNumber }}
                </a-descriptions-item>
                <a-descriptions-item label="商品信息">
                    <a-col a-col v-for="(item, index) in list_data.goods" :key="index">
                        <a @click="toGoodPage(list_data.goods[index].gid)">商品名称:{{ list_data.goods[index].name }} 数量:{{list_data.goods[index].num}} </a>
                    </a-col>
                </a-descriptions-item>
            </a-descriptions>
        </div>
        <a-button type="primary" block @click="hidden">确认</a-button>
    </a-modal>
</template>

<script>
export default {
    name: 'OrderDetails',
    props: {
        show: {
            type: Boolean,
            default: false
        },
        list_data: {}
    },
    methods: {
        hidden() {
            this.$emit('hidden')
        },
        toGoodPage(goodID)
        {
            this.$router.push({
                path: "/good",
                query: {
                    id: goodID
                }
            })          
        }
    }
}
</script>