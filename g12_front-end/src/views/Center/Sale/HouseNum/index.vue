<template>
  <div style="display: flex;height: 100%;flex-direction: column">
    <P class="center-title">Room number and the orientation</P>
    <el-row style="height: 100%" :gutter=20>
      <el-col :span=24>
        <div class="form-block">
          <el-form label-position="right" label-width="80px" :model="form">
            <el-row>
              <el-col  :span=12>
                <el-form-item label="hall">
                  <el-input-number v-model="form.hall"></el-input-number>
                </el-form-item>
              </el-col>
              <el-col :span=12>
                <el-form-item label="room">
                  <el-input-number v-model="form.room"></el-input-number>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span=12>
                <el-form-item label="kitchen">
                  <el-input-number v-model="form.kitchen"></el-input-number>
                </el-form-item>
              </el-col>
              <el-col :span=12>
                <el-form-item label="bathroom">
                  <el-input-number v-model="form.bathroom"></el-input-number>
                </el-form-item>
              </el-col>
              <el-form-item label="direction">
                <el-checkbox-group v-model="form.direction">
                  <el-col :span=6 v-for="(value,key) in direction" :key="value">
                    <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
                  </el-col>
                </el-checkbox-group>
              </el-form-item>
            </el-row>
            <el-row style="text-align: end;">
              <el-form-item>
                <el-button type="primary" @click="onSubmit" style="margin-right: 20px">N E X T</el-button>
              </el-form-item>
            </el-row>
          </el-form>
        </div>
      </el-col>
    </el-row>

  </div>

</template>

<script>
import global from '@/assets/global'

export default {
name: "index",
  data(){
    return{
      form:{
        hall: 0,
        room: 0,
        kitchen: 0,
        bathroom:0,
        direction:[]
      },
      direction:global.direction
    }
  },
  mounted() {
    this.$route.params.form?this.form=Object.assign(this.$route.params.form,this.form):
    console.log(this.form)
    console.log(this.direction)
  },
  methods:{
    onSubmit(){
      this.$router.push({ name: 'BaseInfo', params: { form: this.form }})
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