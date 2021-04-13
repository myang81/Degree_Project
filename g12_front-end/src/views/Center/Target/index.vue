<template>
  <div>
    <P class="center-title">Expected house type</P>
    <el-form ref="form" :model="form" label-width="140px">
      <el-form-item label="totalPrice" prop="totalPrice">
        <el-row :gutter=20>
          <el-col :span=3 class="ds-flex">
            <el-input v-model="form.totalPrice[0]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥</span>
          </el-col>
          <el-col :span=17>
            <el-slider
                v-model="form.totalPrice"
                range
                :max="100000000">
            </el-slider>
          </el-col>
          <el-col :span=3 class="ds-flex">
            <el-input v-model="form.totalPrice[1]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥</span>
          </el-col>
        </el-row>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="unitPrice" prop="unitPrice">
        <el-row :gutter=20>
          <el-col :span=3 class="ds-flex">
            <el-input v-model="form.unitPrice[0]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥/m2</span>
          </el-col>
          <el-col :span=17>
            <el-slider
                v-model="form.unitPrice"
                range
                :max="1000000">
            </el-slider>
          </el-col>
          <el-col :span=3 class="ds-flex">
            <el-input v-model="form.unitPrice[1]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥/m2</span>
          </el-col>
        </el-row>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="area" prop="area">
        <el-row :gutter=20>
          <el-col :span=3 class="ds-flex">
            <el-input v-model="form.area[0]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">m2</span>
          </el-col>
          <el-col :span=17>
            <el-slider
                v-model="form.area"
                range
                :max="1000">
            </el-slider>
          </el-col>
          <el-col :span=3 class="ds-flex">
            <el-input v-model="form.area[1]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">m2</span>
          </el-col>
        </el-row>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="district" prop="district">
        <el-checkbox-group v-model="form.district">
          <el-col :span=6 v-for="(value,key) in global.district" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="house structure" prop="houseStructure">
        <el-checkbox-group v-model="form.houseStructure">
          <el-col :span=6 v-for="(value,key) in global.house_structure" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="direction" prop="direction">
        <el-checkbox-group v-model="form.direction">
          <el-col :span=6 v-for="(value,key) in global.direction" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="decoration" prop="decoration">
        <el-checkbox-group v-model="form.decoration">
          <el-col :span=6 v-for="(value,key) in global.decoration" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="heating" prop="heating">
        <el-checkbox-group v-model="form.heating">
          <el-col :span=6 v-for="(value,key) in global.heating" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="elevator" prop="elevator">
        <el-checkbox-group v-model="form.elevator">
          <el-col :span=6 v-for="(value,key) in global.elevator" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item  style="text-align: right">
        <el-button type="primary" @click="onSubmit" size="medium">S a v e</el-button>
        <!--                        <el-button>取消</el-button>-->
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import global from '@/assets/global'

export default {
  name: "Profit",
  data(){
    return{
      form: {
        totalPrice:[0,0],
        unitPrice:[0,0],
        area: [0,0],
        district:[],
        houseStructure:[],
        direction:[],
        decoration:[],
        heating:[],
        elevator:[],
      },
      // rules:{
      //   price: [
      //       { type: 'array', required: true, message: 'at least choose one', trigger: 'blur' }
      //     ],
      //    layout: [
      //       { type: 'array', required: true, message: 'at least choose one', trigger: 'change' }
      //     ],
      //    measure: [
      //       { type: 'array', required: true, message: 'at least choose one', trigger: 'change' }
      //     ],
      //    orientation: [
      //       { type: 'array', required: true, message: 'at least choose one', trigger: 'change' }
      //     ],
      //    floor: [
      //       { type: 'array', required: true, message: 'at least choose one', trigger: 'change' }
      //     ],
      //    decoration: [
      //       { type: 'array', required: true, message: 'at least choose one', trigger: 'change' }
      //     ],
      // },
      navContent:[{name:'Renting',router:''},{name:'Purchase',router:'/'},{name:'Purchase',router:'/'},{name:'Publishing',router:'/'}],
      global:global,
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