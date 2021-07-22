<template>
    <main>
        <a-row :gutter="[10,20]">
            <a-col v-for="(item, index) in goods" :key="index" :span="6">
                <GoodView
                    :id="item.id"
                    :name="item.name"
                    :description="item.description"
                    :figure="item.figure"
                    :price="item.price"
                    @click="toGoodPage(item.id)"
                />
            </a-col>
        </a-row>
    </main>
</template>

<script>
import GoodView from '../components/GoodView'

let goods =[
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 0,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 1,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 2,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 3,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 0,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 1,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 2,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 3,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 0,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 1,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 2,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 3,
    }
]

let search = [
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 1,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 2,
    },
    {
        name: '七彩虹3070显卡',
        description: "绝地求生、英雄联盟，高画质高帧率畅玩",
        figure: "https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/8B53F293163383A5FBBDEAFC9EFED387.jpg",
        price: 47.5,
        id: 3,
    }
]

export default {
    components: {
        GoodView
    },
    data() {
        return {
            goods: []
        }
    },
    mounted() {
        let _this = this
        let catgory = this.$route.query.catgory
        let search_result = this.$route.query.searchid
        if(search_result) {
            this.searchGoodsList(search_result)
                .then((data) => {
                    _this.goods = data
                })
        }
        else{
            this.getGoodsList(catgory)
                .then((data) => {
                    _this.goods = data
                })
        }
    },
    methods: {
        getGoodsList: async (id) =>{
            return goods
        },
        searchGoodsList: async (id) =>{
            return search
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
