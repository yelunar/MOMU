<template>
  <div class="article-list" style="margin-bottom;: 0%">
    <MusicArticleItem
      v-for="article in musicarticles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script>
import MusicArticleItem from "@/components/MusicArticleItem";

export default {
  name: "MusicArticleList",
  components: {
    MusicArticleItem,
  },
  computed: {
    musicarticles() {
      return this.$store.state.articles;
    },
  },
};
</script>

<style scoped>
.article-list {
  text-align: start;
  padding-left: 5%;
  padding-right: 5%;
  color: white;
  padding-bottom: 0%;
}
</style>
