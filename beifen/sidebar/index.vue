<template>
    <div class="sidebar-basic">
        <div class="sidebar-icon" :class="{'sidebarOpen':isCollapse,'sidebarClose':!isCollapse}" @click="handleSwitch"></div>
        <el-menu default-active="1-2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-s-custom"></i>
                    <span slot="title">Profile</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item index="1-1">Detail</el-menu-item>
                    <el-menu-item index="1-2">Target</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="2">
                <i class="el-icon-star-off"></i>
                <span slot="title">Collection</span>
            </el-menu-item>
            <el-menu-item index="3">
                <i class="el-icon-s-goods"></i>
                <span slot="title">Published</span>
            </el-menu-item>
            <el-menu-item index="4">
                <i class="el-icon-upload"></i>
                <span slot="title">Sale</span>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "index",
        data() {
            return {
                isCollapse: true
            };
        },
        methods: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            handleSwitch(){
                this.isCollapse=!this.isCollapse
            }
        }
    }
</script>

<style scoped>
    .sidebar-basic{
        height: 100%;
        position: fixed;
        left: 0;
        top: 0;
        background-color: white;
        text-align: left;
        z-index: 999;
        padding-top: 10px;
    }
    .sidebar-icon{
        height: 32px;
        width: 32px;
        background-image: url("../../assets/right-icon.png");
        margin-left: 15px;
    }
    .sidebarOpen{
        animation:sidebarOpen 0.5s forwards;
    }
    .sidebarClose{
        animation:sidebarClose 0.5s forwards;
    }
    @keyframes sidebarOpen
    {
        from {transform: rotate(180deg);margin-left: 150px;
        }
        to {transform: rotate(0);margin-left: 15px;}
    }
    @keyframes sidebarClose
    {
        from {transform: rotate(0);margin-left: 15px;}
        to {transform: rotate(-180deg);margin-left: 150px;}
    }
</style>
<style>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        min-height: 400px;
    }
</style>
