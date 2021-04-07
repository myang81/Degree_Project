<template>
    <div class="sidebar-basic">
        <div class="sidebar-icon" :class="{'sidebarOpen':isCollapse,'sidebarClose':!isCollapse}" @click="handleSwitch"></div>
        <el-menu default-active="1-2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-user-solid"></i>
                    <span slot="title">Profile</span>
                </template>
                <el-menu-item-group>
                  <router-link to="/center/userDetail">
                    <el-menu-item index="1-1">
                      <router-link to="detail">Detail</router-link>
                    </el-menu-item>
                  </router-link>
                  <router-link to="/center/target">
                    <el-menu-item index="1-2">
                      Target
                    </el-menu-item>
                  </router-link>
                </el-menu-item-group>
            </el-submenu>
          <router-link to="/center/collection">
            <el-menu-item index="2">
                <i class="el-icon-star-on"></i>
                <span slot="title">Collection</span>
            </el-menu-item>
          </router-link>
          <router-link to="/center/published">
          <el-menu-item index="3">
                <i class="el-icon-s-help"></i>
                <span slot="title">Published</span>
            </el-menu-item>
          </router-link>
          <router-link to="/center/sale">
          <el-menu-item index="4">
                <i class="el-icon-s-goods"></i>
                <span slot="title">Sale</span>
            </el-menu-item>
          </router-link>
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
        from {transform: rotate(180deg);margin-left: 110px;
        }
        to {transform: rotate(0);margin-left: 15px;}
    }
    @keyframes sidebarClose
    {
        from {transform: rotate(0);margin-left: 15px;}
        to {transform: rotate(-180deg);margin-left: 110px;}
    }
    a{
      color: initial;
    }
</style>
<style>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 160px;
        min-height: 400px;
    }
    .el-menu-item.is-active a{
      color: #409EFF !important;
    }
    .el-submenu .el-menu-item {
      min-width: auto!important;
    }
</style>
