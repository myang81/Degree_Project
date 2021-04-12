<template>
  <div>
    <HeaderNav :navContent="navContent" show-search="true" :searchValue="searchValue"></HeaderNav>
    <div  style="padding: 0 10px">
      <div class="head-content">
        <div class="choice-button-group">

          <div class="choice-div">
            <el-button class="choice-button" @click="handleChoiceButton('date')">
              date
            </el-button>
            <el-card class="choice-card" :class="{'choice-card-show':choiceCardVisible.date}">
              <vc-date-picker v-model="choice.dateRange" :columns="$screens({ default: 1, lg: 2 })" is-range
                              style="border: 0"/>
              <div class="choice-card-bottom">
                <span class="cancel" @click="handleHideChoice">Cancel</span>
                <span class="confirm" @click="handleHideChoice">Confirm</span>
              </div>
            </el-card>
          </div>

          <div class="choice-div">
            <el-button class="choice-button" @click="handleChoiceButton('type')">
              type
            </el-button>
            <el-card class="choice-card" :class="{'choice-card-show':choiceCardVisible.type}">
              <div>
                <el-checkbox-group v-model="choice.houseType">
                  <el-checkbox v-for="item in houseType" :label="item.title" :key="item.value" size="medium">
                    {{ item.title }}
                  </el-checkbox>
                </el-checkbox-group>
              </div>
              <div class="choice-card-bottom">
                <span class="cancel" @click="handleHideChoice">Cancel</span>
                <span class="confirm" @click="handleHideChoice">Confirm</span>
              </div>
            </el-card>
          </div>

          <div class="choice-div">
            <el-button class="choice-button" @click="handleChoiceButton('price')">
              price
            </el-button>
            <el-card class="choice-card" :class="{'choice-card-show':choiceCardVisible.price}">
              <div style="width: 500px;padding: 0 20px">
                <el-slider
                    v-model="choice.price"
                    range
                    :max="50000">
                </el-slider>
                <div style="display: flex;align-items: center;margin-bottom: 20px">
                  <el-input v-model="choice.price[0]" style="flex: 2" type="text"></el-input>
                  <span style="flex: 1">-</span>
                  <el-input v-model="choice.price[1]" style="flex: 2" type="text"></el-input>
                </div>
              </div>
              <div class="choice-card-bottom">
                <span class="cancel" @click="handleHideChoice">Cancel</span>
                <span class="confirm" @click="handleHideChoice">Confirm</span>
              </div>
            </el-card>
          </div>

          <div class="choice-div">
            <el-button class="choice-button" @click="handleMoreButton()">
              more
            </el-button>
          </div>

<!--          地图展示选项按钮，有问题，先关了-->
<!--          <div class="switch-div">
            <span style="margin-right: 20px">map switch</span>
            <el-switch
                @change="handleMapSwitch"
                v-model="mapShow"
                >
            </el-switch>
          </div>-->

          <div style="clear: both"></div>
        </div>
        <el-card class="check-block"
                 :class="{'check-block_show':choiceCardVisible.more&&!choiceCardVisible.init,'check-block_hide':!choiceCardVisible.more&&!choiceCardVisible.init}">
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="price">
              <el-checkbox-group v-model="form.type">
                <el-col :span="6">
                  <el-checkbox label="Less than 2 million" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="2-3.5 million" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="3.5-4.5 million" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="more than 4.5 million" name="type"></el-checkbox>
                </el-col>
              </el-checkbox-group>
            </el-form-item>

            <el-form-item label="layout">
              <el-checkbox-group v-model="form.type">
                <el-col :span="6">
                  <el-checkbox label="One room" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="Two room" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="Three room" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="Four rooms and above" name="type"></el-checkbox>
                </el-col>
              </el-checkbox-group>
            </el-form-item>

            <el-form-item label="measure">
              <el-checkbox-group v-model="form.type">
                <el-col :span="6">
                  <el-checkbox label="Less than 50 square meters" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="50-90 square meters" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="90-150 square meters" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="more than 150 square meters" name="type"></el-checkbox>
                </el-col>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item label="orientation">
              <el-checkbox-group v-model="form.type">
                <el-col :span="6">
                  <el-checkbox label="North South orientation" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="East west orientation" name="type"></el-checkbox>
                </el-col>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item label="floor">
              <el-checkbox-group v-model="form.type">
                <el-col :span="6">
                  <el-checkbox label="low" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="middle" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="high" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="top" name="type"></el-checkbox>
                </el-col>
              </el-checkbox-group>
            </el-form-item>

            <el-form-item label="decoration">
              <el-checkbox-group v-model="form.type">
                <el-col :span="6">
                  <el-checkbox label="Simple" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="Normal" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="high" name="type"></el-checkbox>
                </el-col>
                <el-col :span="6">
                  <el-checkbox label="luxury" name="type"></el-checkbox>
                </el-col>
              </el-checkbox-group>
            </el-form-item>
            <!--<el-form-item  style="text-align: right">
                <el-button type="primary" @click="onSubmit" size="medium">S a v e</el-button>
                &lt;!&ndash;                        <el-button>取消</el-button>&ndash;&gt;
            </el-form-item>-->
            <div class="choice-card-bottom">
              <span class="cancel" @click="handleHideChoice">Cancel</span>
              <span class="confirm" @click="handleHideChoice">Confirm</span>
            </div>
          </el-form>
        </el-card>

      </div>

      <div class="main-block">
