<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body">
        <span @click="updateTodo(todo)" :class="{ complete: todo.completed}"> {{ todo.title }} </span>
        <span @click="deleteTodo(todo)">x</span>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name:'TodoList',
    props: {
      todos: {
        type: Array,
        required: true,
      }
    },
    computed: {
      requestHeader: function() {
        return this.$store.getters.requestHeader
      }
    },
    methods: {
      deleteTodo(todo) { // 이미 for문이 돌고 있어서..! decode는 필요없음
        // this.$session.start()
        // const token = this.$session.get('jwt')
        // const requestHeader = {
        //   headers: {
        //     Authorization: 'JWT ' + token
        //   }
        // } //vuex
        axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, this.requestHeader) //computed의 requestheader를 가져온다.
          .then(res => {
            console.log(res)
            const targetTodo = this.todos.find(function(el) { // vue의 화면 반영을 위해
              return el === todo
            })
            const idx = this.todos.indexOf(targetTodo)
            if (idx > -1) {
              this.todos.splice(idx, 1)
            }
          })
          .catch(err => {
            console.log(err)
          })
      },
      updateTodo(todo) {
        // this.$session.start()
        // const token = this.$session.get('jwt')
        // const requestHeader = {
        //   headers: {
        //     Authorization: 'JWT ' + token
        //   }
        // }
        const requestForm = new FormData()
        requestForm.append('id', todo.id)
        requestForm.append('title', todo.title)
        requestForm.append('user', todo.user)
        requestForm.append('completed', !todo.completed) // 반대로 보내줘야 수정되니까
        axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, this.requestHeader) // form먼저
          .then(res => {
            console.log(res) 
            todo.completed = !todo.completed // vue의 화면 반영을 위해
          })
          .catch(err => {
            console.log(err)
          })
      }
    }
  }
</script>

<style>
  .complete {
    text-decoration: line-through;
    color: #999;
  }
</style>