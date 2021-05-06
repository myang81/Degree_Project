<template>
  <div style="height: 100%;flex-direction: column">
    <P class="center-title">Advanced information</P>
    <b-row style="height: 100%;display: inline-block" cols="12">
      <div class="form-block">
        <el-form label-position="right" label-width="100px" :model="form" ref="ruleForm" :rules="rules">
          <b-col style="display: inline-block" cols="12">
            <el-form-item label="decoration" prop="decoration">
              <el-radio-group v-model="form.decoration" style="line-height: 50px;width: 100%;text-align: left">
                <b-col style="display: inline-block" lg="3" sm="6" cols="12" v-for="(value,key) in global.decoration"
                       :key="value">
                  <el-radio :label="value" :value="value">{{ key }}</el-radio>
                </b-col>
              </el-radio-group>
            </el-form-item>
          </b-col>
          <b-col style="display: inline-block" cols="12">
            <el-form-item label="heating" prop="heating">
              <el-radio-group v-model="form.heating" style="line-height: 50px;width: 100%;text-align: left">
                <b-col style="display: inline-block" lg="3" sm="6" cols="12" v-for="(value,key) in global.heating"
                       :key="value">
                  <el-radio :label="value" :value="value">{{ key }}</el-radio>
                </b-col>
              </el-radio-group>
            </el-form-item>
          </b-col>
          <b-col style="display: inline-block" cols="12">
            <el-form-item label="elevator" prop="elevator">
              <el-radio-group v-model="form.elevator" style="line-height: 50px;width: 100%;text-align: left">
                <b-col style="display: inline-block" lg="3" sm="6" cols="12" v-for="(value,key) in global.elevator"
                       :key="value">
                  <el-radio :label="value" :value="value">{{ key }}</el-radio>
                </b-col>
              </el-radio-group>
            </el-form-item>
          </b-col>
          <b-col style="display: inline-block" cols="12">
            <b-row :gutter=30 style="text-align: left;">
              <b-col style="display: inline-block" cols="12" sm="6">
                <el-form-item label="elevatorNum" prop="elevatorNum">
                  <b-form-input type="number" v-model="form.elevatorNum" class="sale-form_numberInput"
                                ></b-form-input>
                </el-form-item>
              </b-col>
              <b-col style="display: inline-block" cols="12" sm="6">
                <el-form-item label="houseNum" prop="houseNum">
                  <b-form-input type="number" v-model="form.houseNum"
                                class="sale-form_numberInput"></b-form-input>
                </el-form-item>

              </b-col>
            </b-row>
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
        houseNum: undefined,
      },
      global: global,
      rules: {
        decoration: [
          {required: true, message: 'please choose decoration type', trigger: 'blur'},
        ],
        heating: [
          {required: true, message: 'please choose heating type', trigger: 'blur'},
        ],
        elevator: [
          {required: true, message: 'is there an elevator?', trigger: 'blur'},
        ],
        elevatorNum: [
          {required: true, message: 'how many are there', trigger: 'blur'}
        ],
        houseNum: [
          {required: true, message: 'please choose house number', trigger: 'blur'}
        ]
      },
    }
  },
  mounted() {
    this.$route.params.form ? this.form = Object.assign(this.form, this.$route.params.form) : this.$router.push({name: 'Address'})
    console.log(this.form)
  },
  methods: {
    onSubmit() {
      this.$refs['ruleForm'].validate((valid) => {
        if (valid) {
          this.$router.push({name: 'TitleAndMoney', params: {form: this.form}})
        }
      })
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

.form-block {
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
