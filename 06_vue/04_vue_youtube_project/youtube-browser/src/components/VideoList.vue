<template>
  <ul class="col-lg-4 list-group">
    <video-list-item
      v-for="video in videos"
      :key="video.etag"
      :video="video"
      @videoSelect="onVideoSelect"
    ></video-list-item>
  </ul>
</template>

<script>
import VideoListItem from "./VideoListItem";

export default {
  name: "VideoList",
  components: {
    VideoListItem
  },
  methods: {
    onVideoSelect(video) {
      this.$emit("videoSelect", video); //얘는 인자로 받아서 this.video가 아니다
    }
  },
  props: {
    videos: {
      type: Array,
      required: true
    }
  }
};
</script>

<style>
</style>