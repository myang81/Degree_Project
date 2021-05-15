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
        /*background-color: #eeeef1;*/
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
.sold-cover{
  width: 100%;
  height: 100%;
  position: absolute;
  background: rgba(0,0,0,0.3);
  top: 0;
  left: 0;
  z-index: 200;
}
.sold-cover::after{
  content: 'SOLD';
  right: 0;
  bottom: 10%;
  position: absolute;
  font-size: 3.5rem;
  transform: rotate(-45deg);
  font-weight: bold;
}
.full-width{
  width: 100%;
}
.mg-b-20{
  margin-bottom: 20px!important;
}
.mg-b-8{
  margin-bottom: 8px;
}
.ds-none{
  display: none;
}
.oneline-text{
  overflow: hidden;text-overflow: ellipsis;white-space: nowrap;
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
