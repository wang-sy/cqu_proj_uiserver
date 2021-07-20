<template>
    <main>
        <!-- 走马灯 -->
        <a-carousel autoplay class="Carousel">
            <div v-for="(item, index) in top10Goods" :key="index">
                <img style="width: 100%" :src="item.src"/>
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
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/hbs.jpeg', // img Src
                    id: 0 // goodID
                },
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/nkx.jpeg',
                    id: 1
                },
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/python.jpeg',
                    id: 2
                },
                {
                    src: 'https://saiyuwang-blog.oss-cn-beijing.aliyuncs.com/k8s.jpeg',
                    id: 3
                }
            ],
            categories: [
                categoryDatas,
                categoryDatas
            ],
        }
    }
}

</script>

<style scoped>

.Carousel{
    width: 90%;
    position: relative;
    left: 5%;
}

.CategoryViewItem{
    margin-bottom: 24px;
}



</style>
