<template>
  <div class="todo-list">
    <h2 class="text-left mx-3">{{ category }}</h2>
    <b-container fluid>
      <b-row>
        <b-col sm="12">
          <b-row>
            <b-col sm="10">
              <b-input type="text" v-model="newTodo" @keyup.enter="addTodo" class="d-inline" />
            </b-col>
            <button @click="addTodo" class="btn btn-outline-info d-inline">+</button>
          </b-row>
          <hr />
          <li v-for="todo in todos" :key="todo.id" class="text-left">
            <span>{{ todo.content }}</span> &nbsp;&nbsp;
            <button @click="removeTodo(todo.id)" class="btn btn-outline-danger">x</button>
          </li>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// 정보를 내보낸다
export default {
  props: {
    category: {
      type: String,
      required: true,
      validator: function(value) {
        if (value.length < 5) {
          return true;
        } else {
          return false;
        }
      }
    }
  },
  data: function() {
    return {
      todos: [],
      newTodo: ""
    };
  },
  methods: {
    addTodo: function() {
      if (this.newTodo.length !== 0) {
        this.todos.push({
          id: Date.now(),
          content: this.newTodo,
          completed: false
        });
        this.newTodo = "";
      }
    },
    removeTodo: function(todoId) {
      this.todos = this.todos.filter(todo => {
        return todo.id !== todoId;
      });
    }
  }
};
</script>

<style>
.todo-list {
  display: inline-block;
  width: 33%;
}
</style>