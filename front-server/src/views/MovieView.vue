<template>
  <div id="MyMainListItem" style="overflow: auto; padding-right: 8%">
    <!--search bar 시작 -->

    <div class="search" style="padding-top: 0%; padding-bottom: 2%">
      <div
        class="form-check form-switch"
        style="padding-left: 15%; padding-right: 7%"
      >
        <input
          class="form-check-input"
          style="
            background-color: #04aa6d;
            border-color: transparent;
            border: none;
          "
          type="checkbox"
          role="switch"
          id="flexSwitchCheckChecked"
          checked
          @click="ismovied"
        />
        <label
          class="form-check-label"
          style="color: white"
          for="flexSwitchCheckChecked"
          >{{ this.ismovie }}</label
        >
      </div>

      <div v-if="ismovie === '영화'">
        <div
          class="searchbar"
          style="
            justify-content: center;
            padding-top: 3%;
            padding-bottom: 8%;
            padding-left: 15%;
          "
        >
          <input
            id="haha"
            type="text"
            @keyup.enter="search"
            placeholder="찾고 싶은 영화를 입력해주세요"
            v-model="inputdata"
            class="mb-5 me-3"
            style="text-align: center; width: 60%"
          />
          <button name="" id="" class="search-btn" @click="search">검색</button>
        </div>

        <div
          class="row row-cols-2 row-cols-md-5 g-5"
          style="padding-right: 15%; padding-left: 5%"
        >
          <div class="" v-for="item in result" :key="item.pk">
            <searchresult :result="item" />
          </div>
        </div>

        <!-- <div
          class="texts"
          style="display: flex; justify-content: center; padding-bottom: 22px"
        ></div>

        <div
          class="tab-pane fade"
          id="pills-contact"
          role="tabpanel"
          aria-labelledby="pills-contact-tab"
        >
          ...
        </div> -->
      </div>

      <div v-else>
        <div
          class="searchbar"
          style="
            justify-content: center;
            padding-top: 3%;
            padding-bottom: 8%;
            padding-left: 15%;
          "
        >
          <input
            id="haha"
            type="text"
            @keyup.enter="musicsearch"
            v-model="inputdata1"
            class="mb-5 me-3"
            placeholder="찾고 싶은 음악을 입력해주세요"
            style="text-align: center; width: 60%"
          />
          <button name="" id="" class="search-btn" @click="musicsearch">
            검색
          </button>
        </div>

        <div
          class="row row-cols-2 row-cols-md-5 g-5 pd-2"
          style="padding-right: 15%; padding-left: 5%"
        >
          <div
            class="col d-flex justify-content-center"
            style="padding-bottom: 10%"
            v-for="item in result1"
            :key="item.id"
          >
            <musicSearch :result="item" />
          </div>
        </div>
      </div>
    </div>
    <!-- 여기 -->

    <!-- search bar 끝 -->

    <div
      class="d-flex justify-content-between"
      style="padding-right: 18%; padding-left: 8%"
    >
      <!-- <iframe style="" width="300" height="50" src="https://www.youtube.com/embed/hKhwHCjo_TU?start=14&fs=0&modestbranding=1&controls=1&autoplay=0&loop=1&mute=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen; "></iframe> -->
      <div id="MovieListItem" style="width: 40vw">
        <h2 class="" style="margin-left: 2%; color: white; padding-bottom: 4%">
          기대되는 영화를 추천해드려요🤩
        </h2>
        <div v-if="!newmovie"></div>
        <carousel-3d
          v-else
          space="130"
          class="px-0"
          height="285px;"
          style="padding-right: 17%"
          :autoplay="true"
          :autoplay-timeout="2000"
        >
          <slide
            v-for="(movie, index) in newmovie"
            :key="index"
            :index="index"
            style="width: 200px"
          >
            <!-- <span class="bg-transparent">{{movie.title[0]}}</span> -->
            <img
              :src="`${movie?.poster_path}`"
              alt=""
              @click="
                $router.push({
                  name: 'MovieDetailView',
                  params: { movieid: movie?.pk },
                })
              "
            />
          </slide>
        </carousel-3d>
      </div>

      <div class="pt-0 mb-3" id="MusicListItem" style="width: 40vw">
        <h2 style="margin-left: 2%; color: whitesmoke; padding-bottom: 7%">
          요즘 HOT한 음악은?🔥
        </h2>
        <carousel-3d
          space="150"
          class="px-0"
          style="padding-right: 17%"
          :autoplay="true"
          :autoplay-timeout="2000"
          height="230px;"
        >
          <slide
            v-for="music in allmusic"
            :key="music.id"
            :index="music.id - 1"
            style="width: 240px"
          >
            <!-- <span class="bg-transparent">{{music.title}}</span> -->
            <img
              :src="`${music.album_img}`"
              alt=""
              @click="
                $router.push({
                  name: 'MusicDetailView',
                  params: { musicid: music.id },
                })
              "
            />
          </slide>
        </carousel-3d>
      </div>
    </div>
    <!-- 토글 시작 -->
    <div class="ranking" style="padding-top: 5%">
      <div class="toggls" style="padding-left: 9%">
        <ul class="nav nav-pills mb-3 mx-1" id="pills-tab" role="tablist">
          <li class="nav-item" role="presentation">
            <button
              class="nav-link active"
              id="pills-home-tab"
              data-bs-toggle="pill"
              data-bs-target="#pills-home"
              type="button"
              role="tab"
              aria-controls="pills-home"
              aria-selected="true"
            >
              좋아요가 많은
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="pills-profile-tab"
              data-bs-toggle="pill"
              data-bs-target="#pills-profile"
              type="button"
              role="tab"
              aria-controls="pills-profile"
              aria-selected="false"
            >
              리뷰가 많은
            </button>
          </li>
          <li v-if="this.$store.getters.isLogin" class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="pills-mbti-tab"
              data-bs-toggle="pill"
              data-bs-target="#pills-mbti"
              type="button"
              role="tab"
              aria-controls="pills-mbti"
              aria-selected="false"
            >
              {{ this.$store.getters.currentUser.mbti }} 친구들은 무엇을
              보았을까?
            </button>
          </li>
        </ul>
      </div>
      <div class="tab-content" id="pills-tabContent" style="margin-top: 2rem">
        <div
          class="tab-pane fade show active"
          id="pills-home"
          role="tabpanel"
          aria-labelledby="pills-home-tab"
        >
          <!-- <p style="color: white">좋아요순</p> -->
          <div class="d-flex">
            <div v-for="music in musicranklst" :key="music?.id">
              <!-- <p>{{ music?.title }}</p> -->
              <div style="width: 120px; height: 120px" class="text-white">
                <img
                  :src="music?.album_img"
                  alt=""
                  style="width: 100px; height: 100px"
                  @click="
                    $router.push({
                      name: 'MusicDetailView',
                      params: { musicid: music?.id },
                    })
                  "
                />
                <p>
                  {{ music?.title.substr(0, 4) }} .. ❤ {{ music?.like_count }}
                </p>
              </div>
            </div>
          </div>
          <div>
            <!-- {{movieranklst}} -->
            <div class="d-flex" style="padding-top: 2%">
              <div v-for="movie in movieranklst" :key="movie.id">
                <!-- <p>{{ movie?.title }}</p> -->
                <div style="width: 120px; height: 120px" class="text-white">
                  <img
                    :src="movie?.poster_path"
                    alt=""
                    style="width: 100px; height: 120px"
                    @click="
                      $router.push({
                        name: 'MovieDetailView',
                        params: { movieid: movie?.id },
                      })
                    "
                  />
                  <p>
                    {{ movie?.title.substr(0, 4) }} .. ❤
                    {{ movie?.like_count }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="tab-pane fade"
          id="pills-profile"
          role="tabpanel"
          aria-labelledby="pills-profile-tab"
        >
          <!-- <p style="color: white">리뷰순</p> -->
          <div class="d-flex">
            <div v-for="music12 in this.musicrankartilcelst" :key="music12?.id">
              <div style="width: 120px; height: 120px" class="text-white">
                <img
                  :src="music12?.album_img"
                  alt=""
                  style="width: 100px; height: 100px"
                  @click="
                    $router.push({
                      name: 'MusicDetailView',
                      params: { musicid: music12?.id },
                    })
                  "
                />
                <p>
                  {{ music12?.title.substr(0, 4) }} .. 💬
                  {{ music12?.music_count }}
                </p>
              </div>
            </div>
          </div>

          <div class="d-flex" style="padding-top: 2%">
            <div v-for="movie12 in this.movierankartilcelst" :key="movie12.id">
              <div style="width: 120px; height: 120px" class="text-white">
                <img
                  :src="movie12?.poster_path"
                  alt=""
                  style="width: 100px; height: 120px"
                  @click="
                    $router.push({
                      name: 'MovieDetailView',
                      params: { movieid: movie12?.id },
                    })
                  "
                />
                <p>
                  {{ movie12?.title.substr(0, 4) }} .. 💬
                  {{ movie12?.movie_count }}
                </p>
              </div>
            </div>
          </div>
        </div>
        <div
          class="tab-pane fade"
          id="pills-mbti"
          role="tabpanel"
          aria-labelledby="pills-mbti-tab"
        >
          <!-- <p style="color: white">mbti</p> -->
          <div class="d-flex">
            <div v-for="music123 in this.mbtimusic" :key="music123?.id">
              <div style="width: 120px; height: 120px" class="text-white">
                <img
                  :src="music123?.album_img"
                  alt=""
                  style="width: 100px; height: 100px"
                  @click="
                    $router.push({
                      name: 'MusicDetailView',
                      params: { musicid: music123?.id },
                    })
                  "
                />
                <p>
                  {{ music123?.title.substr(0, 6) }}
                </p>
              </div>
            </div>
          </div>

          <div class="d-flex" style="padding-top: 2%">
            <div v-for="movie123 in this.mbtimovie" :key="movie123.id">
              <div style="width: 120px; height: 120px" class="text-white">
                <img
                  :src="movie123?.poster_path"
                  alt=""
                  style="width: 100px; height: 120px"
                  @click="
                    $router.push({
                      name: 'MovieDetailView',
                      params: { movieid: movie123?.id },
                    })
                  "
                />
                <p>
                  {{ movie123?.title.substr(0, 6) }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// const API_URL = "http://127.0.0.1:8000";
import { Carousel3d, Slide } from "vue-carousel-3d";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import searchresult from "@/components/searchresult";
import musicSearch from "@/components/musicsearch";

export default {
  name: "MovieVue",
  components: {
    Carousel3d,
    Slide,
    searchresult,
    musicSearch,
  },
  data() {
    return {
      inputdata: null,
      inputdata1: null,
      result: null,
      result1: null,
      checkdata: [],
      musiccheckdata: [],
      genreresult: null,
      musicgenreresult: null,
      musicranklst: [],
      musicrankartilcelst: [],
      movieranklst: [],
      movierankartilcelst: [],
      ismovie: "영화",
      mbtimusic: null,
      mbtimovie: null,
    };
  },
  created() {
    this.movie();
    this.music();
    this.allmovies();
    this.musicrank();
    this.musicrankarticle();
    this.movierank();
    this.movierankarticle();
    this.mbti();
  },
  computed: {
    newmovie() {
      return this.$store.getters?.newmovie;
    },
    allmusic() {
      return this.$store.getters.music;
    },
    slice() {
      return this.$store.getters.music.slice(1);
    },
  },
  methods: {
    allmovies() {
      // console.log(123);
      if (
        this.$store.getters.allmovies === [] ||
        this.$store.getters.allmovies.length === 0
      ) {
        this.$store.dispatch("allmovies");
      }
    },
    movie() {
      console.log(this.$store.getters.newmovie.length);
      if (
        this.$store.getters.newmovie === [] ||
        this.$store.getters.newmovie.length === 0
      ) {
        this.$store.dispatch("movie");
        // console.log("최신영화");
      }
    },
    music() {
      if (
        this.$store.getters.music === [] ||
        this.$store.getters.music.length === 0
      ) {
        this.$store.dispatch("music");
      }
    },

    ismovied() {
      if (this.ismovie === "영화") {
        this.ismovie = "음악";
      } else {
        this.ismovie = "영화";
      }
    },

    search() {
      if (!this.$store.getters.isLogin){
        alert('로그인이 필요한 서비스입니다')
        this.result = null;
      } else {
      const inputdata = this.inputdata;
      if (inputdata.trim().length === 0) {
        // console.log(123);
        alert("검색어를 입력하세요");
        this.result = null;
      } else {
        console.log(inputdata, 123);
        axios({
          method: "get",
          url: `${API_URL}/api/v2/movie_search/${inputdata}/`,
          headers: {
            Authorization: `Token ${this.$store.getters.token}`,
          },
        }).then((res) => {
          this.result = res.data;
          // console.log(res);
        });
      }}
    },

    musicsearch() {
       if (!this.$store.getters.isLogin){
        alert('로그인이 필요한 서비스입니다')
        this.result1 = null;
      } else {
      const inputdata1 = this.inputdata1;
      if (inputdata1.trim().length === 0) {
        alert("검색어를 입력하세요");
        this.result1 = null;
      } else {
        axios({
          method: "get",
          url: `${API_URL}/api/v2/music_search/${inputdata1}/`,
          headers: {
            Authorization: `Token ${this.$store.getters.token}`,
          },
        }).then((res) => {
          this.result1 = res.data;
          // console.log(res);
        });
      }}
    },

    musicgenreserach() {
      const genre = this.musiccheckdata;
      if (genre.length === 0) {
        alert("하나 이상의 장르를 선택해 주세요");
      } else {
        axios({
          method: "post",
          url: `${API_URL}/api/v2/musicgenre/`,
          data: {
            genre,
          },
          headers: {
            Authorization: `Token ${this.$store.getters.token}`,
          },
        }).then((res) => {
          this.musicgenreresult = res.data;
          // console.log(this.musicgenreresult);
        });
      }
    },
    mbti() {
      console.log(this.$store.getters.currentUser?.mbti);
      axios({
        method: "post",
        url: `${API_URL}/api/v1/accounts/mbti/`,
        data: {
          mbti: this.$store.getters.currentUser?.mbti,
        },
      }).then((res) => {
        // console.log(res.data)
        this.mbtimusic = res.data[1];
        this.mbtimovie = res.data[0];
      });
    },

    movierank() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/movie/rank/like/`,
        // headers: {
        //   Authorization: `Token ${this.$store.getters.token}`,
        // },
      }).then((res) => {
        this.movieranklst = res.data;
        // console.log(res);
      })
      .catch((err)=> {
        console.log(err)
      })
    },
    movierankarticle() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/movie/rank/article/`,
        // headers: {
        //   Authorization: `Token ${this.$store.getters.token}`,
        // },
      }).then((res) => {
        this.movierankartilcelst = res.data;
        // console.log(res);
      })
      .catch((err)=> {
        console.log(err)
      })
    },
    musicrank() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/music/rank/like/`,
        // headers: {
        //   Authorization: `Token ${this.$store.getters.token}`,
        // },
      }).then((res) => {
        this.musicranklst = res.data;
        // console.log(res)
      })
      .catch((err)=> {
      console.log(err)
      })
    },
    musicrankarticle() {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/music/rank/article/`,
        // headers: {
        //   Authorization: `Token ${this.$store.getters.token}`,
        // },
      }).then((res) => {
        this.musicrankartilcelst = res.data;
        // console.log(res);
      })
      .catch((err)=> {
       console.log(err)
      })
    },
  },
};
</script>

