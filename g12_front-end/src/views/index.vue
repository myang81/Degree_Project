<template>
    <div>
        <el-container>
            <el-header>Header</el-header>
            <el-main>Main</el-main>
            <el-footer>Footer</el-footer>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "index",
        props: {
            msg: String
        },
    }
</script>

<style scoped>

</style>
