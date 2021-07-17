<template>
    <main>
        <a-card title="个人信息" class="card_item"> 
            TODO(tangzhenlin): 实现个人信息组件.
        </a-card>
        <OrderList class="card_item"></OrderList>
        <ShoppingCart class="card_item"></ShoppingCart>
    </main>
</template>


<script>
import OrderList from '../components/OrderList.vue'
import ShoppingCart from "../components/ShoppingCart"

export default {
    components: {
        ShoppingCart,
        OrderList
    },
    data(){
        return {
            collapsed: false,
        }
    }
}

</script>

<style scoped>

.card_item {
    margin-bottom: 2vh;
}

</style>