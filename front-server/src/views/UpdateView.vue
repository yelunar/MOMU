
<!-- views/CreateView.vue -->

<template>
  <div class="page">
    <h1 style="margin-top: 0px; padding-top: 10%">🖥️ 게시글 수정</h1>
    <!-- {{ this.article }}
    {{ this.$route.params.id }} -->
    <!-- 폼의 이벤트를 막는 것 중요, 메서드 실행 -->
    <form
      @submit.prevent="updateArticle"
      class="update_form"
      style="padding-top: 3%"
    >
      <label
        for="title"
        style="font-size: 20px; padding-bottom: 1%; color: white"
        >리뷰 제목을 수정하세요</label
      ><br />
      <input
        type="text"
        id="title"
        cols="55"
        rows="2"
        v-model.trim="title"
        style="padding-bottom: 1%"
      /><br />
      <label
        for="content"
        style="
          font-size: 20px;
          padding-top: 1%;
          padding-bottom: 1%;
          color: white;
        "
        >리뷰 내용을 수정하세요 </label
      ><br />
      <textarea class="contents" cols="90" rows="7" v-model="content"></textarea
      ><br />
      <input type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "UpdateView",
  data() {
    return {
      title: null,
      content: null,
      id: null,
    };
  },
  computerd: {
    article() {
      return this.$store.getters.article;
    },
  },
  created() {
    this.getArticleUpdate();
  },
  methods: {
    updateArticle() {
      const title = this.title;
      const content = this.content;
      const id = this.article.id;
      if (!title) {
        alert("제목을 입력해주세요");
        return;
      } else if (!content) {
        alert("내용을 입력해주세요");
        return;
      }

      axios({
        method: "PUT",
        url: `${API_URL}/api/v1/articles/${id}/`,
        data: { title, content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log(res);
          if (this.article.article_music.length === 0) {
            this.$router.push({ name: "DetailView", params: { id: id } });
          } else if (this.article.article_movie.length === 0) {
            this.$router.push({
              name: "MusicArticleDetailView",
              params: { id: id },
            });
          }
          // this.$router.push({name:'MusicDetailView', params:{id:id}})
        })
        .catch((err) => {
          console.log(err);
        });
    },

    getArticleUpdate() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
      })
        .then((res) => {
          // console.log(res);
          this.article = res.data;
          this.title = this.article.title;
          this.content = this.article.content;
          this.id = this.$route.params.id;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.update_form {
  width: 100%;
  padding-left: 5%;
}
#submit {
  background-color: #04aa6d;
  /* background-color: #be11c4; */
  border: none;
  color: white;
  padding: 8px 28px;
  border-radius: 8px;
}

.page {
  margin: 0%;
  width: 100vw;
  height: 100vh;
  padding-left: 25%;
  background-image: linear-gradient(to bottom, #0000007a, rgba(20, 18, 23, 0.8)),
    url(../update_back.jg.jpg);
  overflow: scroll;
  background-size: cover;
  background-repeat: no-repeat;
}

h1 {
  font-weight: bold;
  font-size: 120px;
  font-family: "GmarketSansMedium";
  font-size: 44px;

  color: white;
}

.contents {
  resize: none;
}
</style>
