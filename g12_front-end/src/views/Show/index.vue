<template>
  <div>
    <HeaderNav :navContent="navContent" :show-search=true :searchString="form.searchString"
               @getSearch="getSearch"></HeaderNav>
    <div style="padding: 0 10px">
      <div class="head-content">
        <div class="choice-button-group">

          <div class="choice-div">
            <el-button class="choice-button" @click="handleChoiceButton('date')">
              date
            </el-button>
            <el-card class="choice-card" :class="{'choice-card-show':choiceCardVisible.date}">
              <vc-date-picker v-model="choice.dateRange" :columns="$screens({ default: 1, lg: 2 })"
                              is-range
                              style="border: 0"/>
              <div class="choice-card-bottom">
                <span class="cancel" @click="handleHideChoice">Cancel</span>
                <span class="confirm" @click="handleConfirmChoice">Confirm</span>
              </div>
            </el-card>
          </div>

          <div class="choice-div">
            <el-button class="choice-button" @click="handleChoiceButton('type')">
              district
            </el-button>
            <el-card class="choice-card choice-district"
                     :class="{'choice-card-show':choiceCardVisible.type}">
              <div>
                <el-row :gutter=20>
                  <el-checkbox-group v-model="form.district">
                    <el-col :span=8 v-for="(value,key) in global.district" :key="value">
                      <el-checkbox :label="value" name="type" :value="value">{{ key }}</el-checkbox>
                    </el-col>
                  </el-checkbox-group>
                </el-row>
              </div>
              <div class="choice-card-bottom">
                <span class="cancel" @click="handleHideChoice">Cancel</span>
                <span class="confirm" @click="handleConfirmChoice">Confirm</span>
              </div>
            </el-card>
          </div>

          <div class="choice-div">
            <el-button class="choice-button" @click="handleChoiceButton('price')">
              range
            </el-button>
            <el-card class="choice-card choice-range" :class="{'choice-card-show':choiceCardVisible.price}"
            >
              <div>
                <p>totalPrice</p>
                <b-row>
                  <b-col cols=3 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
                    <el-input v-model="form.totalPriceRange[0]" style="flex: 2" type="text"></el-input>
                    <span style="margin-left: 10px;line-height:40px">￥</span>
                  </b-col>
                  <b-col v-if="this.screenWidth >= 768" cols=6>
                    <el-slider
                        v-model="form.totalPriceRange"
                        range
                        :step="100000"
                        :max="100000000"
                        >
                    </el-slider>
                  </b-col>
                  <b-col v-if="this.screenWidth < 768" cols=12>
                    <el-slider
                        v-model="form.totalPriceRange"
                        range
                        :step="100000"
                        :max="100000000"
                        :tooltip-class="{'ds-none':!this.showTooltip}">
                    </el-slider>
                  </b-col>
                  <b-col cols=3 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
                    <el-input v-model="form.totalPriceRange[1]" style="flex: 2" type="text"></el-input>
                    <span style="margin-left: 10px;line-height:40px">￥</span>
                  </b-col>
                </b-row>
              </div>
              <el-divider></el-divider>
              <div>
                <p>unitPrice</p>
                <b-row>
                  <b-col cols=3 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
                    <el-input v-model="form.unitPriceRange[0]" style="flex: 2" type="text"></el-input>
                    <span style="margin-left: 10px;line-height:40px">￥/m2</span>
                  </b-col>
                  <b-col v-if="this.screenWidth >= 768" cols=6>
                    <el-slider
                        v-model="form.unitPriceRange"
                        range
                        :step="1000"
                        :max="200000">
                    </el-slider>
                  </b-col>
                  <b-col v-if="this.screenWidth < 768" cols=12>
                    <el-slider
                        v-model="form.unitPriceRange"
                        range
                        :step="1000"
                        :max="200000">
                    </el-slider>
                  </b-col>
                  <b-col cols=3 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
                    <el-input v-model="form.unitPriceRange[1]" style="flex: 2" type="text"></el-input>
                    <span style="margin-left: 10px;line-height:40px">￥/m2</span>
                  </b-col>
                </b-row>
              </div>
              <el-divider></el-divider>
              <div class="mg-b-20">
                <p>area</p>
                <b-row>
                  <b-col cols=3 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
                    <el-input v-model="form.area[0]" style="flex: 2" type="text"></el-input>
                    <span style="margin-left: 10px;line-height:40px">m2</span>
                  </b-col>
                  <b-col v-if="this.screenWidth >= 768" cols=6>
                    <el-slider
                        v-model="form.area"
                        range
                        :step="100"
                        :max="1000">
                    </el-slider>
                  </b-col>
                  <b-col v-if="this.screenWidth < 768" cols=12>
                    <el-slider
                        v-model="form.area"
                        range
                        :max="1000">
                    </el-slider>
                  </b-col>
                  <b-col cols=3 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
                    <el-input v-model="form.area[1]" style="flex: 2" type="text"></el-input>
                    <span style="margin-left: 10px;line-height:40px">m2</span>
                  </b-col>
                </b-row>
              </div>
              <div class="choice-card-bottom">
                <span class="cancel" @click="handleHideChoice">Cancel</span>
                <span class="confirm" @click="handleConfirmChoice">Confirm</span>
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

        <moreFilter :form="form" @handleCancel="handleHideChoice" @handleConfirm="handleConfirmChoice"
                    :choiceCardVisible="choiceCardVisible"></moreFilter>

      </div>

      <div class="main-block" v-loading="loading">
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
          <p style="" class="list-header_title">We find {{ total }} houses for you:</p>
          <listCard :houseList="houseList" @mouseover="mouseover" @mouseLeave="mouseLeave"></listCard>
          <el-pagination
              :page-size="form.pageSize"
              background
              layout="prev, pager, next"
              :total="total"
              v-if="total"
              :current-page.sync="form.pageNum"
          >
          </el-pagination>
          <div class="w-100" v-if="!total">
            <el-image :src="require('@/assets/emptyData.png')" fit="contain"/>
          </div>
        </div>
        <div id="map" :class="[ mapShow ? 'map_show' : 'map_hide' ]"></div>
      </div>
    </div>
    <div :class="{'bland':choiceCardVisible.bland}" @click="handleHideChoice"
         style="transition: .3s;z-index: 1100;"></div>
  </div>
