<template>
  <div>
    <div style="display: flex;height: 100%;flex-direction: column">
      <P class="center-title">Basic information</P>
      <el-row style="height: 100%" :gutter=20>
        <el-col :span=24>
          <div class="form-block">
            <el-form label-position="right" label-width="120px" :model="form">
              <el-row>
                  <el-col :span=12>
                      <el-form-item label="area">
                          <!--                    <el-input-number v-model="form.area" controls-position="right" ></el-input-number> m2-->
                          <b-form-input type="number" v-model="form.area" class="sale-form_numberInput"></b-form-input><span style="padding-left: 20px">m2</span>
                      </el-form-item>
                  </el-col>
                <el-col  :span=24 >
                  <el-form-item label="direction">
                    <el-radio-group v-model="form.property" style="line-height: 50px;width: 100%">
<!--                      <el-row style="display: flex;align-items: center">-->
                        <el-col :span=11  v-for="(value,key) in global.propertyInfo"  :key="value">
                          <el-radio :label="key" :value="value"></el-radio>
                        </el-col>
<!--                      </el-row>-->
                    </el-radio-group>
                  </el-form-item>
                </el-col>
                <el-col :span=24>
                  <el-form-item label="house structure">
                    <el-radio-group v-model="form.houseStructure" style="line-height: 50px;width: 100%">
                      <el-col :span=4 v-for="(value,key) in global.house_structure" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </el-col>
                    </el-radio-group>
                  </el-form-item>
                </el-col>
                <el-col :span=24>
                  <el-form-item label="building type">
                    <el-radio-group v-model="form.buildingType" style="line-height: 50px;width: 100%">
                      <el-col :span=4 v-for="(value,key) in global.building_type" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </el-col>
                    </el-radio-group>
                  </el-form-item>
                </el-col>
                <el-col :span=24>
                  <el-form-item label="building structure">
                    <el-radio-group v-model="form.buildingStructure" style="line-height: 50px;width: 100%">
                      <el-col :span=6 v-for="(value,key) in global.building_structure" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </el-col>
                    </el-radio-group>
                  </el-form-item>
                </el-col>
                <el-col :span=24>
                  <el-form-item label="floor type">
                    <el-radio-group v-model="form.floorType" style="line-height: 50px;width: 100%">
                      <el-col :span=6 v-for="(value,key) in global.floor_type" :key="value">
                        <el-radio :label="key" name="type" :value="value"></el-radio>
                      </el-col>
                    </el-radio-group>
                  </el-form-item>
                </el-col>
                <el-col :span=24>
                  <el-form-item label="Total floors" style="    text-align: left;">
                    <el-input-number v-model="form.floors" controls-position="right" ></el-input-number>
                  </el-form-item>
                </el-col>
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
  </div>
</template>

<script>
import global from '@/assets/global'

export default {
name: "baseInfo",
  data(){
    return{
      form:{
        property:"0",
        houseStructure:"0",

      },
      global:global,
    }
  },
  mounted() {
    this.$route.params.form?this.form=Object.assign(this.$route.params.form,this.form):
        console.log(this.form)
    console.log(this.direction)
  },
  methods:{
    onSubmit(){
      this.$router.push({ name: 'AdvanceInfo', params: { form: this.form }})
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
    .sale-form_numberInput{
        max-width: 150px;display: inline-block;text-align: center;
    }
</style>
