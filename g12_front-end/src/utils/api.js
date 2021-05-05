import axios from "./fetch";
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

export function getCollectionList(data){
    return axios({
        url:'/center/collection/getCollectionList',
        method:'post',
        data
    })
}

export function addCollection(data){
    return axios({
        url:'/addCollection',
        method:'post',
        data
    })
}

export function getPublishedList(data){
    return axios({
        url:'/center/published/getPublishedList',
        method:'post',
        data
    })
}

export function updateTargetInfo(data){
    return axios({
        url:'/center/target/updateTargetInfo',
        method:'post',
        data
    })
}

export function getTartgetInfo(data){
    return axios({
        url:'/center/target/getTargetInfo',
        method:'post',
        data
    })
}

export function delCollection(data){
    return axios({
        url:'/center/collection/delCollection',
        method:'post',
        data
    })
}

export function getDetail(data){
    return axios({
        url:'/detail/getHouseDetail',
        method:'post',
        data
    })
}

export function getsellerDetail(data){
    return axios({
        url:'/detail/getSellerDetail',
        method:'post',
        data
    })
}

export function getRecommended(data){
    return axios({
        url:'/recommendHouse',
        method:'post',
        data
    })
}

export function searchCommunity(data){
    return axios({
        url:'/returnCommunity',
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
    register,
    searchCommunity
    // del_collection
}
