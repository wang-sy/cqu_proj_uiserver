<template>
    <a-modal v-model="show" :title="`订单: `+ list_data.list_id" :footer="null" width="50%">
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
                    Zhou Maomao
                </a-descriptions-item>
                <a-descriptions-item label="联系方式">
                    1810000000
                </a-descriptions-item>
                <a-descriptions-item label="收件地址">
                    Hangzhou, Zhejiang
                </a-descriptions-item>
                <a-descriptions-item label="订单编号">
                    {{ list_data.list_id }}
                </a-descriptions-item>
                <a-descriptions-item label="商品信息">
                    <a href="https://www.antdv.com/"> {{ list_data.name }} </a>
                </a-descriptions-item>
                <a-descriptions-item label="描述">
                    {{ list_data.description }}
                </a-descriptions-item>
                <a-descriptions-item label="订单价格">
                    ￥ {{ list_data.totalPrice }}
                </a-descriptions-item>
                <a-descriptions-item label="创建时间">
                    2020.2.2
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
        }
    }
}
</script>