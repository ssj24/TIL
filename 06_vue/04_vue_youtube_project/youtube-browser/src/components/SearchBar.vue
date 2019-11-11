<template>
  <div>
    <input @change="onInput" type="text" />
    <!-- @input하면 하나하나 날라가고 change는 엔터치면 날라감 -->
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  methods: {
    onInput(e) {
      // console.log(e.target.value); // target.value에 누적된 값이 뜬다.
      this.$emit("inputChange", e.target.value);
    }
  }
};
</script>

<style scoped>
input {
  width: 75%;
}
div {
  text-align: center;
  margin: 20px;
}
</style>
