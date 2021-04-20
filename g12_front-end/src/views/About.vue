<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
<script>
  import {getExample,apiV1} from '@/utils/api'

  export default {
    name: "index",
    data() {
      return {
        queryData:{
          option_A:0,
          option_B:1
        }
      }
    },
    created() {
      this.getTestData();
      this.getApiV1()
    },
    methods:{
      handleSearch(){
        this.$router.push({name:'houseList', params: { q: this.searchString }})
      },
      getTestData(){
        getExample(this.queryData).then(res=>{
          console.log('调用接口成功',res)
        })
      },
      getApiV1(){
        apiV1(this.queryData).then(res=>{
          console.log('调用接口成功',res)
        })
      }
    }
  }
</script>

