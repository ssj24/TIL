<template>
  <li @click="onVideoSelect" class="list-group-item">
    <img :src="thumbnailUrl" alt="thumbnail" />
    <!-- <div class="media-body">{{ video.snippet.title }}</div> -->
    <div class="media-body" v-html="video.snippet.title"></div>
  </li>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  methods: {
    onVideoSelect() {
      this.$emit("videoSelect", this.video);
    }
  },
  computed: {
    // 미리 캐싱되어 있음 이미 호출된 상태로 오기 때문에 template에서 () 안 붙임.(watch는 그때그때 호출하는 거라 써야 함.)
    thumbnailUrl() {
      return this.video.snippet.thumbnails.default.url;
    }
  }
};
</script>

<style scoped>
li {
  display: flex;
  cursor: pointer;
}
li:hover {
  background-color: rgb(253, 237, 222);
}
</style>