<template>
  <div class="articleview" style="margin-bottom;: 0%">
    <!-- <audio src="https://www.youtube.com/watch?v=DtP5V-PYhso"></audio> -->
    <!-- <iframe width="300" height="25" src="https://www.youtube.com/embed/DtP5V-PYhso?version=2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> -->
    <!-- 
    <router-link
      :to="{
        name: 'MusicCreateView',
        params: { musicid: this.$route.params.musicid },
      }"
      >[create]</router-link
    > -->
    <MusicArticleList />
  </div>
</template>

<script>
import MusicArticleList from "@/components/MusicArticleList.vue";

export default {
  name: "MusicArticleView",
  components: {
    MusicArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  created() {
    // 실행하면서 바로 데이터 불러오기
    this.getMusicArticles();
    // this.movie()
  },
  methods: {
    getMusicArticles() {
      if (this.isLogin) {
        // console.log(this.$route.params.musicid);
        this.$store.dispatch("getMusicArticles", this.$route.params.musicid);
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
