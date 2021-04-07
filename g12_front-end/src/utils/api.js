import axios from "axios";

export function testAxios(params){
    return axios({
        url:'/test',
        method:'get',
        params
    })
}

export default {
    testAxios
}
