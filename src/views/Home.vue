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
            <div v-for="(item, index) in categorieViews" :key="index" class="CategoryViewItem">
                <CategoryView
                    :title="item.name"
                    :categoryID="item.id"
                    :goods="item.goods"
                />
            </div>
        </a-card>
      <img src="../assets/footer.png" style="width: 50vw; left: 25vw; position: relative">
    </main>
</template>

<script>

import CategoryView from '../components/CategoryView'

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
            categorieViews: [],
            categories: [
                "vga",
                "memory",
                "motherboard",
                "cpu",
                "hard_drives",
                "case",
                "power"
            ],
            categoriesName: {
                "vga": "显卡",
                "memory": "内存",
                "motherboard": "主板",
                "cpu": "处理器",
                "hard_drives": "硬盘",
                "case": "机箱",
                "power": "电源"
            }
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
        },
        async getCategoryGoods(name) {
            let data = await this.$axios({
                method: 'GET',
                url: this.$base_url + `api/goods/getGoodsByTypes?type=${name}&pageStart=0&pageSize=4`
            })

            return {
                id: data.data.name,
                name: this.categoriesName[data.data.name],
                goods: data.data.goods
            }
        }
    },
    async mounted() {
        let categoryViews = []
        for( let i = 0; i < this.categories.length; i ++ ) {
            let categoryView = await this.getCategoryGoods(this.categories[i])
            categoryViews.push(categoryView)
        }

        this.categorieViews = categoryViews
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
