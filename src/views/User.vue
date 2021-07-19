<template>
    <main>
        <a-card title="个人信息" class="card_item"> 
            <PersonInfo></PersonInfo>
        </a-card>
        <a-card title="订单列表" class="card_item"> 
            TODO(zhaoyingkai): 实现订单组件.
        </a-card>
        <ShoppingCart class="card_item"></ShoppingCart>
    </main>
</template>


<script>

import ShoppingCart from "../components/ShoppingCart"
import PersonInfo from "../components/PersonInfo"

export default {
    components: {
        ShoppingCart,
        PersonInfo
    }
}

</script>

<style scoped>

.card_item {
    margin-bottom: 2vh;
}

</style>