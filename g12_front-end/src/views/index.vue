<template>
    <div>
        <div class="home-header">
            <HeaderNav></HeaderNav>
            <div class="home-header-content">
                <P class="p-header-content">Find your favorite house</P>
                <el-input
                    placeholder="Please input the house name, location, house type and other characteristics"
                    suffix-icon="el-icon-search"
                    v-model="searchValue"
                    class="input_search"
                >
                </el-input>
            </div>
        </div>
        <div class="home-main">
            <div class="recommendation-carousel">
                <p class="recommendation-title">Recommended housing</p>
                <el-carousel :interval="4000" type="card" height="300px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >
<!--                        <h3 class="medium" :style="{backgroundImage: item.image}">{{ item.name }}</h3>-->
                        <div  style="position: relative;width: 100%;height: 100%">
                            <el-image
                                    src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg"
                                    fit="cover"
                                    style="width: 100%;height: 100%"
                            >
                            </el-image>
                            <p style="position: absolute;left: 10px;bottom: 0px;font-size: 1.5rem;background: rgba(84, 92, 100, 0.5);width: 100%;text-align: left;padding-left: 5%;color: white">{{item.name}}</p>
                        </div>
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="recommendation-carousel">
                <p class="recommendation-title">latest housing</p>
                <el-carousel :interval="4000" type="card" height="300px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >
                        <!--                        <h3 class="medium" :style="{backgroundImage: item.image}">{{ item.name }}</h3>-->
                        <div  style="position: relative;width: 100%;height: 100%">
                            <el-image
                                    src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg"
                                    fit="cover"
                                    style="width: 100%;height: 100%"
                            >
                            </el-image>
                            <p style="position: absolute;left: 10px;bottom: 0px;font-size: 1.5rem;background: rgba(84, 92, 100, 0.5);width: 100%;text-align: left;padding-left: 5%;color: white">{{item.name}}</p>
                        </div>
                    </el-carousel-item>
                </el-carousel>
            </div>
        </div>
    </div>
</template>

<script>
    import HeaderNav from '@/components/headerNav_logout/index.vue'

    export default {
        name: "index",
        props: {
            msg: String,
        },
        components: {
            HeaderNav
        },
        data() {
            return {
                searchValue: "",
                activeIndex:0,
                recommendationList:[{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"}]
            }
        }
    }
</script>

<style scoped>
    .home-header{
        width: 100%;
        height: 100vh;
        /*background-image: url("https://s1.ljcdn.com/feroot/pc/asset/img/home/bannerV2.jpg");*/
        /*background-position: center;*/
        position: relative;
        z-index: 10;
    }
    .home-header::after{
        content: '';
        background-repeat:no-repeat;
        background-origin:content-box;
        animation: infinite forwards indexImg linear 10s;
        /*background-color: rgba(0,0,0,0.1);*/
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        z-index: -90;
        background-size: cover;

        /*background-image: url("https://s1.ljcdn.com/feroot/pc/asset/img/home/bannerV2.jpg");*/
        /*background-position: 0;*/
    }
    .home-header::before{
        content: '';
        background-color: rgba(0,0,0,0.3);
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        z-index: -100;
    }

    .home-header-nav{
        width: 100%;
        height: 50px;
    }
    .home-header-content{
        width: 100%;
        height: calc(100% - 50px);
    }
    .home-header-content .input_search{
        width: 60%;
        margin: 40px auto 0 auto;
    }
    .home-header-content .p-header-content{
        text-align: center;
        margin: 150px auto 0 auto;
        color: white;
        font-size: 2.5rem;
    }
    .block_nav{
        display: flex;
        flex-direction: row-reverse;
        background: rgba(84, 92, 100, 0.5);
    }
    .home-main{
        width: 100%;
        padding: 10px;
    }
    .recommendation-carousel{
        width: 100%;
        padding: 10px 0;
    }
    .recommendation-carousel .recommendation-title{
        font-size: 1.8rem;
        color: rgba(84, 92, 100,1);
        text-align: left;
        padding: 10px 10px 10px 2%;
    }
    @keyframes indexImg
    {
        0% {background-position: 0;background-image: url("../assets/banner.jpg");opacity:0;}
        12.5% {background-position: 25%;background-image: url("../assets/banner.jpg");opacity:1}
        37.5% {background-position: 75%;background-image: url("../assets/banner.jpg");opacity:1}
        50% {background-position: 100%;background-image: url("../assets/banner.jpg");opacity:0}
        50.1% {background-position: 0;background-image: url("../assets/cyber.jpg");opacity:0;}
        62.5% {background-position: 25%;background-image: url("../assets/cyber.jpg");opacity:1}
        87.5% {background-position: 75%;background-image: url("../assets/cyber.jpg");opacity:1}
        100% {background-position: 100%;background-image: url("../assets/cyber.jpg");opacity:0}
    }

    .p-header-content,.p-header-content::after{
        margin-right: 5px;
        /*width: 55px;*/
        height: 25px;
        line-height: 25px;
        letter-spacing: 2px;
        color: white;
        border: 0;
        position: relative;
        padding: 0 10px;
    }
    .p-header-content:first-of-type::after{
        --slice-0: inset(50% 50% 50% 50%);
        --slice-1: inset(80% -6px 0 0);
        --slice-2: inset(50% -6px 30% 0);
        --slice-3: inset(10% -6px 85% 0);
        --slice-4: inset(40% -6px 43% 0);
        --slice-5: inset(80% -6px 5% 0);
        display: block;
        content: "Find your favorite house";
        position: absolute;
        left: 0;
        top: 0;
        right: 0;
        bottom: 0;
        /*background: linear-gradient(45deg, transparent 3%, yellow 3%, #3A5FCD 6%);*/
        text-shadow: -2px -2px yellow, 2px 2px #FF0000 ,4px 4px #3A5FCD;
        clip-path: var(--slice-0);
    }
    .p-header-content:first-of-type::after{
        animation: glitch 2s infinite;
        animation-timing-function: steps(1, end);
        animation-delay: 2s;
    }
    @keyframes glitch {
        50% {
            clip-path: var(--slice-1);
            transform: translate(-10px, -10px);
        }

        55% {
            clip-path: var(--slice-3);
            transform: translate(5px, 0px);
        }

        60% {
            clip-path: var(--slice-1);
            transform: translate(-5px, 0px);
        }

        65% {
            clip-path: var(--slice-3);
            transform: translate(0px, 5px);
        }

        70% {
            clip-path: var(--slice-2);
            transform: translate(-2px, 0px);
        }

        75% {
            clip-path: var(--slice-3);
            transform: translate(2px, 0px);
        }

        80% {
            clip-path: var(--slice-4);
            transform: translate(2px, 5px);
        }

        85% {
            clip-path: var(--slice-2);
            transform: translate(-5px, 5px);
        }

        90% {
            clip-path: var(--slice-5);
            transform: translate(10px, -10px);
        }

        95% {
            clip-path: var(--slice-1);
            transform: translate(-5px, 0px);
        }

        100% {
            clip-path: var(--slice-1);
            transform: translate(0);
        }
    }

</style>
<style>
    .block_nav ul{
        background: transparent!important;
    }
    .block_nav li{
        background: transparent!important;
    }
    .input_search input{
        background-color: rgba(255,255,255,0.9);
    }
</style>
