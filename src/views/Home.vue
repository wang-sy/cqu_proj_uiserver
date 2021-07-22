<template>
    <main>
        <!-- 走马灯 -->
        <a-carousel autoplay class="Carousel">
            <div v-for="(item, index) in top10Goods" :key="index">
                <img style="width: 100%" :src="item.src" @click="toGoodPage(item.id)"/>
            </div>
        </a-carousel>

            <!-- 分类展示 -->

        <a-card :bordered="false" style="margin-top: 24px">
            <div v-for="(item, index) in categories" :key="index" class="CategoryViewItem">
                <CategoryView 
                    :title="item.name" 
                    :categoryID="item.id" 
                    :goods="item.goods"
                />
            </div>
        </a-card>
    </main>
</template>

<script>

import CategoryView from '../components/CategoryView'

let categoryDatas = {
    name: "家用电器",
    id: 0,
    goods: [
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
    ],
}

export default {
    components: {
        CategoryView
    },
    data() {
        return {
            top10Goods: [
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/cqu/AMD RADEON RX6000_v1.png', // img Src
                    id: 0 // goodID
                },
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/cqu/ROG Strix 850W_v1.png',
                    id: 1
                },
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/cqu/ROG case_v1.png',
                    id: 2
                },
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/cqu/X570_v1.png',
                    id: 3
                },
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/cqu/Z590_v1.png',
                    id: 4
                }
            ],
            categories: [
                categoryDatas,
                categoryDatas
            ],
        }
    },
    methods: {
        toGoodPage(goodID) {
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

<style scoped>

.Carousel{
    width: 94%;
    left: 3%;
    position: relative;
}

.CategoryViewItem{
    margin-bottom: 24px;
}



</style>
