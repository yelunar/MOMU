<template>
  <div class="articleview" style="margin-bottom;: 0%">
    <!-- <h1>Article Page</h1> -->
    <!-- <audio src="https://www.youtube.com/watch?v=DtP5V-PYhso"></audio> -->
    <!-- <iframe width="300" height="25" src="https://www.youtube.com/embed/DtP5V-PYhso?version=2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> -->

    <ArticleList />
  </div>
</template>

<script>
import ArticleList from "@/components/ArticleList.vue";

export default {
  name: "ArticleView",
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  created() {
    // 실행하면서 바로 데이터 불러오기
    this.getArticles();
    // this.movie()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        // console.log(this.$route.params.movieid);
        this.$store.dispatch("getArticles", this.$route.params.movieid);
      } else {
        alert("로그인이 필요한 서비스 입니다.");
        this.$router.push({ name: "LogInView" });
      }
    },
  },
};
</script>

<style scoped>
.articleview {
  padding: 0;
  width: 100%;
  height: 100vh;
  margin-top: 0%;
}
</style>