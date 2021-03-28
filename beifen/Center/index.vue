<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="js/vue.js" type="text/javascript"></script>
</head>








<template>
    <div>
        <HeaderNav></HeaderNav>
        <div>
            <Sidebar></Sidebar>
            <div class="center-main">
                <P class="center-title" type="danger" icon="el-icon-delete">Your collection</P>
                <el-form ref="form" :model="form" label-width="80px">
                   <div class="divcss5" id="demo" v-on:mouseenter="show = true" v-on:mouseleave="show=false">
                    <el-form-item>
                        <el-col :span="10">
                        <div class="left">





<!--                          <div><img src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" width="268px" height="168px"></div>-->
                          <div class="recommendation-carousel">
                <el-carousel :interval="0" type="card" height="170px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >

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
                          <div style="margin-left:5px;margin-top: 1px;font-size: 20px;FONT-FAMILY: STKaiti">{{xiaoqumingzi}}</div>
                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="right" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>
                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="rright" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>
                        </div>
                        </el-col>



                      <el-col :span="2">
                        <div class="child" style="margin-top: 60px;">
<!--                       <button v-if="show">Toggle</button>-->
                          <el-button type="danger" icon="el-icon-delete" circle v-if="show"   style="width:150px;	height:150px;" ></el-button>
                          </div>
                        </el-col>

                      <el-col :span="16">
                        <div class="child">
                          </div>
                        </el-col>

                    </el-form-item>
                     </div>


                    <el-divider></el-divider><div class="divcss5" id="demo" v-on:mouseenter="show1 = true" v-on:mouseleave="show1=false">
                    <el-form-item>
                        <el-col :span="10">
                        <div class="left">





<!--                          <div><img src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" width="268px" height="168px"></div>-->
                          <div class="recommendation-carousel">
                <el-carousel :interval="0" type="card" height="170px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >

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
                          <div style="margin-left:5px;margin-top: 1px;font-size: 20px;FONT-FAMILY: STKaiti">{{xiaoqumingzi}}</div>
                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="right" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>


                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="rright" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>
                        </div>
                        </el-col>



                      <el-col :span="2">
                        <div class="child" style="margin-top: 60px;">
<!--                       <button v-if="show">Toggle</button>-->
                          <el-button type="danger" icon="el-icon-delete" circle v-if="show1"   style="width:150px;	height:150px;" ></el-button>
                          </div>
                        </el-col>

                      <el-col :span="16">
                        <div class="child">
                          </div>
                        </el-col>

                    </el-form-item>
                     </div>
                    <el-divider></el-divider>
                    <div class="divcss5" id="demo" v-on:mouseenter="show3 = true" v-on:mouseleave="show3=false">
                    <el-form-item>
                        <el-col :span="10">
                        <div class="left">





<!--                          <div><img src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" width="268px" height="168px"></div>-->
                          <div class="recommendation-carousel">
                <el-carousel :interval="0" type="card" height="170px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >

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
                          <div style="margin-left:5px;margin-top: 1px;font-size: 20px;FONT-FAMILY: STKaiti">{{xiaoqumingzi}}</div>
                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="right" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>


                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="rright" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>
                        </div>
                        </el-col>



                      <el-col :span="2">
                        <div class="child" style="margin-top: 60px;">
<!--                       <button v-if="show">Toggle</button>-->
                          <el-button type="danger" icon="el-icon-delete" circle v-if="show3"   style="width:150px;	height:150px;" ></el-button>
                          </div>
                        </el-col>

                      <el-col :span="16">
                        <div class="child">
                          </div>
                        </el-col>

                    </el-form-item>
                     </div>
                    <el-divider></el-divider>
                    <div class="divcss5" id="demo" v-on:mouseenter="show4 = true" v-on:mouseleave="show4=false">
                    <el-form-item>
                        <el-col :span="10">
                        <div class="left">





<!--                          <div><img src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" width="268px" height="168px"></div>-->
                          <div class="recommendation-carousel">
                <el-carousel :interval="0" type="card" height="170px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >

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
                          <div style="margin-left:5px;margin-top: 1px;font-size: 20px;FONT-FAMILY: STKaiti">{{xiaoqumingzi}}</div>
                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="right" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>


                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="rright" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>
                        </div>
                        </el-col>



                      <el-col :span="2">
                        <div class="child" style="margin-top: 60px;">
