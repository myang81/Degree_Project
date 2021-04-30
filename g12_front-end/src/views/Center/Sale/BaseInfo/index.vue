<template>
  <div>
    <div style="display: flex;height: 100%;flex-direction: column">
      <P class="center-title">Basic information</P>
      <b-row style="height: 100%" :gutter=20>
        <b-col :span=24>
          <div class="form-block">
            <el-form label-position="right" label-width="90px" :model="form">
              <b-row>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="area" style="text-align: left;">
                    <!--                    <el-input-number v-model="form.area" controls-position="right" ></el-input-number> m2-->
                    <b-form-input type="number" v-model="form.area" class="sale-form_numberInput"
                                  style="width: 70%"></b-form-input>
                    <span style="padding-left: 20px">m2</span>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="property">
                    <el-radio-group v-model="form.property" style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" cols="12" v-for="(value,key) in global.propertyInfo"
                             :key="value">
                        <el-radio :label="value">{{ key }}</el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="house structure">
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
                  <el-form-item label="building type">
                    <el-radio-group v-model="form.buildingType" style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" lg="3" sm="6" cols="12"
                             v-for="(value,key) in global.building_type" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="building structure">
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
                  <el-form-item label="floor type">
                    <el-radio-group v-model="form.floorType" style="line-height: 50px;width: 100%;text-align: left">
                      <b-col style="display: inline-block" lg="3" sm="6" cols="12"
                             v-for="(value,key) in global.floor_type" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </b-col>
                    </el-radio-group>
                  </el-form-item>
                </b-col>
                <b-col style="display: inline-block" cols="12">
                  <el-form-item label="Total floors" style="    text-align: left;">
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
        property: undefined,
        houseStructure: undefined,
        buildingType: undefined,
        buildingStructure: undefined,
        floorType: undefined,
        floors: undefined

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
      this.$router.push({name: 'AdvanceInfo', params: {form: this.form}})
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
