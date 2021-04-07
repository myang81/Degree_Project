<template>
  <div>
    <P class="center-title">Expected house type</P>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="price">
        <el-checkbox-group v-model="form.type">
          <el-col :span="8">
            <el-checkbox label="Less than 2 million" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="2-2.5 million" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="2.5-3 million" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="3-3.5 million" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="4-4.5 million" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="more than 4.5 million" name="type"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="layout">
        <el-checkbox-group v-model="form.type">
          <el-col :span="8">
            <el-checkbox label="One room" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="Two room" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="Three room" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="Four room" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="Five rooms and above" name="type"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="measure">
        <el-checkbox-group v-model="form.type">
          <el-col :span="8">
            <el-checkbox label="Less than 50 square meters" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="50-70 square meters" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="70-90 square meters" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="90-120 square meters" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="120-150 square meters" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="more than 150 square meters" name="type"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="orientation">
        <el-checkbox-group v-model="form.type">
          <el-col :span="8">
            <el-checkbox label="North South orientation" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="East west orientation" name="type"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="floor">
        <el-checkbox-group v-model="form.type">
          <el-col :span="8">
            <el-checkbox label="bottom" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="low" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="middle" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="high" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="top" name="type"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
      <el-divider></el-divider>
      <el-form-item label="decoration">
        <el-checkbox-group v-model="form.type">
          <el-col :span="8">
            <el-checkbox label="None" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="Simple" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="Normal" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="high" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="slap-up" name="type"></el-checkbox>
          </el-col>
          <el-col :span="8">
            <el-checkbox label="luxury" name="type"></el-checkbox>
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
export default {
  name: "Profit",
  data(){
    return{
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      navContent:[{name:'Renting',router:''},{name:'Purchase',router:'/'},{name:'Purchase',router:'/'},{name:'Publishing',router:'/'}]
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