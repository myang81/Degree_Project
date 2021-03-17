<template>
    <div style="padding: 0 10px">
        <HeaderNav></HeaderNav>
        <div style="">
<!--        <div class="search-block">
            <el-input
                    placeholder="Please input the house name, location, house type and other characteristics"
                    suffix-icon="el-icon-search"
                    v-model="searchValue"
                    class="input_search"
            >
            </el-input>
        </div>-->
        <el-card class="check-block">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="price">
                    <el-checkbox-group v-model="form.type">
                        <el-col :span="6">
                            <el-checkbox label="Less than 2 million" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="2-3.5 million" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="3.5-4.5 million" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="more than 4.5 million" name="type"></el-checkbox>
                        </el-col>
                    </el-checkbox-group>
                </el-form-item>

                <el-form-item label="layout">
                    <el-checkbox-group v-model="form.type">
                        <el-col :span="6">
                            <el-checkbox label="One room" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="Two room" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="Three room" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="Four rooms and above" name="type"></el-checkbox>
                        </el-col>
                    </el-checkbox-group>
                </el-form-item>

                <el-form-item label="measure">
                    <el-checkbox-group v-model="form.type">
                        <el-col :span="6">
                            <el-checkbox label="Less than 50 square meters" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="50-90 square meters" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="90-150 square meters" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="more than 150 square meters" name="type"></el-checkbox>
                        </el-col>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item label="orientation">
                    <el-checkbox-group v-model="form.type">
                        <el-col :span="6">
                            <el-checkbox label="North South orientation" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="East west orientation" name="type"></el-checkbox>
                        </el-col>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item label="floor">
                    <el-checkbox-group v-model="form.type">
                        <el-col :span="6">
                            <el-checkbox label="low" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="middle" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="high" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="top" name="type"></el-checkbox>
                        </el-col>
                    </el-checkbox-group>
                </el-form-item>

                <el-form-item label="decoration">
                    <el-checkbox-group v-model="form.type">
                        <el-col :span="6">
                            <el-checkbox label="Simple" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="Normal" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="high" name="type"></el-checkbox>
                        </el-col>
                        <el-col :span="6">
                            <el-checkbox label="luxury" name="type"></el-checkbox>
                        </el-col>
                    </el-checkbox-group>
                </el-form-item>
                <!--<el-form-item  style="text-align: right">
                    <el-button type="primary" @click="onSubmit" size="medium">S a v e</el-button>
                    &lt;!&ndash;                        <el-button>取消</el-button>&ndash;&gt;
                </el-form-item>-->
            </el-form>
        </el-card>
        <div class="main-block">
            <div class="sort-choice-block">
                <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
                    <el-tab-pane label="default" name="first"></el-tab-pane>
                    <el-tab-pane label="up-to-date" name="second"></el-tab-pane>
                    <el-tab-pane label="popular" name="third"></el-tab-pane>
                    <el-tab-pane label="cheapest" name="fourth"></el-tab-pane>
                </el-tabs>
            </div>
            <div class="list-block" v-for="(item,index) in houseList" :key="index" >
                <el-row class="house-item">
                    <el-col span="8">
                    <el-image class="item-img" :src=item.img></el-image>
                    </el-col>
                    <el-col span="12">
                    <div class="item-text">
                        <div class="item-name">{{item.name}}</div>
                        <div class="item-pos item-little"><i class="el-icon-position"> </i>{{item.pos}}</div>
                        <div class="item-details item-little"><i class="el-icon-s-home"> </i>{{item.detail}}</div>
                        <div class="item-collection item-little"><i class="el-icon-star-off"> </i>{{item.collection}}</div>
                    </div>
                    </el-col>
                    <el-col span="4" style="height: 100%">
                        <div class="item-price">3.5 <span style="color: red">million</span></div>
                    </el-col>
                </el-row>
            </div>
        </div>



        <div class="recommendation-carousel">
            <p class="recommendation-title">recommendation housing</p>
            <el-carousel :interval="4000" type="card" height="300px">
                <el-carousel-item v-for="(item,index) in recommendationList" :key="index" >
                    <!--                        <h3 class="medium" :style="{backgroundImage: item.image}">{{ item.name }}</h3>-->
                    <div  style="position: relative;width: 100%;height: 100%">
                        <el-image
                                src="https://cdn.homedit.com/wp-content/uploads/2014/05/minimalist-interior-design.jpg"
                                fit="cover"
                                style="width: 100%;height: 100%"
                        >
                        </el-image>
                        <p style="position: absolute;left: 10px;bottom: 0px;font-size: 1.5rem;background: rgba(84, 92, 100, 0.5);width: 100%;text-align: left;padding-left: 5%;color: white">{{item.name}}</p>
                    </div>
                </el-carousel-item>
            </el-carousel>
        </div>
        </div>
    </div>
</template>

<script>
    import HeaderNav from '@/components/headerNav_withSearch/index.vue'

    export default {
        name: "index",
        components:{
            HeaderNav
        },
        data(){
            return{
                recommendationList:[{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"},{name:"house1",image:"../assets/home_header_bg.jpg"}],
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                activeName: 'first',
                houseList: [{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'},{'name':'Xin\'anli fine decoration one bedroom owners sincerely sell','pos':'XINANLI Zaoyuan','detail':'1 room 2 halls | 51.56 square meters | North South | hardcover | top floor (6 floors in total) | built in 1997 | slab building','collection':139,'img':'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00277-440.jpg'}]
            }
        }
    }
</script>

<style scoped>
    .recommendation-carousel{
        width: 100%;
        padding: 10px 0;
    }
    .recommendation-carousel .recommendation-title{
        font-size: 1.8rem;
        color: rgba(84, 92, 100,1);
        text-align: left;
        padding: 10px 10px 10px 2%;
    }
    .check-block{
        margin: 20px 10px;
    }
    .main-block{
        background-color: white;
        max-width: 1200px; margin: 0 auto
    }
    .house-item{
        padding: 20px;
        border-bottom: 2px solid black;
        height: 260px;
    }
    .house-item .item-text{
        text-align: left;
        margin-left: 20px;
    }
    .house-item .item-name{
        font-weight: bold;
        font-size: 1.6rem;
        padding: 10px 0;
    }
    .house-item .item-little{
        line-height: 35px;
    }
    .house-item .item-price{
        font-weight: bold;
        font-size: 1.6rem;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
<style>
    .check-block .el-form-item{
        margin-bottom: 0;
    }
    .check-block .el-form-item__content,.check-block .el-form-item__label{
        line-height: 15px!important;
    }
    .check-block .el-form-item__content{
        text-align: left;
    }
</style>
