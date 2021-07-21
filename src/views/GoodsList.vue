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

export default {
    components: {
        GoodView
    },
    data() {
        return {
            goods: goods
        }
    }
}
</script>
