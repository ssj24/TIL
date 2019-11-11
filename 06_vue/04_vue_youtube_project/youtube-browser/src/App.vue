<template>
  <div id="app" class="container">
    <!-- 만약 inputChange 이벤트가 일어나면 onInputChange라는 method가 실행됨 -->
    <search-bar @inputChange="onInputChange"></search-bar>
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SearchBar from "./components/SearchBar";
import VideoList from "./components/VideoList";
import VideoDetail from "./components/VideoDetail";
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "App", // 최상단 컴포넌트이기 때문에 이름이 없어도 되지만 명시적으로 작성한다.
  data() {
    return {
      // namespace를 위해서.. components에서는 return할 때 꼭 {}로 객체로 만들어 줘야한다.
      videos: [],
      selectedVideo: null
    };
  },
  components: {
    SearchBar, // SearchBar: SearchBar 이렇게 썼었는데 업데이트 되면서 하나만 써도 되게 바뀜. 실제 데이터는 key-value로 들어간다.
    VideoList,
    VideoDetail
  },
  methods: {
    onVideoSelect(video) {
      this.selectedVideo = video;
    },
    onInputChange(inputValue) {
      // 얘 인자가 searchbar에서 받은 그 데이터
      // console.log(inputValue);
      axios
        .get(API_URL, {
          params: {
            // parameters
            key: API_KEY,
            type: "video",
            part: "snippet",
            q: inputValue
          }
        })
        .then(response => {
          // console.log(response);
          this.videos = response.data.items;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
</style>
