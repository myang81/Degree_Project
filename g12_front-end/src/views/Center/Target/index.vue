<template>
  <div>
    <P class="center-title">Expected house type</P>
    <el-form ref="form" :model="form" label-width="140px" class="center-form">
      <el-form-item label="totalPrice" prop="totalPrice">
        <b-row>
          <b-col cols=2 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
            <el-input v-model="form.totalPrice[0]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥</span>
          </b-col>
          <b-col v-if="this.screenWidth >= 768" cols=8>
            <el-slider
                v-model="form.totalPrice"
                range
                :step="100000"
                :max="100000000">
            </el-slider>
          </b-col>
          <b-col v-if="this.screenWidth < 768" cols=12>
            <el-slider
                v-model="form.totalPrice"
                range
                :step="100000"
                :max="100000000">
            </el-slider>
          </b-col>
          <b-col cols=2 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
            <el-input v-model="form.totalPrice[1]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥</span>
          </b-col>
        </b-row>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="unitPrice" prop="unitPrice">
        <b-row>
          <b-col cols=2 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
            <el-input v-model="form.unitPrice[0]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥/m2</span>
          </b-col>
          <b-col v-if="this.screenWidth >= 768" cols=8>
            <el-slider
                v-model="form.unitPrice"
                range
                :step="1000"
                :max="200000">
            </el-slider>
          </b-col>
          <b-col v-if="this.screenWidth < 768" cols=12>
            <el-slider
                v-model="form.unitPrice"
                range
                :step="1000"
                :max="200000">
            </el-slider>
          </b-col>
          <b-col cols=2 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
            <el-input v-model="form.unitPrice[1]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">￥/m2</span>
          </b-col>
        </b-row>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="area" prop="area">
        <b-row>
          <b-col cols=2 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
            <el-input v-model="form.area[0]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">m2</span>
          </b-col>
          <b-col v-if="this.screenWidth >= 768" cols=8>
            <el-slider
                v-model="form.area"
                range
                :step="100"
                :max="1000">
            </el-slider>
          </b-col>
          <b-col v-if="this.screenWidth < 768" cols=12>
            <el-slider
                v-model="form.area"
                range
                :max="1000">
            </el-slider>
          </b-col>
          <b-col cols=2 class="ds-flex" :class="{'ds-none':this.screenWidth < 768}">
            <el-input v-model="form.area[1]" style="flex: 2" type="text"></el-input>
            <span style="margin-left: 10px">m2</span>
          </b-col>
        </b-row>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="district" prop="district">
        <el-checkbox-group v-model="form.district">
          <b-row>
          <b-col cols=6 md=3 v-for="(value,key) in global.district" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </b-col>
          </b-row>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="house structure" prop="houseStructure">
        <el-checkbox-group v-model="form.houseStructure">
          <b-row>
          <b-col cols=6 md=3 v-for="(value,key) in global.house_structure" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </b-col>
          </b-row>
        </el-checkbox-group>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="direction" prop="direction">
        <el-checkbox-group v-model="form.direction">
          <b-row>
          <b-col cols=6 md=3 v-for="(value,key) in global.direction" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </b-col>
          </b-row>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="decoration" prop="decoration">
        <el-checkbox-group v-model="form.decoration">
          <b-row>
          <b-col cols=6 md=3 v-for="(value,key) in global.decoration" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </b-col>
          </b-row>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="heating" prop="heating">
        <el-checkbox-group v-model="form.heating">
          <b-col cols=6 md=3 v-for="(value,key) in global.heating" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </b-col>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="elevator" prop="elevator">
        <el-checkbox-group v-model="form.elevator">
          <b-col cols=6 md=3 v-for="(value,key) in global.elevator" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </b-col>
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
import {updateTargetInfo} from '@/utils/api'
import {getTartgetInfo} from '@/utils/api'

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
      screenWidth: document.body.clientWidth,

    }

  },
  created() {
            // console.log(this.$route.params)
            console.log("--------userId--------", this.$store.state.userId)
            this.getList()
        },
  mounted() {
    window.onresize = () => {
      return (() => {
        window.screenWidth = document.body.clientWidth
        this.screenWidth = window.screenWidth
      })()
    };
  },

  methods: {
            deldiv: function () {
                var obj = document.getElementById('div2');
                obj.parentNode.removeChild(obj);
            },

    getList() {
                console.log("--------userId--------", this.$store.state)
                getTartgetInfo({userId: this.$store.state.userId}).then(res => {
                       if (res.success) {
                        this.totalPriceRange = res.data.totalPriceRange;
                        this.unitPriceRange = res.data.unitPriceRange;
                        this.area = res.data.area;
                        this.district = res.data.district;
                        this.houseStructure = res.data.houseStructure;
                        this.direction = res.data.direction;
                        this.decoration = res.data.decoration;
                        this.heating = res.data.heating;
                        this.elevator = res.data.elevator;
                    }
                    })
            },




          postList() {
              let f=this.form
              f.userId=this.$store.state.userId
                updateTargetInfo(this.form).then(res => {
                       console.log(res);
                       // updateTargetInfo(this.form)

                    })
            },
          onSubmit(){
              this.postList()
          }
        },
  maijia: 'liangbj0405'





}
</script>

<style scoped>
.ds-none{
  display: none;
}
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
<style>
@media (min-width: 768px) {

}

@media (max-width: 768px) {
  .center-form .el-form-item label{
    width: 100%;
    text-align: left;
    font-weight: bold;
  }
  .center-form .el-form-item .el-form-item__content{
    margin-left: 0!important;
  }
  .center-form .el-form-item .row{
    width: 100%;
    margin-left: 0px;
  }
}
</style>