module.exports = {
//配置代码块
    //配置axios跨域请求
    devServer: {
        proxy: {
            '/api': { //访问路径，可以自己设置，
                target: 'http://127.0.0.1:5000/', //代理接口，即后端运行所在的端口
                changeOrigin: true, //设置是否跨域
                ws: true,
                pathRewrite: { //访问路径重写
                    '^/api': ''
                }
            }
        }
    }
}
