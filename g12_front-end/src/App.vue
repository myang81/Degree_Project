<template>
  <div id="app">
<!--    <div id="nav">-->
<!--      <router-link to="/">Home</router-link> |-->
<!--      <router-link to="/about">About</router-link>-->
<!--    </div>-->
    <router-view/>
  </div>
</template>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
    overflow-x: hidden;
  height: 100vh;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
    body{
        margin: 0;
        background-color: #eeeef1;
    }
    p{
        margin: 0;
    }
a:hover {
  text-decoration: blink!important;
}
.ds-flex{
  display: flex;
}
.ds-ver_center{
  align-items: center;
}
p{
  margin-bottom: 0!important;
}
.full-width{
  width: 100%;
}
.mg-b-20{
  margin-bottom: 20px;
}
.mg-b-8{
  margin-bottom: 8px;
}
    .el-card{
        border-radius: 15px!important;
    }
.el-loading-spinner{
    display: inline;
}
img{
  border-radius: 10px!important;
  background: transparent!important;
}

html {
  font-size : 13px;
}
@media only screen and (min-width: 401px){
  html {
    font-size: 13px !important;
  }
}
@media only screen and (min-width: 428px){
  html {
    font-size: 13px !important;
  }
}
@media only screen and (min-width: 481px){
  html {
    font-size: 13px !important;
  }
}
@media only screen and (min-width: 569px){
  html {
    font-size: 14px !important;
  }
}
@media only screen and (min-width: 641px){
  html {
    font-size: 15px !important;
  }
}
</style>
