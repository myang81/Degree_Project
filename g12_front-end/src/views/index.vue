<template>
    <div>
        <div class="home-header">
            <HeaderNav :navContent="navContent"></HeaderNav>
            <div class="home-header-content">
                <P class="p-header-content">Find your house</P>
                <el-input
                    placeholder="Please input the house name, location, house type and other characteristics"
                    suffix-icon=""
                    v-model="searchValue"
                    class="input_search"
                >
                  <el-button slot="append" icon="el-icon-search" size="small" @click="handleSearch"></el-button>
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
import {getExample} from '@/utils/api'
import HeaderNav from '@/components/headerNav/index.vue'

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
              recommendationList:[{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"}],
              // animationTime:0,
              navContent:[{name:'Login',router:'/login'},{name:'Register',router:'/register'}]
            }
        },
        created() {
            // setInterval(()=>{
            //     this.animationTime++;
            //     if(this.animationTime>15){
            //         this.animationTime=this.animationTime%15
            //     }
            // },1000)
            this.getTestData()
        },
      methods:{
        handleSearch(){
          this.$router.push({name:'houseList', params: { q: this.searchValue }})
        },
          getTestData(){
              getExample().then(res=>{
                console.log('调用接口成功',res)
            })
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
        animation: infinite forwards indexImg linear 15s;
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

    @media (min-width: 992px){
        .home-header-content .input_search{
            width: 60%;
            margin: 12vh auto 0 auto;
        }
        .home-header-content .p-header-content{
            text-align: center;
            color: white;
            font-size: 4rem;
            font-family: herculanum,fantasy;
        }
    }
    @media (max-width: 992px){
        .home-header-content .input_search{
            width: 90%;
            margin: 12vh auto 0 auto;
        }
        .home-header-content .p-header-content{
            text-align: center;
            color: white;
            font-size: 2.0em;
            font-family: herculanum,fantasy;
        }
    }
    .home-header-content .p-header-content{
        text-align: center;
        margin: 20vh auto 0 auto;
        color: white;
        font-family: herculanum,fantasy;
        padding: 0 15px;
        animation:  infinite forwards cyberLight linear 15s;
        box-sizing:border-box;
    }
    @keyframes cyberLight{

        0% {border: solid 10px transparent;box-shadow: 0 0 0;}
        8.33% {border: solid 10px transparent;box-shadow: 0 0 0;}
        24.99% {border: solid 10px transparent;box-shadow: 0 0 0;}
        33.32% {border: solid 10px transparent;box-shadow: 0 0 0;}
        41.65% {border: solid 10px rgba(255,0,0,.5);border-radius: 10px;box-shadow: 0 0 90px rgba(255,0,0,.8);}
        49.98% {border: solid 10px #fff;border-radius: 10px;box-shadow: 0 0 70px rgb(190,40,210);}
        58.31% {border: solid 10px rgba(255,0,0,.5);border-radius: 10px;box-shadow: 0 0 90px rgba(255,0,0,.8);}
        66.64% {border: solid 10px #fff;border-radius: 10px;box-shadow: 0 0 70px rgb(190,40,210);}
        74.97% {border: solid 10px transparent;box-shadow: 0 0 0;}
        91.63% {border: solid 10px transparent;box-shadow: 0 0 0;}
        100% {border: solid 10px transparent;box-shadow: 0 0 0;}
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
        8.33% {background-position: 25%;background-image: url("../assets/banner.jpg");opacity:1}
        24.99% {background-position: 75%;background-image: url("../assets/banner.jpg");opacity:1}
        33.32% {background-position: 100%;background-image: url("../assets/banner.jpg");opacity:0}
        33.321% {background-position: 0;background-image: url("../assets/cyber.jpg");opacity:0;}
        41.65% {background-position: 25%;background-image: url("../assets/cyber.jpg");opacity:1}
        58.31% {background-position: 75%;background-image: url("../assets/cyber.jpg");opacity:1}
        66.64% {background-position: 100%;background-image: url("../assets/cyber.jpg");opacity:0}
        66.641% {background-position: 0;background-image: url("../assets/Chinese.jpg");opacity:0;}
        74.97% {background-position: 25%;background-image: url("../assets/Chinese.jpg");opacity:1}
        91.63% {background-position: 75%;background-image: url("../assets/Chinese.jpg");opacity:1}
        100% {background-position: 100%;background-image: url("../assets/Chinese.jpg");opacity:0}
    }

    .p-header-content,.p-header-content::after{
        margin-right: 5px;
        /*height: 25px;*/
        /*line-height: 25px;*/
        letter-spacing: 2px;
        color: white;
        position: relative;
        /*border: solid 10px #fff;*/
        /*box-shadow: 0 0 70px rgb(190,40,210);*/
        padding: 0 auto;
        width: fit-content;
    }
    .p-header-content:first-of-type::after{
        --slice-0: inset(50% 50% 50% 50%);
        --slice-1: inset(80% -6px 0 0);
        --slice-2: inset(50% -6px 45% 0);
        --slice-3: inset(10% -6px 60% 0);
        --slice-4: inset(40% -6px 50% 0);
        --slice-5: inset(75% -6px 5% 0);
        display: block;
        content: "Find your house";
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
        animation: glitch 15s infinite;
        animation-timing-function: steps(1, end);
    }
    @keyframes glitch  {
        48.749% { opacity: 0}
        48.75% {            clip-path: var(--slice-1);
            transform: translate(-10px, -10px); opacity: 1}
        49.5% {            clip-path: var(--slice-2);
            transform: translate(5px, 0px);}
        50.25% {            clip-path: var(--slice-1);
            transform: translate(-5px, 0px);}
        51% {            clip-path: var(--slice-4);
            transform: translate(0px, 5px);}
        51.75% {            clip-path: var(--slice-2);
            transform: translate(-2px, 0px);}
        52.5% {            clip-path: var(--slice-3);
            transform: translate(2px, 0px);}
        53.25% {            clip-path: var(--slice-4);
            transform: translate(2px, 5px);}
        54% {            clip-path: var(--slice-2);
            transform: translate(-5px, 5px);}
        54.75% {            clip-path: var(--slice-5);
            transform: translate(10px, -10px);}
        55.5% {            clip-path: var(--slice-1);
            transform: translate(-5px, 0px);}
        56.25% {            clip-path: var(--slice-3);
            transform: translate(0px, 5px) ;opacity: 1}
        56.251% { opacity: 0}
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
    .input_search .el-input-group__append, .el-input-group__prepend {
      background-color: rgba(255,255,255,0.9);
    }
</style>
