# g12_front-end 接口配置文档

## 创建接口
```
在utils/api.js中创建接口，参照已有例子即可
```

## 调用接口
```
详情参照About.vue中例子
```
### 引入接口
```
  import { XXX } from '@/utils/api'
    XXX为接口名
```

### 创建function
```
在methods中创建响应包装方法

      getTestData(){
        getExample(this.queryData//此处为要传递的参数).then(res=>{
          console.log('调用接口成功',res)
          //then 中是调用接口后的操作，通常使用res作为参数的箭头函数，res就是后端返回的数据
        })
      }
```
### 调用function
```
自行在create回调函数或点击函数等需要调用接口的地方引用function
```

### 验证查看network
```
你可以使用console.log来查看返回的值，
也可以在浏览器中f12-network中直接看接口，选中接口之后点预览/response可以看返回的值，在标头/header中可以看你传的参数
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
