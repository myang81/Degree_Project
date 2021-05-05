<template>
  <div style="height: 100%;flex-direction: column">
    <P class="center-title">Choose your home address</P>
    <b-row style="height: 100%" :gutter=20>
      <b-col cols="12" md="6"  class="map-container">
        <div id="map" style="height: 100%;">
        </div>
      </b-col>
      <b-col cols="12" md="6">
        <div class="form-community">
          <el-form label-position="right" label-width="120px" :model="form" ref="ruleForm" :rules="rules">
            <b-row>
              <b-col  :span=24>
                <el-form-item label="region/district" style="text-align: left" prop="regionAndDistrict" label-width="120px" >
                  <!--                <el-autocomplete v-model="form.region" :fetch-suggestions="querySearchRegion"></el-autocomplete>-->
                  <el-cascader
                      v-model="form.regionAndDistrict"
                      :options="options"
                  ></el-cascader>
                </el-form-item>
              </b-col>
            </b-row>
            <b-row>
              <b-col  :span=24>
                <el-form-item label="community" style="text-align: left" prop="community" label-width="120px" >
                  <el-select v-model="form.community" filterable placeholder="please choose"  :remote-method="remoteMethod" :loading="loading" remote>
                    <el-option
                        v-for="value in community"
                        :key="value"
                        :label="value"
                        :value="value">
                    </el-option>
                  </el-select>
                </el-form-item>
              </b-col>
            </b-row>
            <b-row>
              <b-col cols="12" md="6">
                <el-form-item label="longitude"  prop="lng">
                  <el-input v-model="form.lng"></el-input>
                </el-form-item>
              </b-col>
              <b-col cols="12" md="6">
                <el-form-item label="latitude" prop="lat">
                  <el-input v-model="form.lat"></el-input>
                </el-form-item>
              </b-col>
            </b-row>
            <b-col style="text-align: end" cols="12">
              <el-button type="primary" @click="onSubmit" style="width: 100%">N E X T</el-button>
            </b-col>
          </el-form>
        </div>
      </b-col>
    </b-row>

  </div>
</template>

<script>
import global from '@/assets/global'
import * as L from 'leaflet'
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
import {searchCommunity} from '@/utils/api'

/**
 * 未做表单验证
 * */
