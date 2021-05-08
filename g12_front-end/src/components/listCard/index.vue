<template>
    <div>
        <el-card class="list-block desktop_card" v-for="(item,index) in houseList" :key="index+'pc'" shadow="hover">
          <div   @mouseenter="mouseover(index)" @mouseleave="mouseLeave(index)">
            <el-row class="house-item">
              <el-col :span=8 style="height: 100%;position: relative">
                <el-image class="item-img" :src=item.imgUrl fit="cover"></el-image>
                <div class="item-collection item-little" @click="handleCollect(index,item.collected)">
                  <i href="#" class="contain-icon icon-hook" :class="{'active':item.collected==='true'}">
                    <!--Begin Second Star Icon-->
                    <svg class="star-icon star-icon-2" version="1.1"
                         viewBox="0 0 105.602 102.931" style="width: 25px;height: 25px">
                      <path class="main-star-2" fill="none" stroke="#ffffff" stroke-width="6" stroke-miterlimit="10" d="M52.35,3.11c0.475-0.963,1.253-0.963,1.728,0 l12.211,24.742c0.475,0.963,1.734,1.877,2.796,2.032l27.305,3.968c1.063,0.154,1.303,0.894,0.534,1.644L77.167,54.754
          c-0.769,0.75-1.25,2.229-1.068,3.287l4.664,27.194c0.182,1.058-0.448,1.516-1.398,1.016L54.942,73.413
          c-0.951-0.5-2.506-0.5-3.456,0L27.064,86.252c-0.951,0.5-1.58,0.043-1.398-1.016l4.664-27.194c0.182-1.058-0.299-2.538-1.068-3.287
          L9.504,35.495c-0.769-0.75-0.529-1.489,0.534-1.644l27.305-3.968c1.063-0.154,2.321-1.069,2.796-2.032L52.35,3.11z"/>
                      <path class="star-dashes-2" fill="#ffffff" stroke="#ffffff" stroke-width="5"
                            stroke-linecap="round" stroke-miterlimit="10" d="M20.881,6.26
          l6.333,7.333 M103.214,63.961l-9.173-3.122 M78.519,13.835l5.724-7.818 M52.777,100.544l0.048-9.69 M11.823,61.737l-9.436,2.204"/>
                      M42.681,47.839l6.817,6.817 M63.747,39.016l-14.249,15.64"/>
                    </svg>
                    <!--End Second Star Icon-->
                    <!--                    <span class="text save-text">Save for Later</span>-->
                  </i>
                </div>
              </el-col>
              <el-col :span=12>
                <div class="item-text">
                  <div class="item-name" @click="handleClickTitle(item.houseId)">{{ item.title }}
                  </div>
                  <div class="item-pos item-little"><i class="el-icon-position"> </i>{{
                      item.position
                    }}
                  </div>
                  <div class="item-details item-little"><i class="el-icon-s-home"> </i>{{
                      item.describe
                    }}
                  </div>
                  <!--                  <div class="item-collection item-little"><i class="el-icon-star-off"> </i>{{ item.collection }}</div>-->
                </div>
              </el-col>
              <el-col :span=4 style="height: 100%">
                <div class="item-price">{{ item.totalPrice }}<span style="color: red;padding-left: 5px">million</span>
                </div>
              </el-col>
            </el-row>
          </div>
          <div v-if="item.sold==='TRUE'" class="sold-cover"></div>
<!--            <div class="sold-cover"></div>-->
        </el-card>
        <el-card class="list-block mobile_card" v-for="(item,index) in houseList" :key="index+'mobile'" shadow="hover" @mouseenter="mouseover(index)" @mouseleave="mouseLeave(index)">
            <el-row class="house-item">
                    <el-image class="item-img" :src=item.imgUrl fit="cover"></el-image>
                    <div class="item-collection item-little" @click="handleCollect(index,item.collected)">
                        <i href="#" class="contain-icon icon-hook" :class="{'active':item.collected==='true'}">
                            <!--Begin Second Star Icon-->
                            <svg class="star-icon star-icon-2" version="1.1"
                                 viewBox="0 0 105.602 102.931" style="width: 25px;height: 25px">
                                <path class="main-star-2" fill="none" stroke="#ffffff" stroke-width="6" stroke-miterlimit="10" d="M52.35,3.11c0.475-0.963,1.253-0.963,1.728,0 l12.211,24.742c0.475,0.963,1.734,1.877,2.796,2.032l27.305,3.968c1.063,0.154,1.303,0.894,0.534,1.644L77.167,54.754
          c-0.769,0.75-1.25,2.229-1.068,3.287l4.664,27.194c0.182,1.058-0.448,1.516-1.398,1.016L54.942,73.413
          c-0.951-0.5-2.506-0.5-3.456,0L27.064,86.252c-0.951,0.5-1.58,0.043-1.398-1.016l4.664-27.194c0.182-1.058-0.299-2.538-1.068-3.287
          L9.504,35.495c-0.769-0.75-0.529-1.489,0.534-1.644l27.305-3.968c1.063-0.154,2.321-1.069,2.796-2.032L52.35,3.11z"/>
                                <path class="star-dashes-2" fill="#ffffff" stroke="#ffffff" stroke-width="5"
                                      stroke-linecap="round" stroke-miterlimit="10" d="M20.881,6.26
          l6.333,7.333 M103.214,63.961l-9.173-3.122 M78.519,13.835l5.724-7.818 M52.777,100.544l0.048-9.69 M11.823,61.737l-9.436,2.204"/>
                                M42.681,47.839l6.817,6.817 M63.747,39.016l-14.249,15.64"/>
                            </svg>
                            <!--End Second Star Icon-->
                            <!--                    <span class="text save-text">Save for Later</span>-->
                        </i>
                    </div>
                    <div class="item-text">
                        <div class="item-name" @click="handleClickTitle(item.houseId)">{{ item.title }}
                        </div>
                        <div class="item-pos item-little"><i class="el-icon-position"> </i>{{
                            item.position
                            }}
                        </div>
                        <div class="item-details item-little"><i class="el-icon-s-home"> </i>{{
                            item.describe
                            }}
                        </div>
                        <!--                  <div class="item-collection item-little"><i class="el-icon-star-off"> </i>{{ item.collection }}</div>-->
                    </div>
                    <div class="item-price">{{ item.totalPrice }}<span style="color: red;padding-left: 5px">million</span>
                    </div>
            </el-row>
                    <div v-if="item.sold==='TRUE'" class="sold-cover"></div>
