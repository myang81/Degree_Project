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
                navContent: [{name: 'Center', router: '/center'}, {name: 'Collection', router: '/center/collection'}, {name: 'Start to Sale', router: '/center/sale'}]
            }
        }
    }
</script>

<style scoped>
    .center-main{
        height: calc(100vh - 60px);
        width: calc(90% - 65px);
        margin: 0 10% 0 calc(5% + 65px);
    }
</style>
