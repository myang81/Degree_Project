import Vue from 'vue'
import VueRouter from 'vue-router'
import index from '../views/index.vue'
import Login from '../views/Login/index'
import Register from '../views/Register/index'
import Show from '../views/Show/index'
import Detail from '../views/Detail/index'
import Center from '../views/Center/index'
import Target from '../views/Center/Target/index'
import UserDetail from '../views/Center/Detail/index'
import Collection from '../views/Center/Collection/index'
import Published from '../views/Center/Published/index'
import Sale from '../views/Center/Sale/index'
import Sale_Address from '../views/Center/Sale/Address/index'
import Sale_AdvanceInfo from '../views/Center/Sale/AdvanceInfo/index'
import Sale_BaseInfo from '../views/Center/Sale/BaseInfo/index'
import Sale_HouseNum from '../views/Center/Sale/HouseNum/index'
import Sale_TitleAndMoney from '../views/Center/Sale/TitleAndMoney/index'




Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: index
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
    component: Center,
    meta: {
      required: true,
    },
    children: [
      {
        path: '/',
        name: 'Target',
        component: Target
      },
      {
        path: 'target',
        name: 'Target',
        component: Target
      },
      {
        path: 'userDetail',
        name: 'UserDetail',
        component: UserDetail
      },
      {
        path: 'collection',
        name: 'Collection',
        component: Collection
      },
      {
        path: 'published',
        name: 'Published',
        component: Published
      },
      {
        path: 'sale',
        name: 'Sale',
        component: Sale,
        meta: {
          required: true,
        },
        children: [
          {
            path: 'address',
            name: 'Address',
            component: Sale_Address
          },
          {
            path: '/',
            name: 'Address',
            component: Sale_Address
          },
          {
            path: 'advanceInfo',
            name: 'AdvanceInfo',
            component: Sale_AdvanceInfo
          },
          {
            path: 'baseInfo',
            name: 'BaseInfo',
            component: Sale_BaseInfo
          },
          {
            path: 'houseNum',
            name: 'HouseNum',
            component: Sale_HouseNum
          },
          {
            path: 'titleAndMoney',
            name: 'TitleAndMoney',
            component: Sale_TitleAndMoney
          }
        ]
      }
    ]
  },
  {
    path: '/houseList',
    name: 'houseList',
    component: Show,
    meta: {
      required: true,
    }
  },
  {
    path: '/detail',
    name: 'detail',
    component: Detail,
    meta: {
      required: true,
    }
  },
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
