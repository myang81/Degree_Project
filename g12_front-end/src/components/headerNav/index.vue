<template>
  <div class="home-header-nav">
    <div class="block_nav">
      <b-navbar toggleable="lg" type="dark" style="position: relative">
        <b-navbar-brand to="/" >IDM</b-navbar-brand>
          <div class="search-block" v-if="showSearch">
              <el-input
                      placeholder="Please input the house name, location, house type and other characteristics"
                      v-model="searchString"
                      class="input_search"
                      size="small"
              >
                  <el-button slot="append" icon="el-icon-search" size="small" @click="handleSearch"></el-button>
              </el-input>
          </div>
        <b-navbar-toggle target="nav-collapse">

        </b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
<!--          <div class="search-block" v-if="showSearch">-->
<!--            <el-input-->
<!--                placeholder="Please input the house name, location, house type and other characteristics"-->
<!--                v-model="searchString"-->
<!--                class="input_search"-->
<!--                size="small"-->
<!--            >-->
<!--              <el-button slot="append" icon="el-icon-search" size="small" @click="handleSearch"></el-button>-->
<!--            </el-input>-->
<!--          </div>-->
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-navbar-nav style="text-align: left" v-for="(item,index) in navContent" :key="index">
              <b-nav-item :to="item.router">{{item.name}}</b-nav-item>
            </b-navbar-nav>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
  </div>
</template>

<script>
export default {
  name: "index",
  props: {
    navContent: Array,
    showSearch: {type: Boolean, default: false},
    searchString: {type: String, default: ''}
  },
  data() {
    return {

    }
  },
  methods: {
    handleSearch() {
      console.log(this.$route);
      this.$route.path==='/houseList'?this.$emit('getSearch', this.searchString):this.$router.push({name: 'houseList', params: {searchString: this.searchString}})
    },
  }
}
</script>

<style scoped>
.home-header-nav{
  width: 100%;
  /*height: 60px;*/
  z-index: 9999;
}
.block_nav{
  background: rgba(84, 92, 100, 0.5);
  z-index: 9999;
}
.search-block{
  padding-left: 2%;
  justify-content: space-between;
  align-items: center;
  display: flex;
  width: 60vw;
  position: absolute;
  top: 0;
  padding-top: 12px;
  left: 50px;
}
</style>
<style>
.check-block .el-form-item {
  margin-bottom: 0;
}

.check-block .el-form-item__content, .check-block .el-form-item__label {
  line-height: 15px !important;
}

.check-block .el-form-item__content {
  text-align: left;
}

</style>
