<template>
  <div style="display: flex;height: 100%;flex-direction: column">
    <P class="center-title">Title and Money</P>
    <el-row style="height: 100%" :gutter=20>
      <el-col :span=24>
        <div class="form-block">
          <el-form label-position="right" label-width="80px" :model="form">
            <el-row>
              <el-form-item label="title">
                <el-input v-model="form.title"></el-input>
              </el-form-item>
            </el-row>
            <el-row>
              <el-col :span="12">
                <el-form-item label="unit-price">
                  <el-input v-model="form.unitPrice"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="total-price">
                  <el-input v-model="form.totalPrice"></el-input>
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
            <el-row style="text-align: end;">
              <el-form-item>
                <el-button type="primary" @click="onSubmit" style="margin-right: 20px">SUBMIT</el-button>
              </el-form-item>
            </el-row>
          </el-form>
        </div>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import global from "@/assets/global";

export default {
name: "index",
  data() {
    return {
      form: {
        decoration: [],
        heating: [],
        elevator: []
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
