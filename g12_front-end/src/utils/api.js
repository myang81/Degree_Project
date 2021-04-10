import axios from "axios";
axios.defaults.baseURL = '/api'

export function getExample(params){
    return axios({
        url:'/getTest',
        method:'get',
        params
    })
}
export function postExample(params){
    return axios({
        url:'/postTest',
        method:'post',
        params
    })
}
export function apiV1(params){
    return axios({
        url:'/apiV1/home',
        method:'get',
        params
    })
}

export function login(params){
    return axios({
        url:'/apiV1/home',
        method:'post',
        params
    })
}



export default {
    getExample,
    postExample,
    apiV1,
    login
}
