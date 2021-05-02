<template>
  <div style="height: 100%;flex-direction: column">
    <P class="center-title">Choose your home address</P>
    <b-row style="height: 100%" :gutter=20>
      <b-col cols="12" md="6"  class="map-container">
        <div id="map" style="height: 100%;">
        </div>
      </b-col>
      <b-col cols="12" md="6">
        <div class="form-block">
          <el-form label-position="right" label-width="100px" :model="form" ref="ruleForm" :rules="rules">
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
              <!--            <b-col cols="12" md="6">-->
              <!--              <el-form-item label="district">-->
              <!--&lt;!&ndash;                <el-autocomplete v-model="form.district" :fetch-suggestions="querySearchDistrict"></el-autocomplete>&ndash;&gt;-->
              <!--                <el-cascader-->
              <!--                        v-model="value"-->
              <!--                        :options="options"-->
              <!--                        ></el-cascader>-->
              <!--              </el-form-item>-->
              <!--            </b-col>-->
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
/**
 * 未做表单验证
 * */
export default {
name: "address",
  data(){
    return {
      form:{
        regionAndDistrict:undefined,
        // coordinate:[undefined,undefined],
        lng:undefined,
        lat:undefined
      },
      rules: {
        regionAndDistrict: [
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
      ]
    }
  },
  created(){
    // let op=[{'value': 'a1', 'label': 1, 'children': [{'value': 209, 'label': 209}, {'value': 207, 'label': 207}, {'value': 61, 'label': 61}, {'value': 18, 'label': 18}, {'value': 127, 'label': 127}, {'value': 48, 'label': 48}, {'value': 129, 'label': 129}, {'value': 225, 'label': 225}, {'value': 102, 'label': 102}, {'value': 232, 'label': 232}, {'value': 194, 'label': 194}, {'value': 111, 'label': 111}, {'value': 1, 'label': 1}, {'value': 46, 'label': 46}, {'value': 211, 'label': 211}, {'value': 125, 'label': 125}, {'value': 139, 'label': 139}, {'value': 166, 'label': 166}, {'value': 37, 'label': 37}, {'value': 196, 'label': 196}, {'value': 42, 'label': 42}, {'value': 195, 'label': 195}, {'value': 95, 'label': 95}, {'value': 89, 'label': 89}, {'value': 191, 'label': 191}, {'value': 177, 'label': 177}, {'value': 20, 'label': 20}, {'value': 182, 'label': 182}, {'value': 71, 'label': 71}, {'value': 151, 'label': 151}, {'value': 27, 'label': 27}, {'value': 235, 'label': 235}, {'value': 25, 'label': 25}, {'value': 69, 'label': 69}, {'value': 130, 'label': 130}, {'value': 117, 'label': 117}, {'value': 206, 'label': 206}, {'value': 149, 'label': 149}]}, {'value': 'a8', 'label': 8, 'children': [{'value': 161, 'label': 161}, {'value': 219, 'label': 219}, {'value': 189, 'label': 189}, {'value': 221, 'label': 221}, {'value': 183, 'label': 183}, {'value': 168, 'label': 168}, {'value': 126, 'label': 126}, {'value': 226, 'label': 226}, {'value': 81, 'label': 81}]}, {'value': 'a12', 'label': 12, 'children': [{'value': 193, 'label': 193}, {'value': 220, 'label': 220}, {'value': 167, 'label': 167}, {'value': 240, 'label': 240}, {'value': 180, 'label': 180}, {'value': 35, 'label': 35}, {'value': 82, 'label': 82}, {'value': 142, 'label': 142}, {'value': 67, 'label': 67}, {'value': 188, 'label': 188}]}, {'value': 'a0', 'label': 0, 'children': [{'value': 79, 'label': 79}, {'value': 10, 'label': 10}, {'value': 14, 'label': 14}, {'value': 112, 'label': 112}, {'value': 113, 'label': 113}, {'value': 120, 'label': 120}, {'value': 72, 'label': 72}, {'value': 114, 'label': 114}, {'value': 100, 'label': 100}, {'value': 149, 'label': 149}, {'value': 15, 'label': 15}, {'value': 30, 'label': 30}, {'value': 160, 'label': 160}, {'value': 216, 'label': 216}, {'value': 118, 'label': 118}, {'value': 136, 'label': 136}, {'value': 101, 'label': 101}, {'value': 137, 'label': 137}, {'value': 223, 'label': 223}, {'value': 90, 'label': 90}, {'value': 11, 'label': 11}, {'value': 43, 'label': 43}, {'value': 196, 'label': 196}, {'value': 121, 'label': 121}]}, {'value': 'a13', 'label': 13, 'children': [{'value': 79, 'label': 79}, {'value': 233, 'label': 233}, {'value': 174, 'label': 174}, {'value': 217, 'label': 217}, {'value': 140, 'label': 140}, {'value': 38, 'label': 38}, {'value': 235, 'label': 235}, {'value': 91, 'label': 91}, {'value': 103, 'label': 103}, {'value': 222, 'label': 222}, {'value': 117, 'label': 117}, {'value': 132, 'label': 132}, {'value': 223, 'label': 223}, {'value': 163, 'label': 163}, {'value': 106, 'label': 106}, {'value': 128, 'label': 128}, {'value': 205, 'label': 205}, {'value': 195, 'label': 195}, {'value': 218, 'label': 218}, {'value': 201, 'label': 201}, {'value': 202, 'label': 202}, {'value': 68, 'label': 68}, {'value': 212, 'label': 212}, {'value': 95, 'label': 95}, {'value': 122, 'label': 122}]}, {'value': 'a11', 'label': 11, 'children': [{'value': 233, 'label': 233}, {'value': 239, 'label': 239}, {'value': 169, 'label': 169}, {'value': 192, 'label': 192}, {'value': 197, 'label': 197}, {'value': 186, 'label': 186}, {'value': 104, 'label': 104}, {'value': 173, 'label': 173}, {'value': 110, 'label': 110}, {'value': 7, 'label': 7}, {'value': 128, 'label': 128}, {'value': 16, 'label': 16}, {'value': 25, 'label': 25}, {'value': 2, 'label': 2}, {'value': 142, 'label': 142}, {'value': 164, 'label': 164}, {'value': 153, 'label': 153}, {'value': 37, 'label': 37}, {'value': 26, 'label': 26}, {'value': 3, 'label': 3}, {'value': 36, 'label': 36}, {'value': 98, 'label': 98}, {'value': 154, 'label': 154}, {'value': 8, 'label': 8}, {'value': 200, 'label': 200}, {'value': 205, 'label': 205}, {'value': 176, 'label': 176}, {'value': 167, 'label': 167}, {'value': 172, 'label': 172}, {'value': 99, 'label': 99}, {'value': 152, 'label': 152}, {'value': 73, 'label': 73}, {'value': 39, 'label': 39}, {'value': 234, 'label': 234}, {'value': 198, 'label': 198}, {'value': 65, 'label': 65}, {'value': 229, 'label': 229}, {'value': 178, 'label': 178}, {'value': 204, 'label': 204}, {'value': 49, 'label': 49}, {'value': 24, 'label': 24}, {'value': 62, 'label': 62}, {'value': 78, 'label': 78}]}, {'value': 'a10', 'label': 10, 'children': [{'value': 233, 'label': 233}, {'value': 80, 'label': 80}, {'value': 215, 'label': 215}, {'value': 13, 'label': 13}, {'value': 133, 'label': 133}, {'value': 147, 'label': 147}, {'value': 137, 'label': 137}, {'value': 157, 'label': 157}, {'value': 28, 'label': 28}, {'value': 55, 'label': 55}, {'value': 185, 'label': 185}, {'value': 124, 'label': 124}, {'value': 72, 'label': 72}, {'value': 210, 'label': 210}, {'value': 12, 'label': 12}, {'value': 115, 'label': 115}, {'value': 179, 'label': 179}, {'value': 51, 'label': 51}, {'value': 56, 'label': 56}, {'value': 175, 'label': 175}, {'value': 190, 'label': 190}, {'value': 50, 'label': 50}, {'value': 105, 'label': 105}, {'value': 101, 'label': 101}, {'value': 138, 'label': 138}, {'value': 88, 'label': 88}, {'value': 29, 'label': 29}, {'value': 77, 'label': 77}, {'value': 64, 'label': 64}, {'value': 187, 'label': 187}, {'value': 125, 'label': 125}, {'value': 63, 'label': 63}, {'value': 171, 'label': 171}, {'value': 203, 'label': 203}, {'value': 34, 'label': 34}, {'value': 44, 'label': 44}, {'value': 170, 'label': 170}, {'value': 40, 'label': 40}, {'value': 33, 'label': 33}, {'value': 5, 'label': 5}, {'value': 113, 'label': 113}, {'value': 59, 'label': 59}, {'value': 74, 'label': 74}, {'value': 134, 'label': 134}, {'value': 97, 'label': 97}, {'value': 237, 'label': 237}, {'value': 96, 'label': 96}, {'value': 162, 'label': 162}, {'value': 53, 'label': 53}, {'value': 86, 'label': 86}, {'value': 121, 'label': 121}, {'value': 0, 'label': 0}, {'value': 76, 'label': 76}, {'value': 129, 'label': 129}, {'value': 14, 'label': 14}, {'value': 6, 'label': 6}, {'value': 230, 'label': 230}, {'value': 135, 'label': 135}, {'value': 118, 'label': 118}, {'value': 100, 'label': 100}, {'value': 52, 'label': 52}, {'value': 17, 'label': 17}, {'value': 214, 'label': 214}, {'value': 184, 'label': 184}]}, {'value': 'a15', 'label': 15, 'children': [{'value': 220, 'label': 220}, {'value': 87, 'label': 87}, {'value': 82, 'label': 82}, {'value': 41, 'label': 41}, {'value': 156, 'label': 156}, {'value': 181, 'label': 181}]}, {'value': 'a16', 'label': 16, 'children': [{'value': 227, 'label': 227}, {'value': 228, 'label': 228}, {'value': 231, 'label': 231}, {'value': 70, 'label': 70}, {'value': 17, 'label': 17}, {'value': 141, 'label': 141}, {'value': 230, 'label': 230}]}, {'value': 'a4', 'label': 4, 'children': [{'value': 144, 'label': 144}, {'value': 155, 'label': 155}, {'value': 54, 'label': 54}, {'value': 66, 'label': 66}, {'value': 244, 'label': 244}, {'value': 108, 'label': 108}, {'value': 107, 'label': 107}]}, {'value': 'a9', 'label': 9, 'children': [{'value': 94, 'label': 94}, {'value': 184, 'label': 184}, {'value': 75, 'label': 75}, {'value': 243, 'label': 243}, {'value': 45, 'label': 45}, {'value': 131, 'label': 131}, {'value': 224, 'label': 224}, {'value': 150, 'label': 150}, {'value': 9, 'label': 9}, {'value': 58, 'label': 58}, {'value': 199, 'label': 199}, {'value': 197, 'label': 197}, {'value': 60, 'label': 60}, {'value': 99, 'label': 99}, {'value': 109, 'label': 109}]}, {'value': 'a3', 'label': 3, 'children': [{'value': 130, 'label': 130}, {'value': 238, 'label': 238}, {'value': 145, 'label': 145}, {'value': 241, 'label': 241}, {'value': 92, 'label': 92}, {'value': 206, 'label': 206}, {'value': 57, 'label': 57}, {'value': 21, 'label': 21}, {'value': 159, 'label': 159}, {'value': 32, 'label': 32}, {'value': 208, 'label': 208}, {'value': 242, 'label': 242}, {'value': 182, 'label': 182}, {'value': 31, 'label': 31}, {'value': 84, 'label': 84}, {'value': 83, 'label': 83}, {'value': 71, 'label': 71}, {'value': 93, 'label': 93}, {'value': 85, 'label': 85}]}, {'value': 'a2', 'label': 2, 'children': [{'value': 32, 'label': 32}, {'value': 31, 'label': 31}, {'value': 236, 'label': 236}]}, {'value': 'a14', 'label': 14, 'children': [{'value': 214, 'label': 214}, {'value': 23, 'label': 23}, {'value': 146, 'label': 146}, {'value': 19, 'label': 19}, {'value': 158, 'label': 158}, {'value': 148, 'label': 148}, {'value': 47, 'label': 47}, {'value': 143, 'label': 143}, {'value': 22, 'label': 22}, {'value': 213, 'label': 213}, {'value': 165, 'label': 165}, {'value': 4, 'label': 4}, {'value': 236, 'label': 236}]}, {'value': 'a6', 'label': 6, 'children': [{'value': 119, 'label': 119}]}, {'value': 'a5', 'label': 5, 'children': [{'value': 116, 'label': 116}]}, {'value': 'a7', 'label': 7, 'children': [{'value': 123, 'label': 123}]}];
    // for (let i = 0; i < op.length; i++) {
    //   op[i].label=this.findValueInDict(op[i].label,'district');
    //   for (let j = 0; j < op[i].children.length; j++) {
    //     op[i].children[j].label=this.findValueInDict(op[i].children[j].label,'region')
    //   }
    // }
    // console.log('op-----------------',op);
    // this.options=op
  },
  mounted() {
    this.initMap()
  },
  methods:{
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
  @keyframes colorLine
  {
    from {left:-100%;}
    to {left: 0}
  }
</style>
