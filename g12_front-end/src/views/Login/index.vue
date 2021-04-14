<template>
    <div>
        <HeaderNav :navContent="navContent"></HeaderNav>
        <el-card class="card_login">
            <el-form ref="form" :model="form" :rules="rules" >
                <el-form-item label="Name" prop="name" label-width="80px">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="Password" prop="password" label-width="80px">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item label="">
                    <el-checkbox label="remember your password?" name="type"  v-model="form.remember"></el-checkbox>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit()">Login</el-button>
                    <el-button>Sign Up</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
    import HeaderNav from '@/components/headerNav/index.vue'
    // import {login} from '@/utils/api'
    export default {
        name: "login",
        components: {
            HeaderNav
        },
        data() {
            return {
                form:{
                   name:undefined,
                   password:undefined,
                    remember:undefined
                },
                rules:{
                    name:[
                         { required: true, message: 'please enter username', trigger: 'blur' },
                        { min: 5, max: 12, message: '5-12', trigger: 'blur' }
                    ],
                     password: [
                        { required: true, message: 'please enter password', trigger: 'blur' },
                        { min: 8, max: 15, message: '8-15', trigger: 'blur' }
                      ],

                },

              navContent:[{name:'Login',router:'/login'},{name:'Register',router:'/register'}]

            }

        },
        methods:{
            onSubmit() {
                    this.$refs['form'].validate((valid) => {
                      if (valid) {
                       this.$router.push({name:'index'})
                      } else {
                        console.log('error submit!!');
                        return false;
                      }
                    });
                  },



            // onSubmit(){
            //     login(this.form.validate).then((res)=>{
            //         console.log(res);
            //         if(res){
            //             this.$router.push({name:'index'})
            //         }
            //
            //
            //
            //     })
            // },
        }
    }
</script>

<style scoped>
.card_login{
    max-width: 500px;
    margin: 20vh auto;
    padding: 10px;
}
</style>
