<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border text-primary" role="status">
      <span class="sr-only">Loading...</span>
      <!-- sr-only = screen reader only 시각장애인분들에게 알려준다. 
            div의 role도 sr을 위한 것-->
    </div>
    <form v-else class="login-form" @submit.prevent="login">
      <div v-if="errors.length" class="error-list alert alert-danger" role="alert">
        <h5>다음의 오류를 해결해주세요.</h5>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">
          {{ error }}
        </div>
      </div>


      <div class="form-group">
        <label for="id">ID</label>
        <input 
          type="text"
          class="form-control" 
          id="id" 
          placeholder="아이디를 입력해주세요."
          v-model="credentials.username"
          >
      </div>
      <div class="form-group">
        <label for="password">PASSWORD</label>
        <input 
          type="password" 
          class="form-control" 
          id="password" 
          placeholder="비밀번호를 입력해주세요."
          v-model="credentials.password"
          >
      </div>
      <button type="submit" class="btn btn-primary" @click="login">login</button>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  import router from '../router'

  export default {
    name: 'LoginForm',
    data() {//component의 data는 리턴이 함수
      return {
        credentials: {
          username: '',
          password: '',
        },
        // loading: false, // vuex
        errors: [],
      }
    },
    computed: {
      loading: function() {
        return this.$store.state.loading //modules는 생략 가능. auth.js만 있으니까 그것도 생략 가능
      }
    },
    methods: {
      login(){
      // console.log('Login button Clicked!!')
        if (this.checkForm()) {
          // this.loading = true //vuex
          this.$store.dispatch('startLoading')
          // console.log('로그인 성공')
          // this.loading = true
          // 1. django jwt를 생성하는 주소로 요청을 보냄
          // 이 때 post요청으로 보내야하며 사용자가 입력한 로그인 정보를 같이 넘겨야 함.
          // axios.get('http://127.0.0.1:8000', this.credentials) //django url. 쟝고는 8000 vue는 8080
          axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials) //django url. 쟝고는 8000 vue는 8080
          .then(res => {
            // this.$session.start() //vuex
            // this.$session.set('jwt', res.data.token) //vuex
            this.$store.dispatch('endLoading')
            this.$srore.dispatch('login', res.data.token)
            router.push('/') // index.js의 path를 가져온 것
            // 2. login 이후에 loading의 상태를 다시 false로 변경
            // 그래야 spinner가 계속 돌지 않고 로그인 폼을 받아 볼 수 있음.
            // this.loading = false
            // console.log(res)
          })
          .catch(err => {
            // 3. login 실패시 loading의 상태를 다시 false로 변경
            // this.loading = false // vuex
            this.$store.dispatch('endLoading')
            console.log(err)
          })
        } else {
          // console.log('로그인 실패')
          console.log('로그인 검증 실패')
        }
      },
      checkForm() {
        this.errors = []
        if (!this.credentials.username) {
          this.errors.push("아이디를 입력해주세요")
        }
        if (this.credentials.password.length < 8) {
          this.errors.push("비밀번호는 8자 이상 입력해주세요")
        }
        if (this.errors.length === 0) {
          return true
        }
      }
    }
  }
</script>

<style>

</style>