</template>


<script>
import HeaderNav from '@/components/headerNav/index.vue'
import listCard from '@/components/listCard/index.vue'
import moreFilter from '@/components/moreFilter/index.vue'
import * as L from 'leaflet'
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
import global from '@/assets/global'
import {getHouseList} from '@/utils/api'
// import 'leaflet/dist/leaflet.css'
// import 'leaflet.pm'
// import 'leaflet.pm/dist/leaflet.pm.css'

export default {
  name: "index",
  components: {
    HeaderNav,
    moreFilter,
    listCard
  },
  data() {
    return {
      showTooltip:false,
      loading: false,
      map: undefined,
      mapShow: true,
      total: 0,
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
        totalPriceRange: [0, 0],
        unitPriceRange: [0, 0],
        area: [0, 0],
        district: [],
        houseStructure: [],
        direction: [],
        decoration: [],
        heating: [],
        elevator: [],
        searchString: "",
        pageNum: 1,
        pageSize: 10
      },
      activeName: 'first',
      navContent: [{name: 'Center', router: '/center'}, {
        name: 'Collection',
        router: '/center/collection'
      }, {name: 'Start to Sale', router: '/center/sale'}],
      global: global,
      screenWidth: document.body.clientWidth,
      houseList: [],
      mapInited: false,
      markerList:[],
    }
  },
  created() {
    console.log(this.$route.params)
    console.log("--------userId--------", this.$store.state)
    if (this.$route.params.searchString) {
      this.form.searchString = this.$route.params.searchString
    }
    console.log(this.form)
    this.getList()
  },
  mounted() {
    // if (this.screenWidth >= 768) {
    //   this.initMap()
    // }
    window.onresize = () => {
      return (() => {
        window.screenWidth = document.body.clientWidth
        this.screenWidth = window.screenWidth
      })()
    };
  },
  watch: {
    'form.pageNum'() {
      // this.form.pageNum=val
      this.loading = true
      this.getList()
    }
  },
  methods: {
    initMap() {
      if(!this.mapInited){
        L.Marker.prototype.options.icon = L.icon({
          iconUrl: icon,
          shadowUrl: iconShadow
        });
        this.map = L.map('map', { center: {lat:this.houseList[0].latitude,lng: this.houseList[0].longitude},zoom: 8});
        // this.map.locate({setView: true, maxZoom: 16});
        L.tileLayer(
            "http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
            // 'http://mt0.google.cn/vt/lyrs=y@160000000&hl=zh-CN&gl=CN&src=app&y={y}&x={x}&z={z}&s=Ga',
            {
              subdomains: ["1", "2", "3", "4"],
              attribution: "高德"
            }
        ).addTo(this.map);
        // this.map.on('locationfound', (e) =>{
        //   console.log(e)
        //   var radius = e.accuracy;
        //   console.log(L.marker(e.latlng))
        //   L.marker(e.latlng).addTo(this.map)
        //       .bindPopup("You are within " + radius + " meters from this point").openPopup();
        //
        //   // L.circle(e.latlng, radius).addTo(this.map);
        // })

        // function onLocationError(e) {
        //     alert(e.message);
        // }
        //
        // map.on('locationerror', onLocationError);
        this.mapInited=true
      }
    },
    mouseover(index){
      // console.log("parent mouseover")
      this.markerList[index].openPopup()
    },
    mouseLeave(index){
      // console.log("parent mouseLeave")
      this.markerList[index].closePopup()
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
          this.showTooltip=true
          break
      }
      this.choiceCardVisible.bland = true
      this.choiceCardVisible.more = false
    },
    handleMoreButton() {
      this.choiceCardVisible.more = !this.choiceCardVisible.more;
      if (this.choiceCardVisible.init) {
        this.choiceCardVisible.init = false
      }
    },
    handleHideChoice() {
      this.choiceCardVisible.bland = true;
      let init = this.choiceCardVisible.init
      for (let item in this.choiceCardVisible) {
        console.log(this.choiceCardVisible[item] = false)
      }
      this.choiceCardVisible.init = init
      this.showTooltip=false
    },
    handleConfirmChoice() {
      this.getList()
      this.handleHideChoice()
    },
    handleMapSwitch() {
      // this.mapShow=!this.mapShow;
      // this.map.invalidateSize(true);

      setTimeout(() => {
        this.map.invalidateSize(true)
      }, 400)
    },
    getList() {
      this.loading = true;
      getHouseList(this.form).then(res => {
        console.log(res);
        if (res.success) {
          this.houseList = res.data.houseList;
          this.total = res.data.total
          this.$nextTick(()=>{
            if (this.screenWidth >= 768) {
              this.initMap()
              this.markerList=[]
              for(let i=0;i<this.houseList.length;i++){
                this.markerList.push(L.marker({lat:this.houseList[i].latitude,lng: this.houseList[i].longitude}).addTo(this.map).bindPopup(this.houseList[i].totalPrice+"million"))
              }
            }
          })
            }
        this.loading = false
      }).catch(() => {
        this.loading = false
      })
    },
    getSearch(sv) {
      console.log(sv);
      this.form.searchString = sv;
      this.getList()
    },
  }
}
</script>