export default {
name: "address",
  data(){
    return {
      loading:false,
      form:{
        regionAndDistrict:undefined,
        // coordinate:[undefined,undefined],
        lng:undefined,
        lat:undefined,
        community:''
      },
      rules: {
        regionAndDistrict: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
        community: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
        lng: [
          {required: true, message: '请选择活动区域', trigger: 'blur'}
        ],
        lat: [
          {required: true, message: '请选择日期', trigger: 'blur'}
        ],
      },
      options:[
        {
          "value": "a1",
          "label": "Fengtai",
          "children": [
            {
              "value": 209,
              "label": "Corner_Gate"
            },
            {
              "value": 207,
              "label": "Xiluoyuan"
            },
            {
              "value": 61,
              "label": "Lugou_Bridge"
            },
            {
              "value": 18,
              "label": "Fengtai_others"
            },
            {
              "value": 127,
              "label": "New_palace"
            },
            {
              "value": 48,
              "label": "Beidadi"
            },
            {
              "value": 129,
              "label": "Fangzhuang"
            },
            {
              "value": 225,
              "label": "green_pagoda"
            },
            {
              "value": 102,
              "label": "songjiazhuang"
            },
            {
              "value": 232,
              "label": "Majiabao"
            },
            {
              "value": 194,
              "label": "Caoqiao"
            },
            {
              "value": 111,
              "label": "Yuegezhuang"
            },
            {
              "value": 1,
              "label": "Qilizhuang"
            },
            {
              "value": 46,
              "label": "Beijing_South_Railway_Station"
            },
            {
              "value": 211,
              "label": "Zhao_Gongkou"
            },
            {
              "value": 125,
              "label": "Chengshou_Temple"
            },
            {
              "value": 139,
              "label": "Muxiyuan"
            },
            {
              "value": 166,
              "label": "Yuquanying"
            },
            {
              "value": 37,
              "label": "Liuli_bridge"
            },
            {
              "value": 196,
              "label": "Puhuangyu"
            },
            {
              "value": 42,
              "label": "Liu_Jia_Yao"
            },
            {
              "value": 195,
              "label": "Caihuying"
            },
            {
              "value": 95,
              "label": "Taiping_Bridge"
            },
            {
              "value": 89,
              "label": "Dahongmen"
            },
            {
              "value": 191,
              "label": "Hometown_of_flowers"
            },
            {
              "value": 177,
              "label": "See_Dan_bridge"
            },
            {
              "value": 20,
              "label": "Lizer"
            },
            {
              "value": 182,
              "label": "science_and_Technology_Park"
            },
            {
              "value": 71,
              "label": "Heyi"
            },
            {
              "value": 151,
              "label": "Foreign_bridge"
            },
            {
              "value": 27,
              "label": "Wulidian"
            },
            {
              "value": 235,
              "label": "malian_road"
            },
            {
              "value": 25,
              "label": "Wukesong"
            },
            {
              "value": 69,
              "label": "youanmenwai"
            },
            {
              "value": 130,
              "label": "Old_palace"
            },
            {
              "value": 117,
              "label": "Guanganmen"
            },
            {
              "value": 206,
              "label": "Xihongmen"
            },
            {
              "value": 149,
              "label": "Yongdingmen"
            }
          ]
        },
        {
          "value": "a8",
          "label": "Fangshan",
          "children": [
            {
              "value": 161,
              "label": "Yanshan"
            },
            {
              "value": 219,
              "label": "Changyang"
            },
            {
              "value": 189,
              "label": "Good_country"
            },
            {
              "value": 221,
              "label": "Yan_Village"
            },
            {
              "value": 183,
              "label": "Doudian"
            },
            {
              "value": 168,
              "label": "Liuli_River"
            },
            {
              "value": 126,
              "label": "Fangshan_others"
            },
            {
              "value": 226,
              "label": "Hancun_River"
            },
            {
              "value": 81,
              "label": "Chengguan"
            }
          ]
        },
        {
          "value": "a12",
          "label": "Shijingshan",
          "children": [
            {
              "value": 193,
              "label": "Apple_Orchard"
            },
            {
              "value": 220,
              "label": "Mentougou_others"
            },
            {
              "value": 167,
              "label": "Yuquan_Road"
            },
            {
              "value": 240,
              "label": "Lugu"
            },
            {
              "value": 180,
              "label": "shijingshan_others"
            },
            {
              "value": 35,
              "label": "Anise"
            },
            {
              "value": 82,
              "label": "Chengzi"
            },
            {
              "value": 142,
              "label": "Yangzhuang"
            },
            {
              "value": 67,
              "label": "Ancient_city"
            },
            {
              "value": 188,
              "label": "Laoshan"
            }
          ]
        },
        {
          "value": "a0",
          "label": "Dongcheng",
          "children": [
            {
              "value": 79,
              "label": "Dianmen"
            },
            {
              "value": 10,
              "label": "Dongdan"
            },
            {
              "value": 14,
              "label": "Dongzhimen"
            },
            {
              "value": 112,
              "label": "Chongwenmen"
            },
            {
              "value": 113,
              "label": "Gongti"
            },
            {
              "value": 120,
              "label": "Jianguo_men_Nei"
            },
            {
              "value": 72,
              "label": "Peace_Lane"
            },
            {
              "value": 114,
              "label": "Zuoanmen"
            },
            {
              "value": 100,
              "label": "Andingmen"
            },
            {
              "value": 149,
              "label": "Yongdingmen"
            },
            {
              "value": 15,
              "label": "Donghua_Market"
            },
            {
              "value": 30,
              "label": "crossing"
            },
            {
              "value": 160,
              "label": "dengshikou"
            },
            {
              "value": 216,
              "label": "Jinbao_Street"
            },
            {
              "value": 118,
              "label": "Guangqumen"
            },
            {
              "value": 136,
              "label": "Inside_Chaoyang_Gate"
            },
            {
              "value": 101,
              "label": "Anzhen"
            },
            {
              "value": 137,
              "label": "Outside_Chaoyang_Gate"
            },
            {
              "value": 223,
              "label": "Taoran_Pavilion"
            },
            {
              "value": 90,
              "label": "The_temple_of_heaven"
            },
            {
              "value": 11,
              "label": "Dongsi"
            },
            {
              "value": 43,
              "label": "front_door"
            },
            {
              "value": 196,
              "label": "Puhuangyu"
            },
            {
              "value": 121,
              "label": "Outside_Jianguo"
            }
          ]
        },
        {
          "value": "a13",
          "label": "Xicheng",
          "children": [
            {
              "value": 79,
              "label": "Dianmen"
            },
            {
              "value": 233,
              "label": "Madian"
            },
            {
              "value": 174,
              "label": "White_paper_shop"
            },
            {
              "value": 217,
              "label": "Financial_Street"
            },
            {
              "value": 140,
              "label": "muxidi"
            },
            {
              "value": 38,
              "label": "Liupu_Kang"
            },
            {
              "value": 235,
              "label": "malian_road"
            },
            {
              "value": 91,
              "label": "Tianning_Temple"
            },
            {
              "value": 103,
              "label": "Guanyuan"
            },
            {
              "value": 222,
              "label": "fumen"
            },
            {
              "value": 117,
              "label": "Guanganmen"
            },
            {
              "value": 132,
              "label": "Yuetan"
            },
            {
              "value": 223,
              "label": "Taoran_Pavilion"
            },
            {
              "value": 163,
              "label": "Niujie"
            },
            {
              "value": 106,
              "label": "Xuanwumen"
            },
            {
              "value": 128,
              "label": "Xinjiekou"
            },
            {
              "value": 205,
              "label": "Xizhimen"
            },
            {
              "value": 195,
              "label": "Caihuying"
            },
            {
              "value": 218,
              "label": "Changchun_Street"
            },
            {
              "value": 201,
              "label": "Xidan"
            },
            {
              "value": 202,
              "label": "Xisi"
            },
            {
              "value": 68,
              "label": "Youanmennei"
            },
            {
              "value": 212,
              "label": "Chegongzhuang"
            },
            {
              "value": 95,
              "label": "Taiping_Bridge"
            },
            {
              "value": 122,
              "label": "Deshengmen"
            }
          ]
        },
        {
          "value": "a11",
          "label": "Haidian",
          "children": [
            {
              "value": 233,
              "label": "Madian"
            },
            {
              "value": 239,
              "label": "Weigong_Village"
            },
            {
              "value": 169,
              "label": "Ganjiakou"
            },
            {
              "value": 192,
              "label": "Suzhou_bridge"
            },
            {
              "value": 197,
              "label": "Xisanqi"
            },
            {
              "value": 186,
              "label": "Zizhuqiao"
            },
            {
              "value": 104,
              "label": "Dinghui_Temple"
            },
            {
              "value": 173,
              "label": "Baishiqiao"
            },
            {
              "value": 110,
              "label": "Xiaoxitian"
            },
            {
              "value": 7,
              "label": "Shangdi"
            },
            {
              "value": 128,
              "label": "Xinjiekou"
            },
            {
              "value": 16,
              "label": "Zhongguancun"
            },
            {
              "value": 25,
              "label": "Wukesong"
            },
            {
              "value": 2,
              "label": "Wanshou_Road"
            },
            {
              "value": 142,
              "label": "Yangzhuang"
            },
            {
              "value": 164,
              "label": "Peony_Garden"
            },
            {
              "value": 153,
              "label": "Haidian_North_New_District"
            },
            {
              "value": 37,
              "label": "Liuli_bridge"
            },
            {
              "value": 26,
              "label": "Wudaokou"
            },
            {
              "value": 3,
              "label": "Wanliu"
            },
            {
              "value": 36,
              "label": "princess_grave"
            },
            {
              "value": 98,
              "label": "Xueyuan_Road"
            },
            {
              "value": 154,
              "label": "Qinghe"
            },
            {
              "value": 8,
              "label": "Century_City"
            },
            {
              "value": 200,
              "label": "Xibeiwang"
            },
            {
              "value": 205,
              "label": "Xizhimen"
            },
            {
              "value": 176,
              "label": "Zaojun_Temple"
            },
            {
              "value": 167,
              "label": "Yuquan_Road"
            },
            {
              "value": 172,
              "label": "Tiancun"
            },
            {
              "value": 99,
              "label": "Anning_Village"
            },
            {
              "value": 152,
              "label": "Haidian_others"
            },
            {
              "value": 73,
              "label": "sijiqing"
            },
            {
              "value": 39,
              "label": "Junbo"
            },
            {
              "value": 234,
              "label": "malianwa"
            },
            {
              "value": 198,
              "label": "Xierqi"
            },
            {
              "value": 65,
              "label": "shuangyushu"
            },
            {
              "value": 229,
              "label": "Summer_Palace"
            },
            {
              "value": 178,
              "label": "Zhichun_Road"
            },
            {
              "value": 204,
              "label": "Xishan"
            },
            {
              "value": 49,
              "label": "Beitaipingzhuang"
            },
            {
              "value": 24,
              "label": "Erlizhuang"
            },
            {
              "value": 62,
              "label": "Changwa"
            },
            {
              "value": 78,
              "label": "Yuanmingyuan"
            }
          ]
        },
        {
          "value": "a10",
          "label": "Chaoyang",
          "children": [
            {
              "value": 233,
              "label": "Madian"
            },
            {
              "value": 80,
              "label": "kuatou"
            },
            {
              "value": 215,
              "label": "Jiuxianqiao"
            },
            {
              "value": 13,
              "label": "East_Bridge"
            },
            {
              "value": 133,
              "label": "Wangjing"
            },
            {
              "value": 147,
              "label": "Happy_Valley"
            },
            {
              "value": 137,
              "label": "Outside_Chaoyang_Gate"
            },
            {
              "value": 157,
              "label": "Pan_Jiayuan"
            },
            {
              "value": 28,
              "label": "Asian_Games_Village"
            },
            {
              "value": 55,
              "label": "Shilihe"
            },
            {
              "value": 185,
              "label": "Guanzhuang"
            },
            {
              "value": 124,
              "label": "Huixin_West_Street"
            },
            {
              "value": 72,
              "label": "Peace_Lane"
            },
            {
              "value": 210,
              "label": "dougezhuang"
            },
            {
              "value": 12,
              "label": "Dongba"
            },
            {
              "value": 115,
              "label": "Changying"
            },
            {
              "value": 179,
              "label": "shifoying"
            },
            {
              "value": 51,
              "label": "Beiyuan"
            },
            {
              "value": 56,
              "label": "Huawei_bridge"
            },
            {
              "value": 175,
              "label": "Baiziwan"
            },
            {
              "value": 190,
              "label": "shaoyaoju"
            },
            {
              "value": 50,
              "label": "Beijing_University_of_Technology"
            },
            {
              "value": 105,
              "label": "Dingfu_Village"
            },
            {
              "value": 101,
              "label": "Anzhen"
            },
            {
              "value": 138,
              "label": "Chaoqing"
            },
            {
              "value": 88,
              "label": "Dawang_road"
            },
            {
              "value": 29,
              "label": "Asian_Games_Village_Camp"
            },
            {
              "value": 77,
              "label": "National_Exhibition"
            },
            {
              "value": 64,
              "label": "double_bridge"
            },
            {
              "value": 187,
              "label": "Red_temple"
            },
            {
              "value": 125,
              "label": "Chengshou_Temple"
            },
            {
              "value": 63,
              "label": "shuangjing"
            },
            {
              "value": 171,
              "label": "Sweet_water_garden"
            },
            {
              "value": 203,
              "label": "Xiba_River"
            },
            {
              "value": 34,
              "label": "Jianxiangqiao"
            },
            {
              "value": 44,
              "label": "Jinsong"
            },
            {
              "value": 170,
              "label": "Manna_garden"
            },
            {
              "value": 40,
              "label": "Agricultural_Exhibition_Hall"
            },
            {
              "value": 33,
              "label": "Liangmaqiao"
            },
            {
              "value": 5,
              "label": "Sanyuanqiao"
            },
            {
              "value": 113,
              "label": "Gongti"
            },
            {
              "value": 59,
              "label": "south_Beach"
            },
            {
              "value": 74,
              "label": "Sihui"
            },
            {
              "value": 134,
              "label": "Chaoyang_Park"
            },
            {
              "value": 97,
              "label": "Olympic_Park"
            },
            {
              "value": 237,
              "label": "Gaobeidian"
            },
            {
              "value": 96,
              "label": "Sun_Palace"
            },
            {
              "value": 162,
              "label": "Yansha"
            },
            {
              "value": 53,
              "label": "Shilibao"
            },
            {
              "value": 86,
              "label": "Dashanzi"
            },
            {
              "value": 121,
              "label": "Outside_Jianguo"
            },
            {
              "value": 0,
              "label": "CBD"
            },
            {
              "value": 76,
              "label": "Tuanjie_Lake"
            },
            {
              "value": 129,
              "label": "Fangzhuang"
            },
            {
              "value": 14,
              "label": "Dongzhimen"
            },
            {
              "value": 6,
              "label": "Sanlitun"
            },
            {
              "value": 230,
              "label": "Capital_Airport"
            },
            {
              "value": 135,
              "label": "Chaoyang_others"
            },
            {
              "value": 118,
              "label": "Guangqumen"
            },
            {
              "value": 100,
              "label": "Andingmen"
            },
            {
              "value": 52,
              "label": "Shibalidian"
            },
            {
              "value": 17,
              "label": "Central_Villa"
            },
            {
              "value": 214,
              "label": "Tongzhou_Beiyuan"
            },
            {
              "value": 184,
              "label": "Lishui_bridge"
            }
          ]
        },
        {
          "value": "a15",
          "label": "Mentougou",
          "children": [
            {
              "value": 220,
              "label": "Mentougou_others"
            },
            {
              "value": 87,
              "label": "Dayu"
            },
            {
              "value": 82,
              "label": "Chengzi"
            },
            {
              "value": 41,
              "label": "Feng_Village"
            },
            {
              "value": 156,
              "label": "riverside_West"
            },
            {
              "value": 181,
              "label": "Shimen_camp"
            }
          ]
        },
        {
          "value": "a16",
          "label": "Shunyi",
          "children": [
            {
              "value": 227,
              "label": "Shunyi_others"
            },
            {
              "value": 228,
              "label": "Shunyi_City"
            },
            {
              "value": 231,
              "label": "Ma_Po"
            },
            {
              "value": 70,
              "label": "Houshayu"
            },
            {
              "value": 17,
              "label": "Central_Villa"
            },
            {
              "value": 141,
              "label": "Li_Qiao"
            },
            {
              "value": 230,
              "label": "Capital_Airport"
            }
          ]
        },
        {
          "value": "a4",
          "label": "Miyun",
          "children": [
            {
              "value": 144,
              "label": "Orchard_Street"
            },
            {
              "value": 155,
              "label": "Xiwengzhuang_Town"
            },
            {
              "value": 54,
              "label": "Shilibao_Town"
            },
            {
              "value": 66,
              "label": "Gubeikou_Town"
            },
            {
              "value": 244,
              "label": "Gulou_Streets"
            },
            {
              "value": 108,
              "label": "Miyun_Town"
            },
            {
              "value": 107,
              "label": "Miyun_others"
            }
          ]
        },
        {
          "value": "a9",
          "label": "Changping",
          "children": [
            {
              "value": 94,
              "label": "tiantongyuan"
            },
            {
              "value": 184,
              "label": "Lishui_bridge"
            },
            {
              "value": 75,
              "label": "Huiguan"
            },
            {
              "value": 243,
              "label": "Gulou_Street"
            },
            {
              "value": 45,
              "label": "Beiqijia"
            },
            {
              "value": 131,
              "label": "Changping_others"
            },
            {
              "value": 224,
              "label": "Huoying"
            },
            {
              "value": 150,
              "label": "Shahe"
            },
            {
              "value": 9,
              "label": "Dongguan"
            },
            {
              "value": 58,
              "label": "Nankou"
            },
            {
              "value": 199,
              "label": "Xiguan_Huandao"
            },
            {
              "value": 197,
              "label": "Xisanqi"
            },
            {
              "value": 60,
              "label": "Nanshao"
            },
            {
              "value": 99,
              "label": "Anning_Village"
            },
            {
              "value": 109,
              "label": "Xiaotangshan"
            }
          ]
        },
        {
          "value": "a3",
          "label": "Daxing",
          "children": [
            {
              "value": 130,
              "label": "Old_palace"
            },
            {
              "value": 238,
              "label": "Gaomi_shop"
            },
            {
              "value": 145,
              "label": "Jujube_Garden"
            },
            {
              "value": 241,
              "label": "Huangcunzhong"
            },
            {
              "value": 92,
              "label": "Tiangongyuan"
            },
            {
              "value": 206,
              "label": "Xihongmen"
            },
            {
              "value": 57,
              "label": "south_central_axis_airport_business_district"
            },
            {
              "value": 21,
              "label": "Yihezhuang"
            },
            {
              "value": 159,
              "label": "Yinghai"
            },
            {
              "value": 32,
              "label": "Others_in_Yizhuang_Development_Zone"
            },
            {
              "value": 208,
              "label": "Guanyin_Temple"
            },
            {
              "value": 242,
              "label": "Huangcun_railway_station"
            },
            {
              "value": 182,
              "label": "science_and_Technology_Park"
            },
            {
              "value": 31,
              "label": "Yizhuang"
            },
            {
              "value": 84,
              "label": "Daxing_new_airport"
            },
            {
              "value": 83,
              "label": "Daxing_others"
            },
            {
              "value": 71,
              "label": "Heyi"
            },
            {
              "value": 93,
              "label": "Tiangongyuan_South"
            },
            {
              "value": 85,
              "label": "daxing_new_airport_villa_area"
            }
          ]
        },
        {
          "value": "a2",
          "label": "Yizhuang",
          "children": [
            {
              "value": 32,
              "label": "Others_in_Yizhuang_Development_Zone"
            },
            {
              "value": 31,
              "label": "Yizhuang"
            },
            {
              "value": 236,
              "label": "majuqiao"
            }
          ]
        },
        {
          "value": "a14",
          "label": "Tongzhou",
          "children": [
            {
              "value": 214,
              "label": "Tongzhou_Beiyuan"
            },
            {
              "value": 23,
              "label": "jiukeshuCarrefour"
            },
            {
              "value": 146,
              "label": "pear_garden"
            },
            {
              "value": 19,
              "label": "Linheli"
            },
            {
              "value": 158,
              "label": "Lu_Yuan"
            },
            {
              "value": 148,
              "label": "Wuyi_Garden"
            },
            {
              "value": 47,
              "label": "Beiguan"
            },
            {
              "value": 143,
              "label": "Orchard"
            },
            {
              "value": 22,
              "label": "Qiaozhuang"
            },
            {
              "value": 213,
              "label": "Tongzhou_others"
            },
            {
              "value": 165,
              "label": "Jade_bridge"
            },
            {
              "value": 4,
              "label": "Wanda"
            },
            {
              "value": 236,
              "label": "majuqiao"
            }
          ]
        },
        {
          "value": "a6",
          "label": "Yanqing",
          "children": [
            {
              "value": 119,
              "label": "Yanqing_others"
            }
          ]
        },
        {
          "value": "a5",
          "label": "Pinggu",
          "children": [
            {
              "value": 116,
              "label": "Pinggu_others"
            }
          ]
        },
        {
          "value": "a7",
          "label": "Huairou",
          "children": [
            {
              "value": 123,
              "label": "Huairou"
            }
          ]
        }
      ],
      community:[]
    }
  },
  created(){
  },
  mounted() {
    this.initMap()
  },
  methods:{
    remoteMethod(query){
      this.loading=true
      searchCommunity({searchString:query}).then((res)=>{
        if(res.success){
          this.community=res.data.community
          this.loading=false
        }
      }).catch(()=>{
        this.loading=false
      })
    },
    findValueInDict(value,dict){
      if(dict=='region'){
        let res=global.region;
        for (let i in res) {
          if(res[i]===value){
            return i
          }
        }
      }else{
        let res=global.district;
        for (let i in res) {
          if(res[i]===value){
            return i
          }
        }
      }
      console.log('useend111111111111',dict)
    },
    initMap(){
      var _this=this;
      const map = L.map('map', {
      });
      L.Marker.prototype.options.icon = L.icon({
        iconUrl: icon,
        shadowUrl: iconShadow
      });
      map.locate({setView: true, maxZoom: 16});
      L.tileLayer(
          "http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
          {
            subdomains: ["1", "2", "3", "4"],
            attribution: "高德"
          }
      ).addTo(map);
      map.on('locationfound', (e)=>{
        console.log(e)
        L.marker(e.latlng).addTo(map).bindPopup("You are here at " + e.latlng.toString()).openPopup()
        _this.form.lng=e.latlng.lng;
        _this.form.lat =e.latlng.lat;
      });

      function onLocationError(e) {
          alert(e.message);
      }

      map.on('locationerror', onLocationError);

      var popup = L.popup();

      function onMapClick(e) {
        popup.setLatLng(e.latlng).setContent("You choose the coordinate of your house at " + e.latlng.toString()).openOn(map);
        _this.form.lng=e.latlng.lng;
        _this.form.lat =e.latlng.lat;
      }
      map.on('click', onMapClick);
    },

    onSubmit(){
      this.$refs['ruleForm'].validate((valid) => {
        if (valid) {
          let f={
            coordinate:[this.form.lng,this.form.lat],
            region:this.form.regionAndDistrict[0],
            district:this.form.regionAndDistrict[1],
            community:this.form.community,
          }
          this.$router.push({ name: 'HouseNum', params: { form: f }})
        }
      })
    },
  }
}
</script>

<style scoped>
@media (max-width: 768px) {
  .map-container{
    height:50%
  }
}
@media (min-width: 768px) {
  .map-container{
    height:100%
  }
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
    display: community;
    position: absolute;
    bottom: 10%;
    left: 0;
    height: 5px;
    width: 200%;
    background-color: #caa;
    background-image: linear-gradient(to right, #cc7575, #ffd544 50%, #cc7575);
    animation:colorLine 1s alternate infinite;
  }
  @keyframes colorLine
  {
    from {left:-100%;}
    to {left: 0}
  }
</style>
