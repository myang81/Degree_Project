import axios from "axios";
axios.defaults.baseURL = '/api'

export function getExample(params){
    return axios({
        url:'/getTest',
        method:'get',
        params
    })
}
export function postExample(data){
    return axios({
        url:'/postTest',
        method:'post',
        data
    })
}
export function apiV1(params){
    return axios({
        url:'/apiV1/home',
        method:'get',
        params
    })
}

export function login(data){
    return axios({
        url:'/login',
        method:'post',
        data
    })
}

export function register(data){
    return axios({
        url:'/register',
        method:'post',
        data
    })
}

export function getHouseList(data){
    return axios({
        url:'/getHouseList',
        method:'post',
        data
    })
}


export default {
    getExample,
    postExample,
    apiV1,
    login,
    getHouseList,
    register
}
