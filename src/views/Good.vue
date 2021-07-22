<template>
    <main>
        <!-- base info for good -->
        <a-card :bordered="false">
            <a-row flex>
                <!-- figure -->
                <a-col :span="10"><a-card style="width: 100%">
                    <a-carousel autoplay arrows>
                        <div v-for="(item, index) in good.pics" :key="index">
                            <img style="width: 100%; height: 50vh" :src="item"/>
                        </div>
                    </a-carousel>
                </a-card></a-col>

                <!-- empty col -->
                <a-col :span="1"/>
                
                <!-- prod info -->
                <a-col :span="13"><div>
                    <b style="font-size: 1.5em">{{good.name}}</b>
                    <p style="font-size: 0.8em; color: #909090; margin-top: 2vh"> {{good.desc}} </p>
                    <!-- price -->
                    <a-row style="margin-top: 3vh">
                            <b style="font-size: 1em; color: #808080"> 单价： </b>
                            <b style="font-size: 1.5em; color: #ff6060"> ¥{{good.price}}</b>
                    </a-row>

                    <!-- number & totalPrice -->
                    <a-row style="margin-top: 3vh">
                        <a-col :span="8">
                            <b style="font-size: 1em; color: #808080"> 购买： </b>
                            <a-input 
                                style="width: 40%"
                                v-model="number"
                                @change="updateNumber"
                            />
                            <b style="font-size: 1em; color: #808080"> 件 </b>
                        </a-col>
                        <a-col :span="12">
                            <b style="font-size: 1em; color: #808080"> 预计总价： </b>
                            <b style="font-size: 1.5em; color: #ffa0a0"> {{totalPrice}} </b>
                        </a-col>
                    </a-row>

                    <!-- add it into shopping cart && buy it now -->
                    <a-row style="margin-top: 10vh; bottom: 10px"> 
                        <a-col :span="11">
                            <a-button
                                style="width: 100%"
                                size="large"
                                @click="submitOrder"
                            > 立即购买 </a-button>
                        </a-col>
                        <a-col :span="1"> </a-col>
                        <a-col :span="11">
                            <a-button
                                style="background-color: rgb(252,238, 237); width: 100%"
                                size="large"
                            > 加入购物车 </a-button>
                        </a-col>
                    </a-row>
                </div></a-col>
            </a-row>
        </a-card>

        <!-- extra infos -->
        <a-card :bordered="false" style="margin-top: 3vh">
            <a-row :gutter="[8,8]">
                <a-col v-for="cValue, cKey, cIndex in good.params" :key="cIndex" :span="8">
                    <a-card style="text-align: center">
                    <p style="font-size: 1.2em; color: #808080;"> {{cKey}} </p>
                    <div v-for="featureValue, featureKey, fIndex in cValue" :key="fIndex">
                        <a-row v-if="featureValue.length < 20">
                            <a-col :span="12" style="background-color: #fdfdfd;">
                                {{featureKey}}
                            </a-col>
                            <a-col :span="1" style="background-color: #fafafa; color: #f8f8f8">
                                |
                            </a-col>
                            <a-col :span="11" style="background-color: #fdfdfd;">{{featureValue}}</a-col>
                        </a-row>
                    </div></a-card>
                </a-col>
            </a-row>
        </a-card>
    </main>
</template>

<script>
export default {
    data() {
        return {
            good: {},
            number: 1,
            totalPrice: 0
        }
    },
    mounted() {
        let _this = this
        let id = this.$route.query.id
        this.getGoodByID(id)
            .then((data) => {
                _this.good = data
                _this.totalPrice = data.price
            })
    },
    methods: {
        /**
         * get good by googID
         */
        async getGoodByID(id) {
            console.log("Get Data")
            let _this = this;
            let data = await this.$axios({
                method: 'GET',
                url: _this.$base_url + `api/goods/getGoods?gid=${id}`
            })

            return {    
                id: data.data.gid,
                name: data.data.name,
                desc: data.data.desc,
                type: data.data.type,
                price: data.data.price,
                pics: data.data.pic_groups,
                params: data.data.good_params
            }
        },
        updateNumber() {
            if (this.number < 0) {
                this.number = 0
            }
            this.totalPrice = this.number * this.good.price
        },
        submitOrder() {
            this.$submitOrder([{
                id: this.good.id,
                name: this.good.name,
                description: this.good.desc,
                figure: this.good.pics[0],
                pricePerOne: this.good.price,
                number: this.number,
                totalPrice: this.totalPrice 
            }])
        }
    }
}
</script>