<style scoped>
#MyMainListItem {
  padding-top: 80px;
  padding-left: 30px;
  /* width: 70vw; */
  width: 100vw;
  /* background-color: black; */
  background-image: linear-gradient(
      to bottom,
      rgba(20, 18, 23, 0.541),
      rgba(20, 18, 23, 0.541)
    ),
    url(../background.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}

#MyMainListItem h2 {
  margin: 0 auto;
  max-width: 1474px;
  font-weight: 700;
  margin-bottom: 20px;
  text-align: left;
  /* background-color: yellow; */
}
.link {
  position: absolute;
  bottom: 0%;
  /* right:0% */
}
.upcom {
  margin: 0 auto;
  width: 100%;
  max-width: 1474px;
  /* border: 1px solid red; */
}
.upcom div {
  display: inline-block;
  width: 200px;
  height: 300px;
  /* border: 1px solid black; */
  margin: 10px 6px;
  transition: all 0.2s;
}
.upcom div:first-child {
  margin-left: 0;
}
.upcom div:last-child {
  margin-right: 0;
}
.upcom div:hover {
  transform: scale(1.05);
}

.upcom img {
  width: 100%;
  height: 100%;
  border-radius: 4px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
}

.main_img {
  margin: 0;
}
#MusicListItem {
  padding-top: 80px;
}

