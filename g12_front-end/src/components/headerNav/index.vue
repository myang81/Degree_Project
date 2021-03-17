<template>
    <div class="home-header-nav">
        <div class="block_logo"></div>
        <div class="block_nav">
            <el-menu
                    mode="horizontal"
                    @select="handleSelect"
                    background-color="#545c64"
                    text-color="#fff"
                    active-text-color="#ffd04b">
                <el-menu-item index="1" class="nav_choice">Renting</el-menu-item>
                <el-menu-item index="2" class="nav_choice">Purchase</el-menu-item>
                <el-menu-item index="3" class="nav_choice">guide</el-menu-item>
                <el-menu-item index="4" class="nav_choice">Publishing</el-menu-item>
            </el-menu>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index"
    }
</script>

<style scoped>
    .home-header-nav{
        width: 100%;
        height: 60px;
    }
    .block_nav{
        display: flex;
        flex-direction: row-reverse;
        background: rgba(84, 92, 100, 0.5);
    }
    .nav_choice{
        background: rgba(84, 92, 100, 0.5);
    }
</style>
