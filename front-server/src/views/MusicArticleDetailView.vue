<template>
  <div
    class="wrapper flex"
    :style="`background-image: linear-gradient(to bottom, rgba(20, 18, 23, 0.705), rgba(20, 18, 23, 0.8)), url(${music[0]?.album_img})`"
  >
    <!-- {{this.$route.params.id}}-->
    <!-- {{article}}  -->
    <div class="review-box">
      <div
        class="review-item"
        style="padding-left: 4%; padding-top: 2%; height: 80vh"
      >
        <span
          style="display: flex; float: right; margin-right: 15px; color: white"
          @click="
            $router.push({
              name: 'MusicDetailView',
              params: { musicid: music[0]?.id },
            })
          "
        >
          음악으로 돌아가기</span
        >
        <h1>{{ article?.title }}</h1>

        <p>{{ article?.content }}</p>

        <p style="font-size: 0.5em; padding-top: 20px">
          {{ article?.created_at?.substr(0, 10) }}에 작성됨
        </p>

        <p style="font-size: 0.5em">
          {{ article?.updated_at?.substr(0, 10) }}에 수정됨
        </p>

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

        <CommentList style="height: 52vh" :id="String(this.$route.params.id)" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CommentList from "@/components/CommentList";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MusicArticleDetailView",
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
    music() {
      return this.$store.getters?.article_music;
    },
    like() {
      // console.log(this.article.like_count)
      return this.article?.like_users?.length;
    },
  },
  methods: {
    getArticleDetail() {
      console.log(this.$route.params?.id);
      this.$store.dispatch("getArticleDetail", this.$route.params?.id);
    },
    deleteArticle() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/articles/${this.$route.params?.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // this.$store.dispatch('getMusicArticles', this.music?.id)
          // console.log(res);
          this.$router.push({
            name: "MusicDetailView",
            params: { musicid: this.music[0]?.id  },
          });
          // this.$router.go(0)
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
  overflow: scroll;
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
  width: 70%;
  height: 70%;
  /* display: flex; */
  /* align-items: center; */
  background: #9a9b9b91;
  box-shadow: -3px -3px 7px #ffffff, 3px 3px 5px #ceced1;
  position: absolute;
  top: 50%;
  left: 57%;
  transform: translate(-50%, -50%);
}
</style>
