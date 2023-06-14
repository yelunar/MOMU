<template>
  <div
    class="wrapper flex"
    :style="`background-image: linear-gradient(to bottom, rgba(20, 18, 23, 0.705), rgba(20, 18, 23, 0.8)), url(${movie[0]?.poster_path})`"
  >
    <div class="review-box">
      <div
        class="review-item"
        style="padding-left: 4%; padding-top: 2%; height: 80vh"
      >
        <span
          style="display: flex; float: right; margin-right: 15px; color: white"
          @click="
            $router.push({
              name: 'MovieDetailView',
              params: { movieid: movie[0]?.id },
            })
          "
        >
          영화로 돌아가기</span
        >
        <h1>📚 {{ article?.title }}</h1>
        <div style="padding-left: 2%; padding-right: 5%; padding-top: 2%">
          <p style="font-size: 100%">{{ article?.content }}</p>
          <p style="font-size: 12px; margin-bottom: 2px">
            {{ article?.created_at?.substr(0, 10) }}에 작성
          </p>
          <p style="font-size: 12px">
            {{ article?.updated_at?.substr(0, 10) }}에 수정
          </p>
        </div>
        <!-- <p>{{article}}</p> -->
        <div
          class="d-flex justify-content-center"
          v-if="article?.username === this.$store.state.currentUser?.username"
        > 
          <router-link
            class="btn btn-success"
            v-if="article?.id"
            :to="{
              name: 'UpdateView',
              params: { id: article?.id },
            }"
            >수정</router-link
          >
          <form @submit.prevent="deleteArticle">
            <input class="btn btn-danger" type="submit" value="삭제" />
          </form>
        </div>

        <div
          v-if="article?.username != this.$store.state.currentUser?.username"
          style="margin-top: 15px"
          class=""
        >
          <button
            class="btn btn-outline-danger nwaves-effect"
            style="border: none"
            @click="likeArticle"
          >
            <p id="1" style="margin-bottom: 0px">
              {{ like }} <span class="text-danger"> ♥ </span>
            </p>
          </button>
        </div>

        <CommentList style="height: 52vh" :id="String(this.$route.params?.id)" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CommentList from "@/components/CommentList";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "DetailView",
  components: {
    CommentList,
  },
  created() {
    this.getArticleDetail();
  },
  computed: {
    article() {
      // console.log(this.$store.getters.article, 123124)
      return this.$store.getters?.article;
    },
    // movie() {
    //   return this.$store.getters.article?.article_movie[0]
    // },
    like() {
      // console.log(this.article.like_count)
      return this.article?.like_users?.length;
    },
    movie() {
      return this.$store.getters?.article?.article_movie;
    },
  },
  methods: {
    getArticleDetail() {
      // console.log(123);
      this.$store.dispatch("getArticleDetail", this.$route.params?.id);
    },
    deleteArticle() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/articles/${this.$route.params?.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state?.token}`,
        },
      })
        .then(() => {
          // console.log(res);

          this.$router.push({
            name: "MovieDetailView",
            params: { movieid: this.movie[0].id },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    likeArticle() {
      this.$store.dispatch("likeArticle", this.$route.params?.id);
    },
  },
};
</script>

<style scoped>
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
h1 {
  color: white;
  font-family: "GmarketSansMedium";
}

p {
  color: white;
}
.review-box {
  width: 60%;
  height: 70%;
  /* display: flex;
  align-items: center; */
  background: #9a9b9b91;
  box-shadow: -3px -3px 7px #ffffff, 3px 3px 5px #ceced1;
  position: relative;
  top: 50%;
  left: 45%;
  transform: translate(-50%, -50%);
}
</style>