<style scoped>
@import "../../assets/css/star.css";

@media (min-width: 768px) {
  .choice-card {
    position: absolute;
    top: calc(100% + 10px);
    left: 0;
  }

  .choice-range {
    width: 600px;
  }

  .choice-div {
    position: relative;
  }

  .map_show {
    display: block;
  }

  .list-header_title {
    font-size: 2em;
  }

}

@media (max-width: 768px) {
  .choice-card {
    position: absolute;
    top: 130px;
    left: 2.5vw;
    width: 95vw !important;
  }

  .choice-div {
    position: unset;
  }

  .map_show {
    display: none;
  }

  .list-header_title {
    font-size: 1em;
  }

  .choice-button-group {
    overflow-x: unset;
  }
}

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

.choice-button-group {
  margin: 20px 10px;
  display: flex;
  align-items: center;
  height: 40px;
}

.choice-div {
  display: inline-block;
  /*position: relative;*/
  margin-right: 10px;
  float: left;
}

.main-block {
  background-color: white;
  /*max-width: 1200px;*/
  margin: 0 auto;
  height: calc(100vh - 140px);
  display: flex;
  -webkit-box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  padding-bottom: 15px;
}

.list-container::-webkit-scrollbar {
  /*滚动条整体样式*/
  width: 10px; /*高宽分别对应横竖滚动条的尺寸*/
  height: 1px;
}

.list-container::-webkit-scrollbar-thumb {
  /*滚动条里面小方块*/
  border-radius: 10px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  background: #535353;
}

.list-container::-webkit-scrollbar-track {
  /*滚动条里面轨道*/
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  background: #ededed;
}

.list-container {
  height: 100%;
  overflow: auto;
  overflow-x: hidden;
  flex: 2;
}

.map_show {
  flex: 1;
  height: 100%;
}

.map_hide {
  flex: 1;
  display: none;
  height: 100%;
}


.choice-button {
  position: relative;
}

.choice-card {
  position: absolute;
  display: none;
  z-index: 1200;
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

.switch-div {
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
    border-bottom: solid 1px rgba(0, 0, 0, 0.1);
  }
  100% {
    height: 220px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border: 1px solid #EBEEF5;
    border-bottom: solid 1px rgba(0, 0, 0, 0.1);
  }
}

@keyframes hideMore {
  0% {
    height: 220px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    border: 1px solid #EBEEF5;
    border-bottom: solid 1px rgba(0, 0, 0, 0.1);
  }
  100% {
    height: 0;
    box-shadow: 0 0;
    border: 0;
    border-bottom: solid 1px rgba(0, 0, 0, 0.1);
  }
}


.list-header_title {
  padding: 20px 0 10px 20px;
  font-weight: bold;
  text-align: left
}

#map {
  z-index: 1;
}
</style>
<style>
    .choice-card .el-loading-mask{
        z-index: 1000!important;
    }
.main-block .leaflet-popup{
  left: -36px!important;
}
.choice-card .el-checkbox__inner {
  width: 19px;
  height: 19px;
}

@media (min-width: 768px) {
  .choice-district {
    width: 500px
  }

  .choice-district .el-checkbox__label {
    font-size: 19px;
    line-height: 30px;
  }
}

@media (max-width: 768px) {
  .choice-district .el-checkbox__label {
    font-size: 12px;
    line-height: 12px;
  }
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

.lh-40 {
  line-height: 40px;
}
</style>
