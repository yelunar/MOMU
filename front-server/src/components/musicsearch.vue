<template>
  <div class="card h-100">
    <img
      :src="this.result?.album_img"
      class="card-img-top"
      alt="..."
      @click="
        $router.push({
          name: 'MusicDetailView',
          params: { musicid: result?.id },
        })
      "
    />
    <div class="card-body">
      <p class="" style="color: white">{{ this.result?.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "musicSearch",
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

.card-title {
  font-family: "GmarketSansMedium";
  /* font-weight: bold; */
  color: white;
  font: 10px;
}
.card {
  background-color: transparent;
  border-color: transparent;
}
</style>
