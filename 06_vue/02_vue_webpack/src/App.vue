<template>
  <div id="app">
    <!-- component 한 덩어리임을 나타낸다. -->
    <h1>여기는 최상위 컴포넌트입니다.</h1>
    <todo-list category="Wishlist"></todo-list>
    <todo-list category="By 2019"></todo-list>
    <todo-list category="Prepare 2020"></todo-list>
  </div>
</template>

<script>
// 1. 하위 컴포넌트 불러오기
import TodoList from "./components/TodoList.vue"; //import 뒤의 이름은 내가 쓸 이름으로 해도 된다.
// 2. 불러온 컴포넌트를 최상위(부모) 컴포넌트에 등록
export default {
  components: {
    TodoList // 여기에서 ,하고 계속 자식 컴포넌트를 넣어준다.
  }
};
</script>

<style>
</style>