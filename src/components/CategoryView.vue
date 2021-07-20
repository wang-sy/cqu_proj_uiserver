<template>
    <main>
        <b class="Title">{{title}}</b>
        <!-- todo(wangsaiyu): add this.$router.push(productList, categoryID=id) -->
        <a class="MoreButton">更多商品</a>
        <a-divider />
        <!-- good list -->
        <a-row :gutter="[32,32]">
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

export default {
    components: {
        GoodView
    },
    props: {
        title: String,
        categoryID: Number,
        goods: Array
    },
}

</script>


<style scoped>
.Title {
    font-size: 1.5em;
    float: left;
}

.MoreButton {
    font-size: 1em;
    float: right;
}

.GoodListItem {
    width: 18%;
    margin-right: 2%;
}

</style>