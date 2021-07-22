<template>
    <a-card hoverable>
        <img
            slot="cover"
            alt="example"
            :src="figure"
            @click="toGoodPage()"
        />
        <a-card-meta>
            <template slot="title">
                <a @click="toGoodPage()">{{name}}</a>
            </template>
            <template slot="description">
                {{description}}
                <a-row>
                    <a-col :span="12" style="margin-top: 8px"><b>{{price}} ¥</b></a-col>
                    <a-col :span="12">
                        <a-button type="dashed" style="width: 100%" @click="buy">立刻购买</a-button>
                    </a-col>
                </a-row>
            </template>
        </a-card-meta>
    </a-card>
</template>

<script>
export default {
    props: {
        id: Number,
        name: String,
        description: String,
        figure: String,
        price: Number
    },
    methods: {
        toGoodPage() {
            this.$router.push({
                path: "/good",
                query: {
                    id: this.id
                } 
            })
        },
        buy() {
            this.$submitOrder([{
                id: this.id,
                name: this.name,
                description: this.description,
                figure: this.figure,
                pricePerOne: this.price,
                number: 1,
                totalPrice: this.price 
            }])
        }
    }
}

</script>

<style scoped>

</style>