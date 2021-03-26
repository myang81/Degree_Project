import Vue from 'vue'
import VueRouter from 'vue-router'
import index from '../views/index.vue'
import Login from '../views/Login/index'
import Register from '../views/Register/index'
import Center from '../views/Center/index'
import Show from '../views/Show/index'
import Detail from '../views/Detail/index'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: index
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/index',
    name: 'Index',
    component: index
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/center',
    name: 'Center',
    component: Center
  },
  {
    path: '/houseList',
    name: 'houseList',
    component: Show
  },
  {
    path: '/detail',
    name: 'detail',
    component: Detail
  },
]

const router = new VueRouter({
  routes
})

export default router
