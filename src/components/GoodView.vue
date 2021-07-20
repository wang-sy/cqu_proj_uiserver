<template>
    <a-card hoverable>
        <img
            slot="cover"
            alt="example"
            :src="figure"
        />
        <a-card-meta :title="name">
            <template slot="description">
                {{description}}
                <a-row>
                    <a-col :span="12" style="margin-top: 8px"><b>{{price}} ¥</b></a-col>
                    <a-col :span="12">
                        <a-button type="dashed" style="width: 100%">立刻购买</a-button>
                    </a-col>
                </a-row>
            </template>
        </a-card-meta>
    </a-card>
</template>

<script>
export default {
    props: {
        id: Number,
        name: String,
        description: String,
        figure: String,
        price: Number
    }
}

</script>

<style scoped>

</style>