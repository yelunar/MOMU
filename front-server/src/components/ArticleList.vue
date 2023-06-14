<template>
  <div class="article-list" style="margin-bottom;: 0%">
    <!-- <h3>리뷰 목록</h3> -->
    <ArticleListItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from "@/components/ArticleListItem";

export default {
  name: "ArticleList",
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
    // contents() {
    //   return this.$store.state.contents;
    // },
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
