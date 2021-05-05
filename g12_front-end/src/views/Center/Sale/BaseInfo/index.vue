<template>
  <div>
    <div style="display: flex;height: 100%;flex-direction: column">
      <P class="center-title">Basic information</P>
      <b-row style="height: 100%" :gutter=20>
        <b-col :span=24>
          <div class="form-block">
            <el-form label-position="right" label-width="100px" :model="form" ref="ruleForm" :rules="rules">
              <b-row>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="area" style="text-align: left;" prop="area">
                    <b-form-input type="number" v-model="form.area" class="sale-form_numberInput"
                                  style="width: 70%"></b-form-input>
                    <span style="padding-left: 20px">m2</span>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="property" prop="property">
                    <el-radio-group v-model="form.property" style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" cols="12" v-for="(value,key) in global.propertyInfo"
                             :key="value">
                        <el-radio :label="value">{{ key }}</el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="house structure" prop="houseStructure">
                    <el-radio-group v-model="form.houseStructure"
                                    style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" lg="3" sm="6" cols="12"
                             v-for="(value,key) in global.house_structure" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="building type" prop="buildingType">
                    <el-radio-group v-model="form.buildingType" style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" lg="3" sm="6" cols="12"
                             v-for="(value,key) in global.building_type" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="building structure" prop="buildingStructure">
                    <el-radio-group v-model="form.buildingStructure"
                                    style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" lg="3" sm="6" cols="12"
                             v-for="(value,key) in global.building_structure" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="floor type" prop="floorType">
                    <el-radio-group v-model="form.floorType" style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" lg="3" sm="6" cols="12"
                             v-for="(value,key) in global.floor_type" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="Total floors" style="    text-align: left;" prop="floors">
                    <el-input-number v-model="form.floors" controls-position="right"></el-input-number>
                  </el-form-item>
                </b-col>
              </b-row>
              <b-col style="text-align: end" cols="12">
                <el-button type="primary" @click="onSubmit" style="width: 100%">N E X T</el-button>
              </b-col>
            </el-form>
          </div>
        </b-col>
      </b-row>

    </div>
  </div>
</template>

<script>
import global from '@/assets/global'

export default {
  name: "baseInfo",
  data() {
    return {
      form: {
        area:'',
        property: undefined,
        houseStructure: undefined,
        buildingType: undefined,
        buildingStructure: undefined,
        floorType: undefined,
        floors: undefined

      },
      rules: {
        area: [
          {required: true, message: 'please enter area', trigger: 'blur'},
        ],
        property: [
          {required: true, message: 'please choose property', trigger: 'blur'},
        ],
        houseStructure: [
          {required: true, message: 'please choose house structure', trigger: 'blur'},
        ],
        buildingType: [
          {required: true, message: 'please choose house type', trigger: 'blur'},
        ],
        buildingStructure: [
          {required: true, message: 'please choose building structure', trigger: 'blur'},
        ],
        floorType: [
          {required: true, message: 'please choose floor type', trigger: 'blur'},
        ],
        floors: [
          {required: true, message: 'please choose floor', trigger: 'blur'},
        ]
      },
      global: global,
    }
  },
  created() {
    this.$route.params.form?this.form=Object.assign(this.form,this.$route.params.form):this.$router.push({ name: 'Address'})


    console.log(this.form)
  },
  methods: {
    onSubmit() {
      this.$refs['ruleForm'].validate((valid) => {
        if (valid) {
          this.$router.push({name: 'AdvanceInfo', params: {form: this.form}})
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
<style>
.sale-form_numberInput {
  max-width: 150px;
  display: inline-block !important;
  text-align: center;
}
</style>
