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
          <div :style="{height:height}" style="width: 20%;display: inline-block;padding: 10px" v-for="(item,index) in pictureList" :key="index">
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
    pictureList: {type:Array, default:()=>{
      return ['https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=1267115342,3426495198&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=632875621,3849475090&fm=26&fmt=auto&gp=0.jpg', 'https://img2.baidu.com/it/u=428922356,2955791946&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=1206287871,1293580609&fm=26&fmt=auto&gp=0.jpg']
      }},
    height: {type:String,default:'100px'}
  },
  data(){
    return{
      chosenIndex: 0,
    }
  },
  created() {
    console.log(this.pictureList)
    if(this.pictureList.length===0||this.pictureList[0]==="None"||this.pictureList[0]===""||typeof (this.pictureList)!=='object') {
      this.pictureList=['https://img1.baidu.com/it/u=1947907598,3262319172&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=1267115342,3426495198&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=632875621,3849475090&fm=26&fmt=auto&gp=0.jpg', 'https://img2.baidu.com/it/u=428922356,2955791946&fm=26&fmt=auto&gp=0.jpg', 'https://img1.baidu.com/it/u=1206287871,1293580609&fm=26&fmt=auto&gp=0.jpg']
      this.$forceUpdate()
    }
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
