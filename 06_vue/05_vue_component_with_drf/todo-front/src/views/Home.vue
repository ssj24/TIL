<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>Todo with Django</h1>
    <TodoInput @createTodo="createTodo"/>
    <TodoList :todos="todos"/> 
    <!-- 오른쪽이 넘길 데이터 왼쪽이 넘길 데이터 이름 -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'
import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex'

export default {
  name: 'home',
  components: {
    // HelloWorld
    TodoList,
    TodoInput,
  }, 
  data() {
    return {
      todos: [],
    }
  },
  computed: { 
    // ...은 spread 문법 -> 각각의 getters를 가져온다.
    // mapGetters 함수의 인자로 들어가는 배열에는 getters에서 정의한 함수들 중에서 가지고 오고 싶은 getter들을 작성한다.
    ...mapGetters([// 모든 게터를 쓸 경우. 배열이라서 ...으로 풀어준다.
      'isLoggedIn',
      'requestHeader',
      'userId'
    ]) 
  },
  methods: {
    checkLoggedIn() {
      // this.$session.start()
      // if (!this.$session.has('jwt')) {
      //   router.push('/login')
      // }
      if (!this.isLoggedIn) {
        router.push('/login')
      }
    },
    getTodos() {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
        // headers: {
          // Authorization: 'JWT ' + token
        // }
      // }
      // const user_id = jwtDecode(token).user_id
      // console.log(jwtDecode(token))
      // axios.get(`http://127.0.0.1:8000/api/v1/users/${user_id}/`, requestHeader)
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`, this.requestHeader)
        .then(res => {
          console.log(res)
          this.todos = res.data.todo_set
        })
        .catch(err => {
          console.log(err)
        })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      const requestForm = new FormData()
      // requestForm.append('user', user_id)
      requestForm.append('user', this.userId)
      requestForm.append('title', title) // createTodo의 인자가 title
      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, this.requestHeader)
        .then(res => {
          // console.log(res)
          this.todos.push(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  // DOM 에 Vue instance가 mount될 때마다 checkLoggedIn이 실행되어 로그인 여부를 체크 // 서버키면 바로 로그인 창이 뜨게 됨(Home에 로그인 안 되면 못 들어가니까)
  mounted() {
    this.checkLoggedIn()
    this.getTodos()
  },
}
</script>
