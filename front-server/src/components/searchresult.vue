<template>
  <div class="card h-100">
    <img
      :src="this.result?.poster_path"
      class="card-img-top"
      alt="..."
      @click="
        $router.push({
          name: 'MovieDetailView',
          params: { movieid: result?.pk },
        })
      "
    />
    <!-- {{result}} -->
    <div class="">
      <!-- <h5 class="card-title">{{ this.result?.title }}</h5> -->
      <!-- <p class="card-text">{{ this.result?.overview }}</p> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "searchResult",
  props: {
    result: Object,
  },
};
</script>

<style scoped>
.result {
  width: 80%;
}
.card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
.card-body {
  padding-bottom: 0px;
}

.card {
  background-color: transparent;
  border-color: transparent;
}
</style>