<!--          <div class="sold-cover"></div>-->
        </el-card>
    </div>
</template>

<script>
    import {addCollection} from '@/utils/api'
    export default {
        name: "index",
        props:{
            houseList:{type:Array}
        },
        data(){
            return {
            }
        },
        methods:{
          mouseover(index){
            console.log("mouseover")
            this.$emit('mouseover',index)
          },
          mouseLeave(index){
            console.log("mouseLeave")
            this.$emit('mouseLeave',index)
          },
            handleClickTitle(houseId) {
                this.$router.push({name: 'detail', query: {houseId: houseId}})
            },
            handleCollect(index,collected){
              let message;
              if(collected==='true'){
                collected='false'
                message="cancel success"
              }else{
                collected='true'
                message="collect success"
              }
              console.log(this.houseList)
                addCollection({houseId:this.houseList[index].houseId,userId:this.$store.state.userId,collected:collected}).then(()=>{
                  this.$message({
                    message: message,
                    type: 'success'
                  });
                    this.houseList[index].collected=collected
                })
            },
        }
    }
</script>

<style scoped>
    .contain-icon{
        cursor: pointer;
    }
    @media (min-width: 576px) {
        .desktop_card{
            display: block;
        }
        .mobile_card{
            display: none;
        }
        .house-item {
            padding: 20px;
            /*border-bottom: 2px solid black;*/
            height: 260px;
        }

        .house-item .item-text {
            text-align: left;
            margin-left: 20px;
        }

        .house-item .item-name {
            font-weight: bold;
            font-size: 1.6rem;
            padding: 10px 0;

            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            transition: color .2s;
            cursor: pointer;
        }

        .house-item .item-name:hover {
            color: #409EFF;
        }

        .house-item .item-pos {
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .house-item .item-details {

            display: -webkit-box;
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 3;
            overflow: hidden;
        }
        .house-item .item-little {
            line-height: 35px;
        }
        .house-item .item-price {
            font-weight: bold;
            font-size: 1.6rem;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .house-item .item-img {
            height: 100%;
            width: 100%;
            border-radius: 15px;
        }
        .house-item .item-collection{
            top: 10px;
            right: 10px;
            position: absolute;
        }
    }

    @media (max-width: 576px) {

        .house-item {
            height: auto;
            display: flex;
            flex-direction: column;
        }

        .house-item .item-text {
            text-align: left;
        }

        .house-item .item-name {
            font-weight: bold;
            font-size: 1.0rem;
            padding-top: 5px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            transition: color .2s;
            cursor: pointer;
        }

        .house-item .item-name:hover {
            color: #409EFF;
        }

        .house-item .item-pos {
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            color: rgba(0,0,0,0.6);
            font-size: 0.8rem;
        }

        .house-item .item-details {
            -webkit-box-orient: vertical;
            -webkit-line-clamp: 3;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            color: rgba(0,0,0,0.6);
            font-size: 0.8rem;
        }

        .house-item .item-price {
            font-weight: bold;
            font-size: 1.2rem;
            text-align: left;
        }
        .house-item .item-img {
            height: 25vh;
            width: 100%;
            border-radius: 15px;
            overflow: initial;
        }
        .house-item .item-collection{
            top: 10px;
            right: 10px;
            position: absolute;
        }
        .desktop_card{
            display: none;
        }
        .mobile_card{
            display: block;
        }
    }




    .list-block {
        margin: 10px;
      position: relative;
    }
</style>