<!--        排序标签，太丑，先注释-->
<!--        <div class="sort-choice-block">
          <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="default" name="first"></el-tab-pane>
            <el-tab-pane label="up-to-date" name="second"></el-tab-pane>
            <el-tab-pane label="popular" name="third"></el-tab-pane>
            <el-tab-pane label="cheapest" name="fourth"></el-tab-pane>
          </el-tabs>
        </div>-->
        <div class="list-container">
          <p style="font-size: 2em;padding: 20px 0 10px 20px;font-weight: bold;text-align: left">We find more than 100 houses for you:</p>
          <el-card class="list-block" v-for="(item,index) in houseList" :key="index" shadow="hover" >
            <el-row class="house-item">
              <el-col span="8" style="height: 100%;">
                <el-image class="item-img" :src=item.imgUrl fit="cover"></el-image>
              </el-col>
              <el-col span="12">
                <div class="item-text">
                  <div class="item-name" @click="handleClickTitle(item.houseId)">{{ item.title }}</div>
                  <div class="item-pos item-little"><i class="el-icon-position"> </i>{{ item.position }}</div>
                  <div class="item-details item-little"><i class="el-icon-s-home"> </i>{{ item.describe }}</div>
<!--                  <div class="item-collection item-little"><i class="el-icon-star-off"> </i>{{ item.collection }}</div>-->
                </div>
              </el-col>
              <el-col span="4" style="height: 100%">
                <div class="item-price">{{item.totalPrice}}<span style="color: red;padding-left: 5px">million</span></div>
              </el-col>
            </el-row>
          </el-card>
        </div>
        <div id="map" :class="[ mapShow ? 'map_show' : 'map_hide' ]"></div>
      </div>
    </div>
    <div :class="{'bland':choiceCardVisible.bland}" @click="handleHideChoice" style="transition: .3s"></div>
  </div>
</template>

<script>
import HeaderNav from '@/components/headerNav/index.vue'
import * as L from 'leaflet'
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
import {getHouseList} from '@/utils/api'


