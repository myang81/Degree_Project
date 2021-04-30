<template>
  <div style="height: 100%;flex-direction: column">
    <P class="center-title">Advanced information</P>
    <b-row style="height: 100%;display: inline-block" cols="12">
      <div class="form-block">
        <el-form label-position="right" label-width="80px" :model="form">
          <b-col style="display: inline-block" cols="12">
            <el-form-item label="decoration">
              <el-radio-group v-model="form.decoration" style="line-height: 50px;width: 100%;text-align: left">
                <b-col style="display: inline-block" lg="3" sm="6" cols="12" v-for="(value,key) in global.decoration"
                       :key="value">
                  <el-radio :label="key" name="type" :value="value"></el-radio>
                </b-col>
              </el-radio-group>
            </el-form-item>
          </b-col>
          <b-col style="display: inline-block" cols="12">
            <el-form-item label="heating">
              <el-radio-group v-model="form.heating" style="line-height: 50px;width: 100%;text-align: left">
                <b-col style="display: inline-block" lg="3" sm="6" cols="12" v-for="(value,key) in global.heating"
                       :key="value">
                  <el-radio :label="key" name="type" :value="value"></el-radio>
                </b-col>
              </el-radio-group>
            </el-form-item>
          </b-col>
          <b-col style="display: inline-block" cols="12">
            <el-form-item label="elevator">
              <el-radio-group v-model="form.elevator" style="line-height: 50px;width: 100%;text-align: left">
                <b-col style="display: inline-block" lg="3" sm="6" cols="12" v-for="(value,key) in global.elevator"
                       :key="value">
                  <el-radio :label="key" name="type" :value="value"></el-radio>
                </b-col>
              </el-radio-group>
            </el-form-item>
          </b-col>
          <b-col style="display: inline-block" cols="12">
            <el-form-item label="rate">
              <b-row :gutter=30 style="text-align: left;">
                <b-col style="display: inline-block" cols="12" sm="6">
                  <b-form-input type="number" v-model="form.elevatorNum" class="sale-form_numberInput" style="width: 60%"></b-form-input>
                  <span style="padding-left: 20px">elevators</span>
                </b-col>
                <b-col style="display: inline-block" cols="12" sm="6">
                  <b-form-input type="number" v-model="form.houseNum" style="width: 60%"
                                class="sale-form_numberInput"></b-form-input>
                  <span style="padding-left: 20px">houses</span>
                </b-col>
              </b-row>
            </el-form-item>
          </b-col>
          <b-col style="text-align: end" cols="12">
            <el-button type="primary" @click="onSubmit" style="width: 100%">N E X T</el-button>
          </b-col>
        </el-form>
      </div>
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
        decoration: undefined,
        heating: undefined,
        elevator: undefined,
        elevatorNum: undefined,
        houseNum: undefined
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
.form-block{
  width: 100%;
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
