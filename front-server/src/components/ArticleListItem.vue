<template>
  <div class="items" style="margin-bottom;: 0%">
    <h3 class="title">
      <router-link
        :to="{
          name: 'DetailView',
          params: { id: article.id },
        }"
        class="router-link"
        >{{ article.title }}</router-link
      >
    </h3>

    <p class="text-muted" style="padding-bottom: 1%">
      <router-link
        :to="{ name: 'ProfileView', params: { userid: article.username } }"
        class="router-link"
      >
        - {{ article.user.nickname }}</router-link
      >
    </p>
  </div>
</template>

<script>
export default {
  name: "ArticleListItem",
  props: {
    article: Object,
  },
};
</script>

<style scoped>
.router-link {
  text-decoration: none;
  color: rgb(255, 255, 255);
}
</style>
