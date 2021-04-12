<template>
  <div>
    <HeaderNav :navContent="navContent" show-search="true"></HeaderNav>
    <div>
      <div class="detail-container">
        <div class="detail-left">
          <div class="picture-div full-width mg-b-20">

          </div>
          <div class="chart-div full-width mg-b-20">

          </div>
          <div class="recommend-div full-width">

          </div>
        </div>
        <div class="detail-right">
          <div class="price-div full-width mg-b-20">

          </div>
          <div class="detail-div full-width mg-b-20">

          </div>
          <div class="seller-div full-width">

          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/headerNav/index.vue'

export default {
  name: "detail",
  components: {
    HeaderNav,
  },
  data() {
    return {
      houseId: '',
      navContent: [{name: 'Center', router: '/center'}, {
        name: 'Collection',
        router: '/center/collection'
      }, {name: 'Start to Sale', router: '/center/sale'}]
    }
  },
  created() {
    if (this.$route.params.houseId) this.houseId = this.$route.params.houseId
  },
  mounted() {
  },
  methods: {}
}
</script>

<style scoped>
.detail-container{
  max-width: 1200px;
  margin: 0 auto;
  flex-direction: row;
}
.detail-left{
  flex: 2;
  padding: 10px;
}
.detail-right{
  flex: 1;
  padding: 10px;
}
.full-width{
  width: 100%;
}
.mg-b-20{
  margin-bottom: 20px;
}
</style>
