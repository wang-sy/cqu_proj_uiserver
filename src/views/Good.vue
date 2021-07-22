<template>
    <main>
        <!-- base info for good -->
        <a-card :bordered="false">
            <a-row flex>
                <!-- figure -->
                <a-col :span="10"><a-card style="width: 100%">
                    <a-carousel autoplay arrows>
                        <div v-for="(item, index) in good.pics" :key="index">
                            <img style="width: 100%" :src="item"/>
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
                        <a-row>
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
        getGoodByID: async (id) => {
            return {    
                id: 123,
                name: "吉列威锋电竞I11超级嬉皮优",
                desc: "女生自用，九成新，真的特别新，新的我快不行了，快，大哥来买了这张卡吧。这张卡我用的时候特别宝贵，他就像我爹一样，我对他特别好，求求你们买了吧。",
                type: "cpu",
                price: 2333,
                pics: [
                    "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/cpu.jpg",
                    "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/ssd.jpg"
                ],
                params: {
                    "基本参数":{
                        "适用类型":"台式机",
                        "CPU系列":"Ryzen 3",
                        "制作工艺":"12纳米",
                        "CPU架构":"Zen+",
                        "插槽类型":"Socket AM4",
                        "包装形式":"盒装"
                    },
                    "性能参数":{
                        "CPU主频":"3.6GHz",
                        "动态加速频率":"4GHz",
                        "核心数量":"四核心",
                        "线程数量":"四线程",
                        "热设计功耗(TDP)":"65W"
                    },
                    "内存参数":{
                        "内存类型":"DDR4 2933MHz"
                    },
                    "显卡参数":{
                        "集成显卡":"Radeon Vega 8 Processor Graphics"
                    }
                }
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