<template>
  <div style="width: 100%;">
    <div class="top-picture">
      <el-carousel height="40vh" width="100%" @change="handlePicChange" ref="carousel">
        <el-carousel-item v-for="(item,index) in pictureList" :key="index">
          <el-image
              style="width: 100%; height: 100%"
              :src="item"
              fit="cover"></el-image>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="bottom-list">
      <div>
        <el-row :gutter=20>
          <div style="width: 20%;height: 100px;display: inline-block;padding: 10px" v-for="(item,index) in pictureList" :key="index">
            <el-image
                style="width: 100%; height: 100%"
                :src="item"
                fit="cover"
                :class="{'active':index===chosenIndex}"
                @click="handleChoosePic(index)"
                class="pic-choice"
            ></el-image>
          </div>
        </el-row>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "pictureScroll",
  props: {
    pictureList: Array,
  },
  data(){
    return{
      chosenIndex: 0,
    }
  },
  created() {
    console.log(this.pictureList)
  },
  methods:{
    handlePicChange(index){
      // console.log(index)
      this.chosenIndex=index
    },
    handleChoosePic(index){
      console.log(index)
      this.$refs.carousel.setActiveItem(index)
      this.chosenIndex=index
    }
  }
}
</script>

<style scoped>
.bottom-list{
  height: 80%;
  width: 100%;
}
.top-picture{
  width: 100%;
  height: 20%;
}
.pic-choice{
  width: 100%;
  height: 100%;
  filter: grayscale(100%);
}
.active{
  filter: grayscale(0%)!important;
}

</style>