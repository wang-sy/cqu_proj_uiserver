<template>
    <main>
        <a-card title="个人信息" class="card_item"> 
            <PersonInfo></PersonInfo>
        </a-card>
        <OrderList class="card_item"></OrderList>
        <ShoppingCart class="card_item"></ShoppingCart>
    </main>
</template>


<script>
import OrderList from '../components/OrderList.vue'
import ShoppingCart from "../components/ShoppingCart"
import PersonInfo from "../components/PersonInfo"

export default {
    components: {
        ShoppingCart,
        PersonInfo,
        OrderList
    },
}

</script>

<style scoped>

.card_item {
    margin-bottom: 2vh;
}

</style>