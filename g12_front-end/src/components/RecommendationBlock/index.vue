<template>
  <div style="width: 100%">
    <p style="text-align: left;font-size: 1.5rem;margin: 0">Recommend high quality housing for you</p>
    <el-row :gutter="40">
      <el-col :span="8" v-for="(item,index) in recommendationList" :key="index">
        <el-card :body-style="{ padding: '20px'}" class="recommendation-card">
          <div class="img-container">
            <el-image
                src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg"
                fit="cover"
                style="width: 100%;height: 100%"
                class="img-content"
            >
            </el-image>
          </div>
          <div style="padding: 5px 5px 0 5px;text-align: left">
            <div class="bottom clearfix">
              <p style="margin: 0;color: #394043;font-size: 19px;font-weight: bold;;">{{ item.name }}</p>
              <p style="margin: 0; color: #394043;font-size: 14px;font-weight: bold;line-height: 1;">{{ item.unitPrice }}￥/m2</p>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {
      recommendationList: [{
        name: "house1",
        image: "../assets/home_header_bg.jpg",
        unitPrice: 52897
      }, {name: "house2", image: "../assets/home_header_bg.jpg", unitPrice: 60203}, {
        name: "house3",
        image: "../assets/home_header_bg.jpg",
        unitPrice: 59723
      }],
    }
  }
}
</script>

<style scoped>
.img-container{
  position:relative;
  width: 100%;
  height:0;
  padding-top:80%;
}
.img-content{
  position:absolute;
  top:0;
  left:0;
  width: 100%;
  height:100%;
}
</style>