#MusicListItem h3 {
  margin: 0 auto;
  max-width: 1474px;
  font-weight: 700;
  margin-bottom: 20px;
  text-align: left;
}

.MusicListItem div:first-child {
  margin-left: 0;
}
.MusicListItem div:last-child {
  margin-right: 0;
}

.image {
  max-width: 200px; /* 원하는 최대 가로 크기 */
  max-height: 200px; /* 원하는 최대 세로 크기 */
  border-radius: 4px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
}

.nowmusic div {
  display: inline-block;
  width: 200px;
  height: 300px;
  /* border: 1px solid black; */
  margin: 10px 6px;

  transition: all 0.2s;
}

.nowmusic div:first-child {
  margin-left: 0;
}
.nowmusic div:last-child {
  margin-right: 0;
}
.nowmusic div:hover {
  transform: scale(1.05);
}
/*  search bar */
#haha {
  background: transparent;
  border: 0;
  /* border-bottom: 2px solid rgba(0, 0, 0, 0.6); */
  border-bottom: 2px solid rgb(255, 255, 255);
  padding-left: 10px;
  padding-right: 60px;
  padding-bottom: 2px;
  font-size: 18px;
}
input:focus {
  outline: none;
  color: rgb(255, 255, 255);
}

h1 {
  font-family: "GmarketSansMedium";
}

.search-btn {
  background-color: #04aa6d;
  /* background-color: #be11c4; */
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 8px;
}

.flexSwitchCheckChecked {
  background-color: #04aa6d;
}

.tab-content {
  margin-top: 2rem; /* 필요한 간격 조정 */
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding-right: 11%;
  padding-bottom: 7%;
}

.d-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}

.nav-pills > .nav-item > .active {
  color: rgb(255, 255, 255) !important;
  background-color: #04aa6d !important;
}

.nav-pills > .nav-item > .nav-link {
  color: rgb(255, 255, 255) !important;
}
</style>
