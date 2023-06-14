<template>
  <div
    class="wrapper flex"
    :style="`background-image: linear-gradient(to bottom, rgba(20, 18, 23, 1), rgba(20, 18, 23, 0.8)), url(${moviedetail?.poster_path})`"
  >
    <div class="movie-detail" style="padding-right: 0px; margin-bottom: 0%">
      <div
        class="movie-detail__container"
        style="padding-top: 3%; overflow: auto"
      > 
        <!-- <b-card-text>{{moviedetail.title}}</b-card-text> -->
        <div class="main-info" style="overflow: hidden">
          <img
            :src="moviedetail?.poster_path"
            alt=""
            style="
              width: 14vw;
              margin-left: 20%;
              border-radius: 10px;
              margin-right: 10%;
            "
          />

          <div class="main-info__info">
            <h1 class="main-info__info__title" style="color: white">
              {{ moviedetail?.title }}
            </h1>
            <div class="main-info__info__subinfo">
              <span class="genre_text" style="color: white">
                {{ moviedetail?.genre }} ・</span
              >
              <span class="release_text" style="color: white">
                {{ moviedetail?.release_date?.substr(0, 10) }}</span
              >
            </div>

            <div class="add">
              <p
                class="overview_text"
                style="color: white; width: 40vw; padding-bottom: 2%"
              >
                {{ moviedetail?.overview?.substr(0, 250) }} ...
              </p>

              <!--버튼 시작 -->
              <div style="margin-top: 15px" class="">
                <button
                  class="btn-like btn btn-danger text-white waves-effect mb-2 me-2"
                  @click="likeMovie()"
                  v-if="likeuserspk.includes(this.$store.state.currentUser?.id)"
                >
                  {{ moviedetail?.like_count }}개의 좋아요를 받은 영화입니다.
                </button>
                <button
                  class="btn-like btn btn-outline-danger waves-effect mb-2 me-2"
                  @click="likeMovie()"
                  v-else
                >
                  {{ moviedetail?.like_count }}개의 좋아요를 받은 영화입니다.
                </button>
              </div>

              <!-- 버튼 끝 -->
              <br />
            </div>
          </div>
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
            🎥 영화 | {{ moviedetail?.title }}의 리뷰
          </h2>
          <br />

          <h5 style="padding-left: 5%; color: white">
            <strong
              >| EMOTIONLY 사용자 평 {{ moviedetail?.movie_count }}개</strong
            >
          </h5>

          <!-- 하위 컴포넌트 시작 -> 리뷰관련 -->
          <div style="display: flex; padding-left: 70%">
            <router-link
              class="btn btn-review"
              style="width:100px;"
              :to="{
                name: 'CreateView',
                params: { movieid: this.$route.params?.movieid },
              }"
            >
              <span class="white-text" style="font-size:0.8em;">리뷰 쓰기</span>
            </router-link>
          </div>
          <br />
          <ArticleView />
        </div>
      </div>

      <!-- 하위컴포넌트인 리뷰를 보여줍니다. -->
    </div>
  </div>
</template>

<script>
import ArticleView from "@/views/ArticleView.vue";

export default {
  name: "MovieDetailView",

  computed: {
    // movie () {
    //   return this.$store.getters.allmovies[this.$route.params.movieid-1]
    // },
    moviedetail() {
      return this.$store.getters?.moviedetail;
    },
    articles() {
      return this.$store.state?.articles;
    },
    likeuserspk() {
      const abc = [];
      this.moviedetail.like_users?.forEach((element) => {
        abc.push(element.pk);
      });
      return abc;
    },
  },
  components: {
    ArticleView,
    // ArticleListItem,
  },
  created() {
    this.getmoviedetail();
  },

  methods: {
    likeMovie() {
      this.$store.dispatch("likeMovie", this.$route?.params?.movieid);
    },

    nolikeMovie() {
      // console.log(123);
      document.querySelector(".btn-like").classList.toggle("btn-danger");
      document
        .querySelector(".btn-like")
        .classList.toggle("btn-outline-danger");
      document.querySelector(".btn-like").classList.toggle("text-white");
    },
    getmoviedetail() {
      // console.log(this.$route.params?.movieid);
      this.$store.dispatch("getmoviedetail", this.$route.params?.movieid);
    },
  },
};
</script>

<style scoped>
.movie-detail__container {
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
