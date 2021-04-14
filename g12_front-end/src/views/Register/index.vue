<template>
    <div>
        <HeaderNav :navContent="navContent"></HeaderNav>
        <el-card class="card_login">
            <el-form ref="form" :model="form" :rules="rules">
                <el-form-item label="Name" prop="name">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="Password" prop="password">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item label="Password-repeat" prop="prp">
                    <el-input v-model="form.prp"></el-input>
                </el-form-item>
                <el-form-item label="Email Address" prop="email">
                    <el-input v-model="form.email"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit()">Sign Up</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
    import HeaderNav from '@/components/headerNav/index.vue'

    export default {
        name: "register",
        components: {
            HeaderNav
        },
        data() {

            var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.form.prp !== '') {
            this.$refs.form.validateField('prp');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.form.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
            return {
                form:{
                    name:undefined,
                    password:undefined,
                    prp:undefined,
                    email:undefined

                },
                rules:{
                    name:[
                         { required: true, message: 'please enter username', trigger: 'blur' },
                        { min: 5, max: 12, message: '5-12', trigger: 'blur' }
                    ],
                     password: [
                        { validator: validatePass, trigger: 'blur' }
                      ],
                    prp: [
                       { validator: validatePass2, trigger: 'blur' }
                      ],
                },
              navContent:[{name:'Login',router:'/login'},{name:'Register',router:'/register'}]
            }

        },
        methods:{
            onSubmit() {
        this.$refs['form'].validate((valid) => {
          if (valid) {
            this.$router.push({name:'Login'})
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
.card_login{
    max-width: 500px;
    margin: 10vh auto;
    padding: 10px;
}
</style>
