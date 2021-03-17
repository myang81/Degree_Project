<template>
    <div>
        <HeaderNav></HeaderNav>
        <el-card class="card_login">
            <el-form ref="form" :model="form" >
                <el-form-item label="Name">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="Password">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item label="Password-repeat">
                    <el-input v-model="form.passwordRe"></el-input>
                </el-form-item>
                <el-form-item label="Email Address">
                    <el-input v-model="form.password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">Sign Up</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
    import HeaderNav from '@/components/headerNav_logout/index.vue'

    export default {
        name: "register",
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
    margin: 10vh auto;
    padding: 10px;
}
</style>
