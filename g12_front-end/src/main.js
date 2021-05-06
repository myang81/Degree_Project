import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'leaflet/dist/leaflet.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VCalendar from 'v-calendar';
import store from './store'

Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VCalendar, {
  componentPrefix: 'vc',  // Use <vc-calendar /> instead of <v-calendar />
});


// 路由跳转
router.beforeEach((to, from, next) => {
  // console.log("localStorage.token",localStorage)
  if (store.state.token||localStorage) {  // 判断是否存在token，如果存在的话，则每个http header都加上token
    if(store.state.token==null) {
      store.commit('set_token', [localStorage.token,localStorage.userId])
    }
  }
  if (to.meta.required) {
    // 检查localStorage
    if (store.state.token) {
      // store.commit('set_token', localStorage.token)
      // // 添加axios头部Authorized
      // axios.defaults.auth = {
      //   username: store.state.token,
      //   password: store.state.token,
      // };
      // console.log("localStorage.token","put token into auth")
      // console.log("service.defaults.auth",axios)
      // iview的页面加载条
      // iView.LoadingBar.start();
      next()
    } else {
      next({
        path: '/login',
      })
    }
  } else {
    // iView.LoadingBar.start();
    next()
  }
})

// router.afterEach((to, from, next) => {
//     // iView.LoadingBar.finish();
// })

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
