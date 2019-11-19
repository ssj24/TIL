<template>
  <div>
    <!-- <h1>로그인 페이지입니다.</h1> -->
    <!-- <login-form></login-form> -->
    <LoginForm/>
  </div>
</template>

<script>
// import LoginForm from '../components/LoginForm'
// import LoginForm from '/src/components/LoginForm'
// @는 '/src'의 alias
import LoginForm from '@/components/LoginForm'
export default {
  name: 'login',
  components: {
    LoginForm,
  }, 
};
</script>

<style>
</style>