<template>
    <div>
      <HeaderNav :navContent="navContent"></HeaderNav>
        <div style="position: relative">
            <Sidebar></Sidebar>
            <div class="center-main">
              <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
    import Sidebar from '@/components/sidebar/index.vue'
    import HeaderNav from '@/components/headerNav/index.vue'

    export default {
        name: "center",
        components:{
            Sidebar,
            HeaderNav
        },
        data(){
            return{
              navContent:[{name:'Renting',router:''},{name:'Purchase',router:'/'},{name:'Purchase',router:'/'},{name:'Publishing',router:'/'}]
            }
        }
    }
</script>

<style scoped>
    .center-main{
        height: calc(100vh - 60px);
        width: calc(80% - 65px);
        margin: 0 10% 0 calc(10% + 65px);
    }
</style>