<!--                       <button v-if="show">Toggle</button>-->
                          <el-button type="danger" icon="el-icon-delete" circle v-if="show4"   style="width:150px;	height:150px;" ></el-button>
                          </div>
                        </el-col>

                      <el-col :span="16">
                        <div class="child">
                          </div>
                        </el-col>

                    </el-form-item>
                     </div>
                             <el-divider></el-divider>
                    <div class="divcss5" id="demo2" v-on:mouseenter="show5 = true" v-on:mouseleave="show5=false">
                    <el-form-item>
                        <el-col :span="10">
                        <div class="left">





<!--                          <div><img src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg" width="268px" height="168px"></div>-->
                          <div class="recommendation-carousel">
                <el-carousel :interval="0" type="card" height="170px">
                    <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >

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
                          <div style="margin-left:5px;margin-top: 1px;font-size: 20px;FONT-FAMILY: STKaiti">{{xiaoqumingzi}}</div>
                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="right" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>


                        </div>
                        </el-col>
                      <el-col :span="5">
                        <div class="rright" style="font-size: 20px;">
                        <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{mianji}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{huxing}}</div>
                          <div style="margin-left:5px;margin-top: 20px;font-size: 20px;FONT-FAMILY: STKaiti;">{{chaoxiang}}</div>
                        </div>
                        </el-col>



                      <el-col :span="2">
                        <div class="child" style="margin-top: 60px;">
<!--                       <button v-if="show">Toggle</button>-->
                          <el-button type="danger" icon="el-icon-delete" circle v-if="show5"   style="width:150px;	height:150px;" ></el-button>
                          </div>
                        </el-col>

                      <el-col :span="16">
                        <div class="child">
                          </div>
                        </el-col>

                    </el-form-item>
                     </div>
                    <el-divider></el-divider>

                    <el-form-item  style="text-align: right">
                        <el-button type="primary" @click="onSubmit" size="medium">S a v e</el-button>
<!--                        <el-button>取消</el-button>-->
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>





</template>

<script>
    import Sidebar from '@/components/sidebar/index.vue'
    import HeaderNav from '@/components/headerNav/index.vue'






    export default {
        name: "center",
        el:'#demo',
        el2:'#demo2',
        components:{
            Sidebar,
            HeaderNav,

        },
        data(){

            return{
              currentDate: new Date(),
              recommendationList:[{name:"客厅",image:"../assets/home_header_bg.jpg"},{name:"卧室",image:"../assets/home_header_bg.jpg"},{name:"厨房",image:"../assets/home_header_bg.jpg"},{name:"卫生间",image:"../assets/home_header_bg.jpg"}],
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: '',

                },
                xiaoqumingzi:'陶然北岸',
                mianji:'面积：  120m',
                huxing:'户型：  两室一厅',
                chaoxiang:'朝向：  南北',
                show:false,
                show1:false,
                show5:false,
                show3:false,
                show4:false,

            }
        }
    }





</script>



<style scoped>


.divcss5{
  border:3px solid #AAAAAA;
  width:1500px;
	height:260px;
	transition:width 2s;
	-webkit-transition:width 2s; /* Safari */

}

.divcss5:hover
{
	width:2000px;
  -webkit-animation: mymove 5s infinite; /* Chrome, Safari, Opera */

}



.time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }




/*.child{*/
/*  visibility: hidden;*/
/*}*/

/*.divcss5:hover .child{*/
/*    display:block ;*/
/*    visibility:visible;*/
/*}*/


/* Chrome, Safari, Opera */
@-webkit-keyframes mymove {
    50% {background-color: #00FFFF;}
}

/* Standard syntax */
/*@keyframes mymove {*/
/*    50% {background-color: blue;}*/
/*}*/





    .center-main{
        height: 100%;
        width: calc(80% - 65px);
        margin: 0 10% 0 calc(10% + 65px);
    }
    .center-title{
        font-size: 2rem;
        padding: 30px;
        text-align: right;
        position: relative;
        overflow: hidden;
    }
    .center-title:after {
        content: "";
        display: block;
        position: absolute;
        bottom: 10%;
        left: 0;
        height: 5px;
        width: 200%;
        background-color: #caa;
        background-image: linear-gradient(to right, #cc7575, #ffd544 50%, #cc7575);
        animation:colorLine 1s alternate infinite;
    }



    .fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}







    .box {
		height: 80%;
		/*overflow-y: auto;*/
		display: flex;
		flex-direction: column;
	}
    .el-card{
		margin-bottom:20px;
	}


    @keyframes colorLine
    {
        from {left:-100%;}
        to {left: 0}
    }
</style>
