<template>
  <div class="wrapper flex" style="background-color: transparent">
    <iframe
      :src="`${videoid}?autoplay=1&mute=1&controls=0&frameborder=0%&fs=0&border=0&modestbranding=1;`"
      style="
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        autoplay=1;
        mute=1;
        border=0;
        fs=0;
        modestbranding=1;
        frameborder=0; 
        controls=0 컨트롤바 숨기기
       filter: Alpha(Opacity=85);
       background-color:#FFFFFF;
      "
      frameborder="0"
      allow="autoplay"
      allowfullscreen

      allowTransparency="true"
    ></iframe>

    <!-- <div style="width:100vw; height:60vh;">
      <iframe
            :src="videoid"
            
          ></iframe>
    </div>
    <div style="width:100vw; height:40vh;"> -->
    <!-- <div
        class="wrapper"
        :style="`background-image: linear-gradient(to bottom, rgba(20, 18, 23, 1), rgba(20, 18, 23, 0.8)), url(${musicdetail.album_img})`"
        style="overflow: hidden; background-position: center center"
      > -->
    <div class="music-detail" style="padding-right: 0px; margin-bottom: 0%">
      <div
        class="music-detail__container"
        style="padding-top: 2%; overflow: auto"
      >
        <div class="main-info" style="overflow: hidden">
          <img
            :src="musicdetail.album_img"
            class="musicImg"
            alt=""
            style="
              width: 15vw;
              margin-left: 20%;
              border-radius: 10px;
              margin-right: 10%;
            "
          />

          <div class="main-info__info">
            <h1 class="main-info__info__title" style="color: white">
              {{ musicdetail?.title }} 
            </h1>

            <div class="main-info__info__subinfo">
              <span>{{ musicdetail?.artist }} </span>
              <!-- <span>{{ musicdetail?.album }}</span> -->
            </div>

            <!-- 버튼 시작  -->
            <div style="padding-top: 10%" class="">
              <button
                class="btn btn-danger text-white waves-effect mb-2 me-2"
                @click="likeMusic"
                v-if="likeuserspk.includes(this.$store.state.currentUser.id)"
              >
                {{ musicdetail?.like_count }}개의 좋아요를 받은 음악입니다.
              </button>
              <button
                class="btn-like btn btn-outline-danger waves-effect mb-2 me-2"
                @click="likeMusic"
                v-else
              >
                {{ musicdetail?.like_count }}개의 좋아요를 받은 영화입니다.
              </button>
            </div>
          </div>
          <!-- 버튼 끝 -->
          <br />
        </div>

        <!-- 리뷰 시작 -->

        <div class="review-zone" style="padding-top: 3%">
          <h2
            class="review_start"
            style="
              padding-left: 5%;
              color: white;
              font-family: 'GmarketSansMedium';
            "
          >
            🎥 음악 {{ musicdetail.title }}의 리뷰
          </h2>
          <br />
          <h5 style="padding-left: 5%; color: white">
            <strong
              >| EMOTIONLY 사용자 평 {{ musicdetail.music_count }}개</strong
            >
          </h5>
          <!-- 하위 컴포넌트 시작 -> 리뷰관련 -->
          <div style="display: flex; padding-left: 70%">
            <router-link
              class="btn btn-review"
              :to="{
                name: 'MusicCreateView',
                params: { musicid: this.$route.params.musicid },
              }"
              ><span class="white-text">나도 리뷰 쓰기</span></router-link
            >
          </div>
          <br />
          <MusicArticleView />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import MusicArticleView from "@/views/MusicArticleView.vue";

export default {
  name: "MusicDetailView",
  data() {
    return {
      imgsrc: null,
    };
  },
  components: {
    MusicArticleView,
  },
  created() {
    this.getmusicdetail();
    // this.searchToApp()
  },
  computed: {
    imgSrc() {
      return `https://www.youtube.com/embed/${this.imgsrc}`;
    },
    musicdetail() {
      return this.$store.getters.musicdetail;
    },
    videoid() {
      return this.$store.getters.videoid;
    },
    likeuserspk() {
      const abc = [];
      this.musicdetail.like_users?.forEach((element) => {
        abc.push(element.pk);
      });
      return abc;
    },
    // id () {
    //   return this.$store.getters?.videoid
  },
  methods: {
    likeMusic() {
      this.$store.dispatch("likeMusic", this.$route.params?.musicid);
    },
    getmusicdetail() {
      // console.log(this.$route.params.musicid);
      this.$store.dispatch("getmusicdetail", this.$route.params?.musicid);
    },
  },
};
</script>

<style scoped>
/* iframe {
  position: absolute;
  top: 0;
  left: 0; 
  width: 100%;
  height: 60%;
  pointer-events: none;
} */

.music-detail__container {
  position: absolute;
  padding: 0;
  width: 100%;
  height: 100vh;
  box-sizing: border-box;
}

.main-info__info__subinfo {
  opacity: 0.7;
  font-weight: 300;
  margin-bottom: 8px;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}
.main-info__info__title {
  font-weight: bold;
}
.main-info {
  display: flex;
  align-items: flex-start;
}
.main-info__info__subinfo {
  margin-left: 10px;
}
.wrapper {
  /* width: 100px;
  height: 500px; */
  justify-content: right;
  align-items: center;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100vh;
  width: 100vw;
}
.main-info {
  height: 390px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  padding-right: 25%;
  /* margin-top: 10px; */
}
/* .main-info__poster {
  margin-left: 200px;
   margin-right: 50px;
} */

.main-info__info {
  margin-right: 120px;
}
.review_like {
  display: flex;
  justify-content: center;
  align-items: center;
}
.add {
  justify-content: center;
  align-items: center;
}

.textarea {
  color: white;
  width: 100%;
  min-height: 120px;
  box-sizing: border-box;
  border-radius: 20px;
  font-size: 1rem;
  resize: none;
  padding: 0;
  padding: 16px;
  background: linear-gradient(#000000c5, #141217) padding-box,
    linear-gradient(45deg, #ffb0d7, hsl(275, 100%, 69%)) border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}
.btn-review {
  width: 40%;
  height: 36px;
  border: 1px solid rgba(0, 0, 0, 0.4);
  background: linear-gradient(#ffffff, #ffffff) padding-box,
    linear-gradient(#ffb0d7, hsl(275, 100%, 69%)) border-box;
  border-radius: 20px;
  color: rgb(0, 0, 0);
}
.white-text {
  color: rgb(0, 0, 0);
}

.button-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  display: flex;
}
</style>
