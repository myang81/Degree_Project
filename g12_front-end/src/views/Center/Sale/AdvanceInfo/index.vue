<template>
  <div style="display: flex;height: 100%;flex-direction: column">
    <P class="center-title">Advanced information</P>
    <el-row style="height: 100%" :gutter=20>
      <el-col :span=24>
        <div class="form-block">
          <el-form label-position="right" label-width="80px" :model="form">
            <el-row>
              <el-form-item label="decoration">
                <el-radio-group v-model="form.decoration" style="line-height: 50px;width: 100%">
                  <el-col :span=6 v-for="(value,key) in global.decoration" :key="value">
                    <el-radio :label="key" name="type" :value="value"></el-radio>
                  </el-col>
                </el-radio-group>
              </el-form-item>
            </el-row>
            <el-row>
              <el-form-item label="heating">
                <el-radio-group v-model="form.heating" style="line-height: 50px;width: 100%">
                  <el-col :span=6 v-for="(value,key) in global.heating" :key="value">
                    <el-radio :label="key" name="type" :value="value"></el-radio>
                  </el-col>
                </el-radio-group>
              </el-form-item>
            </el-row>
            <el-row>
              <el-form-item label="elevator">
                <el-radio-group v-model="form.elevator" style="line-height: 50px;width: 100%">
                  <el-col :span=6 v-for="(value,key) in global.elevator" :key="value">
                    <el-radio :label="key" name="type" :value="value"></el-radio>
                  </el-col>
                </el-radio-group>
              </el-form-item>
            </el-row>
            <el-row>
              <el-form-item label="rate">
                <el-row :gutter=30>
                  <el-col :span=11>
<!--                    <el-input-number v-model="form.elevatorNum"></el-input-number>-->
                    <b-form-input type="number" v-model="form.elevatorNum" class="sale-form_numberInput"></b-form-input><span style="padding-left: 20px">elevators</span>
<!--                    <span>elevator</span>-->
                  </el-col>
                  <el-col :span=11  >
<!--                    <el-input-number v-model="form.houseNum"></el-input-number>-->
                    <b-form-input type="number" v-model="form.houseNum" class="sale-form_numberInput"></b-form-input><span style="padding-left: 20px">houses</span>
<!--                    <span>house</span>-->
                  </el-col>
                </el-row>


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
import global from "@/assets/global";

export default {
  name: "index",
  data() {
    return {
      form: {
        decoration: undefined,
        heating: undefined,
        elevator: undefined,
        elevatorNum:undefined,
        houseNum:undefined
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
      this.$router.push({name: 'TitleAndMoney', params: {form: this.form}})
    }
  }
}
</script>

<style scoped>
.center-title {
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
  animation: colorLine 1s alternate infinite;
}

@keyframes colorLine {
  from {
    left: -100%;
  }
  to {
    left: 0
  }
}
</style>
