<template>
  <!-- <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>-->
  <div id="app">
    <!-- component 한 덩어리임을 나타낸다. -->

    <todo-list category="Wishlist"></todo-list>
    <todo-list category="By 2019"></todo-list>
    <todo-list category="Prepare 2020"></todo-list>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TodoList from "./components/TodoList.vue";
// export default {
//   name: 'app',
//   components: {
//     HelloWorld
//   }
// }
export default {
  components: {
    TodoList
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
