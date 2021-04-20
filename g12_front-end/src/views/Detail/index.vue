<template>
  <div>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
    <HeaderNav :navContent="navContent" show-search="true"></HeaderNav>
    <div style="background: #f5f5f6" class="head-container">
      <div style="max-width: 1200px;  margin: 0 auto;position: relative">
        <div class="title-block">
          {{ houseTitle }}
        </div>
        <div style="display: inline-block;position: absolute;bottom: calc(50% - 40px);right: 20px">
          <div class="buttons">
            <button class="blob-btn" @click="handleCollect">
              COLLECT <i :class="[collected?'el-icon-star-on':'el-icon-star-off']"></i>
              <span class="blob-btn__inner">
                <span class="blob-btn__blobs">
                  <span class="blob-btn__blob"></span>
                  <span class="blob-btn__blob"></span>
                  <span class="blob-btn__blob"></span>
                  <span class="blob-btn__blob"></span>
                </span>
              </span>
            </button>
          </div>
        </div>
        <!--        <el-button style="display: inline-block;position: absolute;bottom: calc(50% - 40px);right: 20px">-->
        <!--          collect <i class="el-icon-star-off"></i>-->
        <!--        </el-button>-->
      </div>
    </div>
    <div style="max-width: 1200px;  margin: 0 auto;">
      <div class="detail-container">
        <div class="detail-left">
          <div class="picture-div full-width mg-b-20">
            <pictureScroll :picture-list="pictureList"></pictureScroll>
          </div>
          <div class="chart-div full-width mg-b-20">

          </div>
          <div class="recommend-div full-width">
            <Recommendation></Recommendation>
          </div>
        </div>
        <div class="detail-right">
          <div class="price-div full-width mg-b-20">
            <el-card>
              <p><span style="font-size: 2rem">{{ totalPrice }}<span style="color: red">million</span></span><span
                  style="font-size: 1rem;color: gray;margin-left: 20px">{{ unitPrice }}￥/m2</span></p>
            </el-card>
          </div>
          <div class="detail-div full-width mg-b-20">
            <el-card style="color: gray">
              <el-row :gutter=20 v-for="(item,value) in houseDetail" :key="value" class="mg-b-8">
                <el-col :span=6>
                  <p style="color: black">{{ value }}: </p>
                </el-col>
                <el-col :span=18>
                  {{ item }}
                </el-col>
              </el-row>
            </el-card>
          </div>
          <div class="seller-div full-width mg-b-20">
            <el-card style="color: gray">
              <p style="color: black;font-size: 1.2rem;text-align: left;padding-bottom: 15px">Seller information</p>
              <el-row :gutter=20 v-for="(item,value) in sellerDetail" :key="value" class="mg-b-8">
                <el-col :span=6>
                  <p style="color: black">{{ value }}: </p>
                </el-col>
                <el-col :span=18>
                  {{ item }}
                </el-col>
              </el-row>
            </el-card>
          </div>
          <div class="buy-div full-width">
            BUY NOW
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/headerNav/index.vue'
import pictureScroll from '@/components/pictureScroll/index.vue'
import Recommendation from '@/components/RecommendationBlock/index.vue'

export default {
  name: "detail",
  components: {
    HeaderNav,
    pictureScroll,
    Recommendation
  },
  data() {
    return {
      houseId: '',
      navContent: [{name: 'Center', router: '/center'}, {
        name: 'Collection',
        router: '/center/collection'
      }, {name: 'Start to Sale', router: '/center/sale'}],
      pictureList: ['https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=1267115342,3426495198&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=632875621,3849475090&fm=26&fmt=auto&gp=0.jpg', 'https://img2.baidu.com/it/u=428922356,2955791946&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=1206287871,1293580609&fm=26&fmt=auto&gp=0.jpg'],
      houseDetail: {},
      houseTitle: 'The corner gate of Majiabao is close to the subway, with good north-south transparency, sufficient lighting and complete supporting facilities',
      unitPrice: '60203',
      totalPrice: '4.16',
      sellerDetail: {},
      collected: false,
    }
  },
  created() {
    if (this.$route.params.houseId) this.houseId = this.$route.params.houseId;
    this.getHouseDetail()
    this.getSellerDetail()
  },
  mounted() {
  },
  methods: {
    getHouseDetail() {
      this.houseDetail = {
        'describe': '2 room 1 halls | 69.1square meters | south north | Banlou | middle_floor ( total: 6 )',
        'position': 'Fengtai-Corner_Gate',
        'area': '123',
        'houseStructure': 'flat_floor',
        'direction': 'north,south',
        'decoration': 'rough',
        'heating': 'self_heating',
        'elevator': 'yes',
      }
    },
    getSellerDetail() {
      this.sellerDetail = {
        userName: 'sbLBJ',
        userEmail: 'LBJLBJLBG@sb.com',
        createTime: '1999-04-05'
      }
    },
    handleCollect(){
      this.collected=!this.collected
    },
  }

}
</script>
<style lang="scss">
*, *:before, *:after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

