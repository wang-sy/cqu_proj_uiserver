<template>
    <a-card title="购物车">
        <a-list item-layout="horizontal" :data-source="commoditys">
            <a-list-item 
                slot="renderItem" 
                slot-scope="item, index" 
                :style=" item.selected ? 
                'background-color: #f9f9f9f9' : ''"
            >
                <div style="width: 5%">
                    <a-checkbox v-model="item.selected" ></a-checkbox>
                </div>
                <div style="width: 65%">
                    <a-list-item-meta
                        :description="item.description"
                    >
                        <a 
                            slot="title" 
                            href="https://www.antdv.com/"
                            style="font-size: 1.5em"
                        >
                            {{ item.name }}
                        </a>
                        <img 
                            slot="avatar" 
                            :src="item.figure" 
                            style="width: 110px; height: 82px;"
                        />
                    </a-list-item-meta>
                </div>
                <div style="width: 30%">
                    <!-- price -->
                    <h3 style=""> 
                        单价：¥ {{ item.pricePerOne }}
                    </h3>
                    <!-- counter -->
                    <h3 style=""> 
                        数量：
                        <a-input 
                            style="width: 30%" 
                            v-model="item.number"
                            @change="changeNumber(item)"
                        />
                    </h3> 
                    <h3>
                        总价：¥ {{ item.totalPrice }}
                    </h3>
                </div>
                 <a-icon solt="extra" type="delete" @click="deleteItem(index)"/>
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

let commoditys = [
  {
    name: '七彩虹吉列威锋竞速3070显卡（吃鸡英雄联盟绝地求生）',
    description: "Fuck and Shit",
    href: "https://www.baidu.com",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
  },
  {
    name: 'Ant Design Title 1',
    description: "Fuck and Shit",
    href: "https://www.baidu.com",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
  },
  {
    name: 'Ant Design Title 1',
    description: "Fuck and Shit",
    href: "https://www.baidu.com",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
  },
  {
    name: 'Ant Design Title 1',
    description: "Fuck and Shit",
    figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
    pricePerOne: 47.5,
    number: 10,
    selected: true,
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
            console.log(item.totalPrice)
        },
        deleteItem(index) {
            this.commoditys.splice(index,1)
        },
        updateSelected(item) {
            console.log(item)
            item.selected = !item.selected
        },
        submit() {
            console.log(this.commoditys)
        }
    },
    // get prices.
    beforeMount() {
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
