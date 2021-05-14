<template>
    <div class="demo">
        <HeaderNav :navContent="navContent"></HeaderNav>
      <div class="main-container">
        <div class="main-agileits">
          <div class="form-w3-agile">
            <h1>Invincible Dragon Mars</h1><br><br>
            <el-form ref="form" :model="form" :rules="rules">
              <el-form-item prop="name">
                <input placeholder="Username" v-model="form.name"/>
              </el-form-item>
              <el-form-item prop="password">
                <input placeholder="Password" v-model="form.password"/>
              </el-form-item>
              <el-form-item prop="prp">
                <input placeholder="Repeat Password" v-model="form.prp"/>
              </el-form-item>
              <el-form-item prop="email">
                <input placeholder="Email" v-model="form.email"/>
              </el-form-item>
              <el-form-item>
                <div class="submit-w3l">
                  <!--                    <input type="submit"  value="Register" id="submit" @click="onSubmit()">-->
                  <el-button type="submit" @click="onSubmit()">Register</el-button>
                </div>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </div>
    </div>


</template>

<script>
    import HeaderNav from '@/components/headerNav/index.vue'
    import {register} from '@/utils/api'

    export default {
        name: "register",
        components: {
            HeaderNav
        },
        data() {

            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('please enter passsword'));
                } else {
                    if (this.form.prp !== '') {
                        this.$refs.form.validateField('prp');
                    }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('please enter again'));
                } else if (value !== this.form.password) {
                    callback(new Error('different password entered'));
                } else {
                    callback();
                }
            };
            return {
                form: {
                    name: undefined,
                    password: undefined,
                    prp: undefined,
                    email: undefined

                },
                rules: {
                    name: [
                        {required: true, message: 'please enter username', trigger: 'blur'},
                        {min: 5, max: 12, message: 'please enter username with 5-12 letters', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: 'please enter password', trigger: 'blur'},
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    prp: [
                        {required: true, message: 'please repeat password', trigger: 'blur'},
                        {validator: validatePass2,message: 'different password entered', trigger: 'blur'}
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
                        register(this.form).then(res=>{
                            console.log('set_token',[res.data.token,res.data.userId]);
                            this.$store.commit('set_token', [res.data.token,res.data.userId]);
                          this.$router.push({name: 'index'})
                        })
                    } else {
                        console.log('error submit!!');
                    }
                });
            },

        }
    }
</script>

<style scoped>
.main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 45px);
}
    .card_login {
        max-width: 500px;
        margin: 10vh auto;
        padding: 10px;
    }

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
      max-width: 700px;
    }


    .form-w3-agile {
        background: rgba(41, 39, 39, 0.46);
        -webkit-box-shadow: 0px 35px 44px -22px rgba(0, 0, 0, 0.72);
        -moz-box-shadow: 0px 35px 44px -22px rgba(0, 0, 0, 0.72);
        box-shadow: 0px 35px 44px -22px #1f181b;
      padding: 3rem 2.5rem;
    }


    .form-w3-agile input {
        outline: none;
        font-size: 15px;
        color: #ffffff;
        text-align: left;
        padding: 12px 14px 5px 14px;
        width: 95.5%;
        border: none;
        border-bottom: 1px solid #889ba0;
        -webkit-appearance: none;
        margin-bottom: 10px;
        background: transparent;

        letter-spacing: 1px;
    }


    .form-w3-agile h1 {
        color: #EBEEF5;
      font-size: 3rem;
    }


    .submit-w3l input[type="submit"] {
        background: #fff;
        color: #000;
        outline: none;
        display: block;
        margin: 0 auto;
        border: none;
        cursor: pointer;
        padding: 13px 38px;
        font-size: 14px;
        width: 100%;
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

    .submit-w3l input[type="submit"]:hover {
        background: #42b983;
        color: #ffffff;
        transition: 0.3s all;
        -webkit-transition: 0.3s all;
        -moz-transition: 0.3s all;
        -o-transition: 0.3s all;
        -ms-transition: 0.3s all;
    }

    input::-webkit-input-placeholder {
        color: #EBEEF5;
    }


    @media only screen and (max-width: 500px) {
      .form-w3-agile h1 {
        color: #EBEEF5;
      font-size: 2rem;
    }



    }
</style>
