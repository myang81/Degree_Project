<template>
    <div>
        <HeaderNav></HeaderNav>
        <el-card class="card_login">
            <el-form ref="form" :model="form" >
                <el-form-item label="Name" label-width="80px">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="Password" label-width="80px">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item label="">
                    <el-checkbox label="remember your password?" name="type"></el-checkbox>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">Login</el-button>
                    <el-button>Sign Up</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
    import HeaderNav from '@/components/headerNav_logout/index.vue'

    export default {
        name: "login",
        components: {
            HeaderNav
        },
        data() {
            return {
                form:{},
            }
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
