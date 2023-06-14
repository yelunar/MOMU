<template>
  <div class="list" style="padding-top: 7%; overflow: scroll">
    <h1 class="title" style="margin-top: 0%">전체 음악 목록🎧</h1>
    <div
      class="abc d-flex flex-wrap justify-content-center"
      style="padding-right: 15%; padding-left: 5%"
    >
      <div v-for="musicss in allmusic" class="music_for" :key="musicss.id">
        <img
          class="musicListImg"
          :src="musicss.album_img"
          style="width: 240px; cursor: pointer max-width: 20rem "
          alt=""
          @click="
            $router.push({
              name: 'MusicDetailView',
              params: { musicid: musicss.id },
            })
          "
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AllMusicView",
  computed: {
    allmusic() {
      return this.$store.getters.music;
    },
  },
  created() {
    this.music();
  },

  methods: {
    music() {
      if (
        this.$store.getters.music === [] ||
        this.$store.getters.music.length === 0
      ) {
        this.$store.dispatch("music");
      }
    },
  },
};
</script>

<style scoped>
.list {
  margin: 0%;
  width: 100vw;
  /* padding-left: 3%; */
  /* padding-right: 5%; */
  background-image: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.685),
      rgba(20, 18, 23, 0.534)
    ),
    url(../musicbackground.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}

.listCard div:hover {
  transform: scale(1.05);
}

.musicListImg {
  position: relative;
  display: inline-block;
  width: 100%;
  width: 200px;
  /* height: 300px; */
  border-radius: 4px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease-in;
  display: flex;
  margin: 5% 5% 5% 5%;
}
.musicListImg:hover {
  transform: scale(1.1);

  /* transform: scale(1.2); */
}

.music_for {
  margin-right: 2%;
}

.title {
  font-family: "GmarketSansMedium";
  padding-left: 5%;
  padding-bottom: 3%;
  color: white;
  font-weight: bold;
  font-size: 44px;
}
</style>
