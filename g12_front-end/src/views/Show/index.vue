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
                     :class="{'choice-card-show':choiceCardVisible.type}" style="width: 500px
">
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
              price
            </el-button>
            <el-card class="choice-card" :class="{'choice-card-show':choiceCardVisible.price}"
                     style="width: 600px">
              <div>
                <p>totalPrice</p>
                <el-row :gutter=20>
                  <el-col :span=6 class="ds-flex ds-ver_center">
                    <el-input v-model="form.totalPriceRange[0]" style="flex: 2"
                              type="text"></el-input>
                    <span>￥</span>
                  </el-col>
                  <el-col :span=12>
                    <el-slider
                        v-model="form.totalPriceRange"
                        range
                        :step="1000"
                        :max="200000">
                    </el-slider>
                  </el-col>
                  <el-col :span=6 class="ds-flex ds-ver_center">
                    <el-input v-model="form.totalPriceRange[1]" style="flex: 2"
                              type="text"></el-input>
                    <span>￥</span>
                  </el-col>
                </el-row>
              </div>
              <el-divider></el-divider>
              <div>
                <p>unitPrice</p>
                <el-row :gutter=20>
                  <el-col :span=6 class="ds-flex ds-ver_center">
                    <el-input v-model="form.unitPriceRange[0]" style="flex: 2"
                              type="text"></el-input>
                    <span>￥/m2</span>
                  </el-col>
                  <el-col :span=12>
                    <el-slider
                        v-model="form.unitPriceRange"
                        range
                        :max="1000000">
                    </el-slider>
                  </el-col>
                  <el-col :span=6 class="ds-flex ds-ver_center">
                    <el-input v-model="form.unitPriceRange[1]" style="flex: 2"
                              type="text"></el-input>
                    <span>￥/m2</span>
                  </el-col>
                </el-row>
              </div>
              <el-divider></el-divider>
              <div class="mg-b-20">
                <p>area</p>
                <el-row :gutter=20>
                  <el-col :span=6 class="ds-flex ds-ver_center">
                    <el-input v-model="form.area[0]" style="flex: 2" type="text"></el-input>
                    <span>m2</span>
                  </el-col>
                  <el-col :span=12>
                    <el-slider
                        v-model="form.area"
                        range
                        :max="1000">
                    </el-slider>
                  </el-col>
                  <el-col :span=6 class="ds-flex ds-ver_center">
                    <el-input v-model="form.area[1]" style="flex: 2" type="text"></el-input>
                    <span>m2</span>
                  </el-col>
                </el-row>
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
        <div class="list-container" v-loading="loading">
          <p style="" class="list-header_title">We find {{ total }} houses for you:</p>
          <el-card class="list-block" v-for="(item,index) in houseList" :key="index" shadow="hover">
            <el-row class="house-item">
              <el-col :span=8 style="height: 100%;position: relative">
                <el-image class="item-img" :src=item.imgUrl fit="cover"></el-image>
                <div class="item-collection item-little" @click="handleCollect(index,item.collected)">
                  <i href="#" class="contain-icon icon-hook" :class="{'active':item.collected}">
                    <!--Begin Second Star Icon-->
                    <svg class="star-icon star-icon-2" version="1.1"
                         viewBox="0 0 105.602 102.931" style="width: 20px;height: 20px">
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
          </el-card>
          <el-pagination
              :page-size="form.pageSize"
              layout="prev, pager, next"
              :total="total"
              v-if="total">
          </el-pagination>
          <div class="w-100" v-if="!total">
            <el-image :src="require('@/assets/emptyData.png')" fit="contain"/>
          </div>
        </div>
        <div id="map" :class="[ mapShow ? 'map_show' : 'map_hide' ]"></div>
      </div>
    </div>
    <div :class="{'bland':choiceCardVisible.bland}" @click="handleHideChoice" style="transition: .3s"></div>
  </div>
</template>

<script>
import HeaderNav from '@/components/headerNav/index.vue'
import moreFilter from '@/components/moreFilter/index.vue'
import * as L from 'leaflet'
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
import {getHouseList,addCollection} from '@/utils/api'
import global from '@/assets/global'


export default {
  name: "index",
  components: {
    HeaderNav,
    moreFilter
  },
  data() {
    return {
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
      houseList: [],
      navContent: [{name: 'Center', router: '/center'}, {
        name: 'Collection',
        router: '/center/collection'
      }, {name: 'Start to Sale', router: '/center/sale'}],
      global: global,
      screenWidth: document.body.clientWidth
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
    if (this.screenWidth >= 768) {
      this.initMap()
    }
    window.onresize = () => {
      return (() => {
        window.screenWidth = document.body.clientWidth
        this.screenWidth = window.screenWidth
      })()
    };
  },
  methods: {
    initMap() {
      this.map = L.map('map', {});
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
    handleClickTitle(houseId) {
      this.$router.push({name: 'detail', params: {houseId: houseId}})
    },
    handleCollect(index,collected){
      addCollection({houseId:this.houseList[index].houseId,userId:this.$store.state.userId,collected:collected}).then(()=>{
        this.houseList[index].collected=collected
      })
    },
    getList() {
      this.loading = true
      getHouseList(this.form).then(res => {
        console.log(res);
        if (res.success) {
          this.houseList = res.data.houseList;
          this.total = res.data.total
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

  .choice-div {
    position: relative;
  }

  .map_show {
    display: block;
  }

  .list-header_title {
    font-size: 2em;
  }

  .choice-button-group {
    overflow-x: unset;
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
    overflow-x: auto;
  }
}

@media (min-width: 576px) {
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
}

@media (max-width: 576px) {
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

  .house-item .item-img {
    height: 100%;
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
  overflow-x: auto;
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
  -webkit-box-shadow: 0 -10px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 -10px 10px rgba(0, 0, 0, 0.2);
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

.list-block {
  margin: 10px;
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
.choice-card .el-checkbox__inner {
  width: 19px;
  height: 19px;
}

@media (min-width: 768px) {
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