export default {
  name: "index",
  components: {
    HeaderNav,
  },
  data() {
    return {
      map:undefined,
      mapShow:true,
      searchValue:undefined,
      recommendationList: [{name: "house1", image: "../assets/home_header_bg.jpg"}, {
        name: "house1",
        image: "../assets/home_header_bg.jpg"
      }, {name: "house1", image: "../assets/home_header_bg.jpg"}, {
        name: "house1",
        image: "../assets/home_header_bg.jpg"
      }],
      choiceCardVisible: {bland: false, date: false, type: false, price: false, more: false, init: true},
      choice: {
        dateRange: {
          start: undefined,
          end: undefined
        },
        houseType: [],
        price: [0, 0]
      },
      houseType: [{title: 'Whole house', value: 0}, {title: 'Separate room', value: 1}, {
        title: 'Separate room',
        value: 1
      }, {title: 'Shared room', value: 2}],
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      activeName: 'first',
      houseList: [],
      navContent: [{name: 'Center', router: '/center'}, {name: 'Collection', router: '/center/collection'}, {name: 'Start to Sale', router: '/center/sale'}]
    }
  },
  created(){
    this.getList()
    if(this.$route.params.searchValue) this.searchValue=this.$route.params.searchValue
  },
  mounted() {
    this.initMap()
  },
  methods: {
    initMap(){
      this.map = L.map('map', {
      });
      L.Marker.prototype.options.icon = L.icon({
        iconUrl: icon,
        shadowUrl: iconShadow
      });
      this.map.locate({setView: true, maxZoom: 16});
      L.tileLayer(
          "http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
          {
            subdomains: ["1", "2", "3", "4"],
            attribution: "高德"
          }
      ).addTo(this.map);
      function onLocationFound(e) {
        console.log(e)
        var radius = e.accuracy;
        L.marker(e.latlng).addTo(this.map)
            .bindPopup("You are within " + radius + " meters from this point").openPopup();

        L.circle(e.latlng, radius).addTo(this.map);
      }

      this.map.on('locationfound', onLocationFound);

      // function onLocationError(e) {
      //     alert(e.message);
      // }
      //
      // map.on('locationerror', onLocationError);
    },
    handleChoiceButton(choice) {
      switch (choice) {
        case 'date':
          this.choiceCardVisible.date = true;
          break
        case 'type':
          this.choiceCardVisible.type = true;
          break
        case 'price':
          this.choiceCardVisible.price = true;
          break
      }
      this.choiceCardVisible.bland = true
      this.choiceCardVisible.more = false
      console.log('-----choiceCardVisible-------', this.choiceCardVisible)
    },
    handleMoreButton() {
      this.choiceCardVisible.more = !this.choiceCardVisible.more;
      if (this.choiceCardVisible.init) {
        this.choiceCardVisible.init = false
      }
    },
    handleHideChoice() {
      this.choiceCardVisible.bland = true;
      for (let item in this.choiceCardVisible) {
        console.log(this.choiceCardVisible[item] = false)
      }
    },
    handleMapSwitch(){
      // this.mapShow=!this.mapShow;
      // this.map.invalidateSize(true);

      setTimeout(()=>{
        this.map.invalidateSize(true)
      }, 400)
    },
    handleClickTitle(houseId){
      this.$router.push({name: 'detail', params: {houseId: houseId}})
    },
    getList(){
      getHouseList(this.form).then(res=>{
        console.log(res);
        if(res.data.success){
          this.houseList=res.data.data.houseList
        }
      })
    },
  }
}
</script>

<style scoped>
.recommendation-carousel {
  width: 100%;
  padding: 10px 0;
}

.recommendation-carousel .recommendation-title {
  font-size: 1.8rem;
  color: rgba(84, 92, 100, 1);
  text-align: left;
  padding: 10px 10px 10px 2%;
}

.check-block {
  /*margin: 20px 10px;*/
  height: 0;
  box-shadow: 0 0;
  border: 0;
  /*width: 100%;*/
  width: calc(100% - 20px);
  position: absolute;
  z-index: 99;
  border-bottom: solid 1px rgba(0,0,0,0.1);
}

.check-block_show {
  animation: forwards showMore .4s;
}

.check-block_hide {
  animation: forwards hideMore .4s;
}


.choice-button-group {
  margin: 20px 10px;
  display: flex;
  align-items: center;
  height: 40px;
}

.choice-div {
  display: inline-block;
  position: relative;
  margin-right: 10px;
  float: left;
}

