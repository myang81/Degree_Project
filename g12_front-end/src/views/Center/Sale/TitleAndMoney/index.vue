<template>
  <div style="display: flex;height: 100%;flex-direction: column">
    <P class="center-title">Title and Price</P>
    <b-row style="height: 100%;width: 100%">
      <el-col :span=24>
        <div class="form-block">
          <el-form label-position="right" label-width="80px" :model="form">
            <el-row>
              <el-form-item label="title">
                <el-input v-model="form.title"></el-input>
              </el-form-item>
            </el-row>
            <el-row>
              <el-col :span="24">
                <el-form-item label="unit-price" style="text-align: left">
                  <el-input v-model="form.unitPrice" style="max-width: 200px;width: 60%" v-b-tooltip.hover title="The house price is predicted by the system algorithm, and the error is about 8000￥/m2"></el-input><span style="padding-left: 10px">￥/m2</span>
                </el-form-item>
              </el-col>
              <el-col :span="24">
                <el-form-item label="total-price" style="text-align: left">
                  <el-input v-model="form.totalPrice" style="max-width: 200px;width: 60%"></el-input><span style="padding-left: 10px">￥</span>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-form-item label="picture" style="text-align: left;">
                <el-upload
                    action="https://jsonplaceholder.typicode.com/posts/"
                    list-type="picture-card"
                    :on-preview="handlePictureCardPreview"
                    :before-upload="beforeAvatarUpload">
                  <i class="el-icon-plus"></i>
                </el-upload>
              </el-form-item>
            </el-row>
            <b-col style="text-align: end" cols="12">
                <el-button type="primary" @click="onSubmit" style="width: 100%">SUBMIT</el-button>
            </b-col>
          </el-form>
        </div>
      </el-col>
    </b-row>

  </div>
</template>

<script>
import global from "@/assets/global";

export default {
name: "index",
  data() {
    return {
      form: {
        title: '',
        unitPrice: '58957.51',
        totalPrice: '4447164.97'
      },
      global: global,
    }
  },
  mounted() {
    this.$route.params.form ? this.form = Object.assign(this.$route.params.form, this.form) :
        console.log(this.form)
    console.log(this.direction)
  },
  methods: {
    onSubmit() {
      // this.$router.push({name: 'TitleAndMoney', params: {form: this.form}})
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    }
  }
}
</script>

<style scoped>
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
<style>
  .tooltip-inner{
    max-width: 300px!important;
  }
</style>