$openSans: 'Open Sans', Helvetica, Arial, sans-serif;
body {
  background: #333;
  font-family: $openSans;
}

.buttons {
  margin-top: 50px;
  text-align: center;
}

$cyan: #FF1493;
$dark: rgb(205, 205, 206);
$borderW: 6px;

.blob-btn {
  $numOfBlobs: 4;
  z-index: 1;
  position: relative;
  padding: 15px 20px;
  margin-bottom: 30px;
  text-align: center;
  text-transform: uppercase;
  color: $cyan;
  font-size: 16px;
  font-weight: bold;
  background-color: transparent;
  outline: none;
  border: none;
  transition: color 0.5s;
  cursor: pointer;

  &:before {
    content: "";
    z-index: 1;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    border: $borderW solid $cyan;
  }

  &:after {
    content: "";
    z-index: -2;
    position: absolute;
    left: $borderW*1.5;
    top: $borderW*1.5;
    width: 100%;
    height: 100%;
    border: $borderW solid $dark;
    transition: all 0.3s 0.2s;
  }

  &:hover {
    color: white;

    &:after {
      transition: all 0.3s;
      left: 0;
      top: 0;
    }
  }

  &__inner {
    z-index: -1;
    overflow: hidden;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
  }

  // additional container created, because in FF blobs are breaking overflow:hidden of element with svg gooey filter
  &__blobs {
    position: relative;
    display: block;
    height: 100%;
    filter: url('#goo');
  }

  &__blob {
    position: absolute;
    top: $borderW;
    width: 100% / $numOfBlobs;
    height: 100%;
    background: $cyan;
    border-radius: 100%;
    transform: translate3d(0, 150%, 0) scale(1.7);
    transition: transform 0.45s;

    @supports (filter: url('#goo')) {
      transform: translate3d(0, 150%, 0) scale(1.4);
    }

    @for $i from 1 through $numOfBlobs {
      &:nth-child(#{$i}) {
        left: ($i - 1) * (120% / $numOfBlobs);
        transition-delay: ($i - 1) * 0.08s;
      }
    }

    .blob-btn:hover & {
      transform: translateZ(0) scale(1.7);

      @supports (filter: url('#goo')) {
        transform: translateZ(0) scale(1.4);
      }
    }
  }

}
</style>

<style scoped>
.detail-container {
  flex-direction: row;
  display: flex;
  padding: 20px;
}

.detail-left {
  flex: 2;
  padding: 10px;
}

.detail-right {
  flex: 1;
  padding: 10px;
}

.title-block {
  font-size: 2rem;
  font-weight: bold;
  text-align: left;
  padding: 40px 20% 20px 10px;
  display: inline-block;
  /*text-overflow:ellipsis;*/
  /*white-space: nowrap;*/
}

.buy-div, .buy-div::after {
  font-size: 2.5rem;
  font-family: 'Bebas Neue', cursive;
  background: linear-gradient(45deg, transparent 5%, #FF013C 5%);
  border: 0;
  color: #fff;
  letter-spacing: 3px;
  box-shadow: 6px 0 0 #00E6F6;
  outline: transparent;
  position: relative;
  width: 100%;
  cursor: pointer;
}

.buy-div::after {
  --slice-0: inset(50% 50% 50% 50%);
  --slice-1: inset(80% -6px 0 0);
  --slice-2: inset(50% -6px 30% 0);
  --slice-3: inset(10% -6px 85% 0);
  --slice-4: inset(40% -6px 43% 0);
  --slice-5: inset(80% -6px 5% 0);
  font-weight: bold;
  content: 'Buy Now';
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent 3%, #00E6F6 3%, #00E6F6 5%, #FF013C 5%);
  text-shadow: -3px -3px 0px #F8F005, 3px 3px 0 #00E6F6;
  clip-path: var(--slice-0);
}

.buy-div:hover::after {
  animation: glitch 1s;
  animation-timing-function: steps(1, end);
}

@keyframes glitch {
  0% {
    clip-path: var(--slice-1);
    transform: translate(-20px, -10px);
  }

  10% {
    clip-path: var(--slice-3);
    transform: translate(10px, 10px);
  }

  20% {
    clip-path: var(--slice-1);
    transform: translate(-10px, 10px);
  }

  30% {
    clip-path: var(--slice-3);
    transform: translate(0px, 5px);
  }

  40% {
    clip-path: var(--slice-2);
    transform: translate(-5px, 0px);
  }

  50% {
    clip-path: var(--slice-3);
    transform: translate(5px, 0px);
  }

  60% {
    clip-path: var(--slice-4);
    transform: translate(5px, 10px);
  }

  70% {
    clip-path: var(--slice-2);
    transform: translate(-10px, 10px);
  }

  80% {
    clip-path: var(--slice-5);
    transform: translate(20px, -10px);
  }

  90% {
    clip-path: var(--slice-1);
    transform: translate(-10px, 0px);
  }

  100% {
    clip-path: var(--slice-1);
    transform: translate(0);
  }
}
</style>
