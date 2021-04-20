import axios from 'axios'
import { MessageBox,Message } from 'element-ui'
import store from '../store'
import Vue from "vue/types/vue";
import router from '../router'

axios.defaults.headers['Content-Type'] = 'application/json;charset=utf-8';
// 创建axios实例
const service = axios.create({
    // axios中请求配置有baseURL选项，表示请求URL公共部分
    // '/api:': 'http://127.0.0.1:5000/',
    // 超时
    timeout: 10000,
});
// request拦截器
// service.interceptors.request.use(config => {
//     // 是否需要设置 token
// /*    const isToken = (config.headers || {}).isToken === false
//     if (getToken() && !isToken) {
//         config.headers['Authorization'] = 'Bearer ' + getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
//     }*/
//     return config
// }, error => {
//     console.log(error)
//     Promise.reject(error)
// });
// 响应拦截器
service.interceptors.response.use(res => {
    console.log("service.interceptors.response",res)
    // 未设置状态码则默认成功状态
    const code = res.success || 0;
    // 获取错误信息
    const message = res.error || 'network error'
/*    if (code === 401) {
        MessageBox.confirm(
            '登录状态已过期，您可以继续留在该页面，或者重新登录',
            '系统提示',
            {
                confirmButtonText: '重新登录',
                cancelButtonText: '取消',
                type: 'warning'
            }
        ).then(() => {
            store.dispatch('LogOut').then(() => {
                location.reload() // 为了重新实例化vue-router对象 避免bug
            })
        })
    } else if (code === 0) {
        Message({
            message: message,
            type: 'error'
        })
        return Promise.reject(new Error(message))
    } else if (code === 602) {
        return res.data
    } else if (code === 601) {
        return res.data
    } else if (code === 603) {
        return res.data
    } else if (code !== 0) {
        Notification.error({
            title: message
        })
        return Promise.reject('error')
    } else {
        return res.data
    }*/
        if (code === 401) {
            MessageBox.confirm(
                '登录状态已过期，您可以继续留在该页面，或者重新登录',
                '系统提示',
                {
                    confirmButtonText: '重新登录',
                    cancelButtonText: '取消',
                    type: 'warning'
                }
            ).then(() => {
                store.dispatch('LogOut').then(() => {
                    location.reload() // 为了重新实例化vue-router对象 避免bug
                })
            })
        } else if (code === 0) {
        Message({
            message: message,
            type: 'error'
        });
        return Promise.reject(new Error(message))
    }else {
        return res.data
    }
},
    error => {
        console.log('err' + error)
        Message({
            message: error.message,
            type: 'error',
            duration: 5 * 1000
        })
        return Promise.reject(error)
    }
)

// 路由跳转
router.beforeEach((to, from, next) => {
    if (to.meta.required) {
        // 检查localStorage
        if (localStorage.token) {
            store.commit('set_token', localStorage.token)
            // 添加axios头部Authorized
            axios.defaults.auth = {
                username: store.state.token,
                password: store.state.token,
            };
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

axios.defaults.baseURL = '/api'

export default service


