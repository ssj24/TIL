<template>
  <div v-if="video" class="col-lg-8">
    <!-- 상위에 row를 줘야 됨. 얘의 상위는 app-->
    <div class="embed-responsive embed-responsive-16by9">
      <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
    </div>
    <div class="details">
      <!-- <h4>{{ video.snippet.title }}</h4> -->
      <h4 v-html="video.snippet.title"></h4>
      <p>{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "VideoDetail",
  props: {
    video: {
      type: Object
      // video 선택이 안 될 수도 있어서 required 안 줌
    }
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId;
      return `http://www.youtube.com/embed/${videoId}`;
    }
  }
};
</script>

<style scoped>
.details {
  margin-top: 10px;
  padding: 10px;
  border: 1px solid orange;
  border-radius: 4px;
}
</style>