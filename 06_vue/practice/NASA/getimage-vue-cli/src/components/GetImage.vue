<template>
  <div>
    <button v-on:click="getCosmicImage">Pic</button>
    <hr />
    <img v-for="image in images" v-bind:key="image.id" v-bind:src="image.content" alt="universe" />
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      images: []
  },
  mehtods: {
    getCosmicImage: function() {
      const URL =
        "https://api.nasa.gov/planetary/apod?api_key=7bNoblBoaHXIyyD4nqjtyl0fUhNpQPimGdumec77";
      Vue.axios.get(URL).then(response => {
        this.images.push(
          id: Date.now(),
          content: response.url,
        );
      });
    }
  }
};
</script>

<style>
</style>