.main-block {
  background-color: white;
  /*max-width: 1200px;*/
  margin: 0 auto;
  height: calc(100vh - 140px);
  display: flex;
  -webkit-box-shadow:  0 -10px 10px rgba(0,0,0,0.2);
  box-shadow:  0 -10px 10px rgba(0,0,0,0.2);
}
.list-container::-webkit-scrollbar {
  /*滚动条整体样式*/
  width : 10px;  /*高宽分别对应横竖滚动条的尺寸*/
  height: 1px;
}
.list-container::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 10px;
  box-shadow   : inset 0 0 5px rgba(0, 0, 0, 0.2);
  background   : #535353;
}
.list-container::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow   : inset 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  background   : #ededed;
}
.list-container{
  height: 100%;
  overflow: auto;
  flex: 2;
}
.map_show{
  flex: 1;
  display: block;
  height: 100%;
}
.map_hide{
  flex: 1;
  display: none;
  height: 100%;
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
  text-overflow:ellipsis;
  white-space: nowrap;
  transition: color .2s;
  cursor: pointer;
}
.house-item .item-name:hover{
  color: #409EFF;
}
.house-item .item-pos{
  overflow: hidden;
  text-overflow:ellipsis;
  white-space: nowrap;
}
.house-item .item-img{
  height: 100%;
}
.house-item .item-details{

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

.choice-button {
  position: relative;
}

.choice-card {
  position: absolute;
  display: none;
  top: calc(100% + 10px);
  left: 0;
  z-index: 999999;
}

.choice-card-bottom .confirm {
  float: right;
  color: #008489;
  font-weight: bold;
  cursor: pointer;
}

.choice-card-bottom .cancel {
  float: left;
  font-weight: bold;
  cursor: pointer;
}

.choice-card-bottom {
  width: 100%;
  overflow: auto;
}

.choice-card-show {
  display: block;
}

.bland {
  position: fixed;
  height: 100%;
  width: 100%;
  left: 0;
  top: 0;
  background: rgba(255, 255, 255, 0.6);
  transition: .3s;
}

.bland-hide {
  position: fixed;
  height: 100%;
  width: 100%;
  left: 0;
  top: 0;
  background: rgba(255, 255, 255, 0);
  display: none;
  transition: .3s;
}
.switch-div{
  overflow: auto;
  width: 100%;
  text-align: end;
  margin: auto 20px auto 0;
}
@keyframes showMore {
  0% {
    height: 0;
    box-shadow: 0 0;
    border: 0;
    border-bottom: solid 1px rgba(0,0,0,0.1);
  }
  100% {
    height: 220px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0 , 0.1);
    border: 1px solid #EBEEF5;
    border-bottom: solid 1px rgba(0,0,0,0.1);
  }
}

@keyframes hideMore {
  0% {
    height: 220px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0  ,0.1);
    border: 1px solid #EBEEF5;
    border-bottom: solid 1px rgba(0,0,0,0.1);
  }
  100% {
    height: 0;
    box-shadow: 0 0;
    border: 0;
    border-bottom: solid 1px rgba(0,0,0,0.1);
  }
}
.list-block{
  margin: 10px;
}
  #map{
    z-index: 1;
  }
</style>
<style>
.check-block .el-form-item {
  margin-bottom: 0;
}

.check-block .el-form-item__content, .check-block .el-form-item__label {
  line-height: 15px !important;
}

.check-block .el-form-item__content {
  text-align: left;
}

.choice-card .el-checkbox__inner {
  width: 19px;
  height: 19px;
}

.choice-card .el-checkbox__label {
  font-size: 19px;
  line-height: 30px;
}

.choice-card .el-checkbox {
  display: flex;
  align-items: center;
  padding: 15px;
}

.choice-card .el-checkbox-group {
  margin-bottom: 20px;
}

.choice-card .el-checkbox__inner::after {
  box-sizing: content-box;
  content: "";
  border: 1px solid #FFF;
  border-left: 0;
  border-top: 0;
  height: 9px;
  left: 5px;
  position: absolute;
  top: 2px;
  transform: rotate(45deg) scaleY(0);
  width: 5px;
  transition: transform .15s ease-in .05s;
  transform-origin: center;
}
</style>
