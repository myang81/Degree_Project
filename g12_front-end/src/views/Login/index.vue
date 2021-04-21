<template>
    <div class="demo">

        <HeaderNav :navContent="navContent"></HeaderNav>
        <div class="main-agileits">
            <div class="form-w3-agile">
                <!--      <el-card class="card_login">-->
                <h1>Invincible Dragon Mars</h1><br><br>
                <el-form ref="form" :model="form" :rules="rules">
                    <el-form-item prop="name" label-width="80px">
                        <input placeholder="Username" v-model="form.userName"/>
                    </el-form-item>
                    <el-form-item prop="password" label-width="80px">
                        <input placeholder="Password" v-model="form.password"/>
                    </el-form-item>
                    <el-form-item label="">
                        <el-checkbox label="remember your password?" name="type" v-model="form.remember"></el-checkbox>
                    </el-form-item>
                    <el-form-item>
                        <div class="submit-w3l">
                            <!--                    <el-button type="primary" @click="onSubmit()">Login</el-button>-->
                            <!--                    <el-button>Sign Up</el-button>-->
<!--                            <input type="submit" value="Sign in" id="submit" @click="onSubmit()">-->

                            <el-button type="submit" value="Sign in" @click="onSubmit()">Sign in</el-button>
                        </div>
                    </el-form-item>
                </el-form>
                <!--        <img alt="Vue logo" src="../assets/pp.png">-->

                <!--        </el-card>-->
            </div>
        </div>
    </div>
</template>

<script>
    import HeaderNav from '@/components/headerNav/index.vue'
    import {login} from '@/utils/api'
    // import imgUrl from "../assets/test.png"

    export default {
        name: "login",
        components: {
            HeaderNav
        },
        data() {
            return {
                // imgUrl('../assets/pp.png'),
                form: {
                    userName: undefined,
                    password: undefined,
                    remember: undefined
                },
                rules: {
                    userName: [
                        {required: true, message: 'please enter username', trigger: 'blur'},
                        // {min: 5, max: 12, message: '5-12', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: 'please enter password', trigger: 'blur'},
                        // {min: 8, max: 15, message: '8-15', trigger: 'blur'}
                    ],

                },
                imgList: [
                    {
                        img: 'oo.jpg',
                        title: '测试'
                    }
                ],

                navContent: [{name: 'Login', router: '/login'}, {name: 'Register', router: '/register'}]

            }

        },
        methods: {
            onSubmit() {
                this.$refs['form'].validate((valid) => {
                    if (valid) {
                        login(this.form).then(res=>{
                            console.log(res)
                        })
                        // this.$router.push({name: 'index'})
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
        }
    }
</script>

<style scoped>
    /*.card_login{*/
    /*    height: 700px;*/
    /*    max-width: 500px;*/
    /*    margin: 20vh auto;*/
    /*    padding: 10px;*/
    /*}*/

    .demo {

        position: fixed;

        top: 0;

        left: 0;

        width: 100%;

        height: 100%;


        background: url(oo.jpg);

        background-repeat: no-repeat;

        background-size: cover;

        -webkit-background-size: cover;

        -o-background-size: cover;

        background-position: center 0;

    }

    /*test*/

    .main-agileits {
        width: 42%;
        margin: 0 auto;
        margin-top: 200px;
    }


    .form-w3-agile {
        background: rgba(41, 39, 39, 0.46);
        -webkit-box-shadow: 0px 35px 44px -22px rgba(0, 0, 0, 0.72);
        -moz-box-shadow: 0px 35px 44px -22px rgba(0, 0, 0, 0.72);
        box-shadow: 0px 35px 44px -22px #1f181b;
        padding: 60px 40px;
        /*text-align:center;*/
    }


    .form-w3-agile input {
        outline: none;
        font-size: 15px;
        color: #ffffff;
        text-align: left;
        padding: 12px 14px;
        width: 95.5%;
        border: none;
        border-bottom: 1px solid #889ba0;
        -webkit-appearance: none;
        margin-bottom: 30px;
        margin-left: -80px;
        background: transparent;

        letter-spacing: 1px;
    }


    .form-w3-agile h1 {
        color: #EBEEF5;
    }


    /*.submit-w3l input[type="submit"] {*/
    /*    background: #fff;*/
    /*    color: #000;*/
    /*    outline: none;*/
    /*    display: block;*/
    /*    margin: 0 auto;*/
    /*    border: none;*/
    /*    cursor: pointer;*/
    /*    padding: 13px 38px;*/
    /*    font-size: 14px;*/
    /*    width: 100%;*/
    /*    margin-top: 1em;*/
    /*    text-align: center;*/
    /*    font-weight: bold;*/
    /*    text-transform: uppercase;*/

    /*    transition: 0.3s all;*/
    /*    -webkit-transition: 0.3s all;*/
    /*    -moz-transition: 0.3s all;*/
    /*    -o-transition: 0.3s all;*/
    /*    -ms-transition: 0.3s all;*/
    /*}*/

    /*.submit-w3l input[type="submit"]:hover {*/
    /*    background: #3A5FCD;*/
    /*    color: #ffffff;*/
    /*    transition: 0.3s all;*/
    /*    -webkit-transition: 0.3s all;*/
    /*    -moz-transition: 0.3s all;*/
    /*    -o-transition: 0.3s all;*/
    /*    -ms-transition: 0.3s all;*/
    /*}*/

    input::-webkit-input-placeholder {
        color: #EBEEF5;
    }


    @media only screen and (max-width: 500px) {

    }


</style>













<style>
.submit-w3l .el-button {
        background: #fff;
        color: #000;
        outline: none;
        display: block;
        margin: 0 auto;
        border: none;
        cursor: pointer;
        padding: 13px 38px;
        font-size: 14px;
        width: 87%;
        margin-top: 1em;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;

        transition: 0.3s all;
        -webkit-transition: 0.3s all;
        -moz-transition: 0.3s all;
        -o-transition: 0.3s all;
        -ms-transition: 0.3s all;
    }

    .submit-w3l .el-button:hover {
        background: #3A5FCD;
        color: #ffffff;
        transition: 0.3s all;
        -webkit-transition: 0.3s all;
        -moz-transition: 0.3s all;
        -o-transition: 0.3s all;
        -ms-transition: 0.3s all;
    }










</style>
