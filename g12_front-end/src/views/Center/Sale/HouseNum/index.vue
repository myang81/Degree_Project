<template>
  <div style="height: 100%;flex-direction: column">
    <P class="center-title">Room number and the orientation</P>
        <div class="form-block">
          <el-form label-position="right" label-width="90px" :model="form" ref="ruleForm" :rules="rules">
            <b-row>
              <b-col  cols="12" sm="6">
                <el-form-item label="hall" prop="hall">
                  <el-input-number v-model="form.hall"></el-input-number>
                </el-form-item>
              </b-col>
              <b-col cols="12" sm="6">
                <el-form-item label="room" prop="room">
                  <el-input-number v-model="form.room"></el-input-number>
                </el-form-item>
              </b-col>
            </b-row>
            <b-row>
              <b-col cols="12" sm="6">
                <el-form-item label="kitchen" prop="kitchen">
                  <el-input-number v-model="form.kitchen"></el-input-number>
                </el-form-item>
              </b-col>
              <b-col cols="12" sm="6">
                <el-form-item label="bathroom" prop="bathroom">
                  <el-input-number v-model="form.bathroom"></el-input-number>
                </el-form-item>
              </b-col>
              <b-col cols="12">
              <el-form-item label="direction" prop="direction">
                <el-checkbox-group v-model="form.direction" style="text-align: left">
                  <b-col cols="6" sm="3" v-for="(value,key) in direction" :key="value" style="display: inline-block">
                    <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
                  </b-col>
                </el-checkbox-group>
              </el-form-item>
              </b-col>
            </b-row>
            <b-col style="text-align: end" cols="12">
                <el-button type="primary" @click="onSubmit" style="width: 100%">N E X T</el-button>
            </b-col>
          </el-form>
        </div>

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
      rules: {
        hall: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
        room: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
        kitchen: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
        bathroom: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
        direction: [
          {required: true, message: '请输入活动名称', trigger: 'blur'},
        ],
      },
      direction:global.direction
    }
  },
  created() {
    this.$route.params.form?this.form=Object.assign(this.$route.params.form,this.form):this.$router.push({ name: 'Address'})
    console.log(this.form)
  },
  methods:{
    onSubmit(){
      this.$refs['ruleForm'].validate((valid) => {
        if (valid) {
          this.$router.push({ name: 'BaseInfo', params: { form: this.form }})
        }
      })
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