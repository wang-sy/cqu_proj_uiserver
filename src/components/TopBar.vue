<template>
    <main>
        <a-icon
            class="trigger"
            :type="collapsed ? 'menu-unfold' : 'menu-fold'"
            @click="changeMenu(collapsed)"
        />
    </main>
</template>

<script>

export default {
    model: {
        prop: 'collapsed',
        event: 'changeMenu'
    },
    props: {
        // close or not.
        collapsed: Boolean
    },
    methods: {
        changeMenu(collapsed) {
            this.$emit('changeMenu', !collapsed)
        }
    }
}

</script>

<style scoped>
.trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

.trigger:hover {
  color: #1890ff;
}

</style>