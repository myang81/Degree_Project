<template>
  <el-card class="check-block"
           :class="{'check-block_show':choiceCardVisible.more&&!choiceCardVisible.init,'check-block_hide':(!choiceCardVisible.more&&!choiceCardVisible.init)}">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="house structure" prop="houseStructure">
        <el-checkbox-group v-model="form.houseStructure">
          <el-col :span=6 v-for="(value,key) in global.house_structure" :key="value">
            <el-checkbox :label="key" name="type" :value="value"></el-checkbox>
          </el-col>
        </el-checkbox-group>
      </el-form-item>
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
      <div class="choice-card-bottom">
        <span class="cancel" @click="handleCancel">Cancel</span>
        <span class="confirm" @click="handleConfirm">Confirm</span>
      </div>
    </el-form>
  </el-card>
</template>

<script>
export default {
name: "index",
  props: {
    form: {type: Object},
    choiceCardVisible: {type: Object}
  },
  methods:{
    handleCancel(){
      this.$emit('handleCancel');
    },
    handleConfirm(){
      this.$emit('handleConfirm');
    }
  }
}
</script>

<style scoped>

.check-block {
  /*margin: 20px 10px;*/
  height: 0;
  box-shadow: 0 0;
  border: 0;
  /*width: 100%;*/
  width: calc(100% - 20px);
  position: absolute;
  z-index: 99;
  border-bottom: solid 1px rgba(0,0,0,0.1);
}

.check-block_show {
  animation: forwards showMore .4s;
}

.check-block_hide {
  animation: forwards hideMore .4s;
}
</style>