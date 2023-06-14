<template style="height:100vh;">
  <div class="list" style="padding-top: 7%; overflow: scroll;" >
    <!-- <div class="wrapper"> -->
    <!-- </div> -->
    <h1 class="title" style="margin-top: 0%">전체 영화 목록🎬</h1>
    <div
      class="abc d-flex flex-wrap justify-content-center"
      style="padding-right: 20%; padding-left: 5%"
    >
      <div
        v-for="movie in movies"
        :key="movie.id"
        class="movie_for"
        style="width: 200px; margin: 0; max-width: 20rem; margin-right: 2%"
      >
        <img
          class="movieListImg"
          :src="movie?.poster_path"
          :alt="movie?.title"
          @click="
            $router.push({
              name: 'MovieDetailView',
              params: { movieid: movie?.id },
            })
          "
          style="width: 200px; cursor: pointer"
        />
      </div>
    </div>
  </div>
</template>

<script>
import _ from "lodash";
// import axios from "axios";
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: "AllMovieView",

  computed: {
    movies() {
      const sample = _.sampleSize(this.$store.getters.allmovies, 200);
      return sample;
    },
  },

  created() {
    this.allmovies();
  },

  methods: {
        allmovies() {
      // console.log(123);
      if (this.$store.getters.allmovies ===[] || this.$store.getters.allmovies?.length === 0) {
        this.$store.dispatch("allmovies");
      }
    },
  },
};
</script>

<style scoped>
.list {
  position: static;
  left:0%;
  top:0%;
  margin: 0%;
  width: 100vw;
  height:100vh;
  /* padding-left: 3%; */
  /* padding-right: 5%; */
  background-image: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.685),
      rgba(20, 18, 23, 0.534)
    ),
    url(../moviebackground.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}

.listCard div:hover {
  transform: scale(1.05);
}

.movieListImg {
  position: relative;
  display: inline-block;
  width: 100%;
  width: 200px;
  /* height: 300px; */
  border-radius: 4px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease-in;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.movieListImg:hover {
  transform: scale(1.1);

  /* transform: scale(1.2); */
}

.movie_for .movieListImg {
  width: 200px;
  height: 300px;
  object-fit: cover;
  cursor: pointer;
  margin-right: 100px;
  margin-bottom: 20px;
}

.movie_for {
  margin-right: 10px;
  margin-bottom: 10px;
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
