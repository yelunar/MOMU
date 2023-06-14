<!-- views/CreateView.vue -->

<template>
  <div
    class="page"
    :style="`background-image: linear-gradient(to bottom,#000000b6, rgba(20, 18, 23, 0.8)), url(${movie.poster_path})`"
  >
    <div
      class="title-container"
      style="
        /* text-shadow: 3px 4px #ff00bf4b; */
        font-size: 30px;
        display: flex;
        align-items: center;
        padding-top: 4%;
      "
    ></div>
    <!-- 폼의 이벤트를 막는 것 중요, 메서드 실행 -->
    <div class="createreview_container">
      <div class="img_container" style="display: flex; align-items: center">
        <img class="movieImg" :src="movie.poster_path" alt="" />
        <h1>{{ movie.title }}</h1>
      </div>

      <form
        @submit.prevent="createArticle"
        class="create_form"
        style="padding-top: 3%; padding-left: 10%"
      >
        <div class="create_title">
          <label
            for="title"
            style="font-size: 20px; padding-bottom: 1%; color: white"
            >리뷰 제목을 입력하세요</label
          ><br />
          <textarea
            class="title"
            cols="50"
            rows="2"
            v-model.trim="title"
            style="background-color: rgba(255, 255, 255, 0.5)"
          ></textarea>
          <!-- <input type="text" id="title" v-model.trim="title" /> -->
        </div>
        <div class="create_content">
          <label
            for="content"
            style="font-size: 20px; padding-bottom: 1%; color: white"
            >리뷰 내용을 입력하세요</label
          ><br />
          <textarea
            class="content"
            cols="90"
            rows="7"
            v-model="content"
            style="background-color: rgba(255, 255, 255, 0.5)"
          ></textarea>
        </div>
        <input type="submit" class="submit" style="" />
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    };
  },
  computed: {
    movie() {
      return this.$store.getters.moviedetail;
    },
  },
  created() {
    // this.getmoviedetail();
  },
  methods: {
    createArticle() {
      const title = this.title;
      const content = this.content;
      const movie_pk = this.$route.params.movieid;
      const article_movie = this.movie;
      console.log(article_movie);
      if (!title) {
        alert("제목을 입력해주세요");
        return;
      } else if (!content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/${movie_pk}/movie_articles/`,
        data: { title, content, article_movie },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log(res);
          // this.$store.dispatch("allmovies");
          this.$router.push({
            name: "MovieDetailView",
            params: { movieid: this.movie?.id },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.page {
  margin: 0%;
  width: 100vw;
  height: 100vh;
  background-size: cover;
  background-repeat: no-repeat;
  overflow: scroll;
}
.h1 {
  /* margin-right: 10px; */
  font-weight: bold;
  font-size: 120px;
}

.img_container {
  width: 50vw;
  margin-right: 1%; /* Adjust spacing between elements as needed */
  padding-left: 10%;
}
h1 {
  font-family: "GmarketSansMedium";
  padding-left: 5%;
  /* padding-bottom: 3%; */
  color: white;
  font-weight: bold;
  font-size: 44px;
}
.movieImg {
  max-width: 27%;
  box-shadow: 5px 5px 5px #000;
  border-radius: 7px;
}
.form-container {
  flex-grow: 1;
  overflow-x: hidden;
}
.create_form {
  width: 100%;
  padding-left: 5%;
}

.create_title,
.create_content {
  width: 100vw;
  padding-bottom: 2%;
}

.content,
.title {
  resize: none;
  border: solid 2px #0000001f;
}

.submit {
  background-color: #04aa6d;
  /* background-color: #be11c4; */
  border: none;
  color: white;
  padding: 16px 32px;
  border-radius: 8px;
}
</style>
