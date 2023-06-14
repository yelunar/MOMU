<template>
  <div class="entire text-white">
    <h1
      style="
        font-weight: bold;
        padding-bottom: 5%;
        margin-top: 15px;
        color: white;
      "
    >
      나만의 PLAYLIST를 만들어 보아요💿
    </h1>

    <div class="form-check form-switch pb-2">
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
      <label class="form-check-label" for="flexSwitchCheckChecked">{{
        this.ismovie
      }}</label>
    </div>

    <div v-if="ismovie === '영화'">
      <div class="row row-cols-2 row-cols-md-5 g-4">
        <div class="col" v-for="item in result" :key="item.pk">
          <searchresult :result="item" />
        </div>
      </div>

      <div
        class="texts"
        style="display: flex; justify-content: center; padding-bottom: 2%"
      ></div>
      <!-- <h2>SELECT GENRE</h2> -->
      <div class="buttons">
        <button
          v-for="genre in this.$store.state.allgenre"
          :key="genre"
          :id="genre"
          class="mx-2 btn btn-sm btn-outline-warning waves-effect my-1"
          @click="onclick(genre), check(genre)"
        >
          {{ genre }}
        </button>
      </div>
      <div style="padding-left: 88%">
        <button class="btn btn-success m-1" @click="genreserach">
          선택 장르 제출
        </button>
      </div>
      <div class="row row-cols-2 row-cols-md-5 g-4 pb-5">
        <div class="col" v-for="item in genreresult" :key="item.pk">
          <searchresult :result="item" />
        </div>
      </div>
    </div>
    <div v-else style="padding-top: 2%">
      <div class="buttons">
        <div class="row row-cols-2 row-cols-md-5 g-4">
          <div class="col" v-for="item in result1" :key="item.id">
            <musicSearch :result="item" />
          </div>
        </div>

        <button
          v-for="genre in this.$store.state.musicgenre"
          :key="genre"
          :id="genre"
          class="mx-2 btn btn-sm btn-outline-warning waves-effect my-1"
          @click="onclick(genre), musiccheck(genre)"
        >
          {{ genre }}
        </button>
      </div>
      <div style="padding-left: 88%">
        <button class="btn btn-success m-1" @click="musicgenreserach">
          선택 장르 제출
        </button>
      </div>
      <div class="row row-cols-2 row-cols-md-5 g-4 pb-5">
        <div class="col pt-2" v-for="item in musicgenreresult" :key="item.id">
          <musicSearch :result="item" />
        </div>
      </div>
    </div>
    <!-- <button @click="mbti">{{this.$store.getters.currentUser.mbti}}</button>
    {{this.mbtimusic}} -->
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import searchresult from "@/components/searchresult";
import musicSearch from "@/components/musicsearch";

export default {
  name: "searchView",
  components: {
    searchresult,
    musicSearch,
  },
  created() {},
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
      mbtimusic : null,
      mbtimovie : null,
      ismovie: "영화",
    };
  },
  computed: {},

  methods: {
    ismovied() {
      if (this.ismovie === "영화") {
        this.ismovie = "음악";
      } else {
        this.ismovie = "영화";
      }
    },


    check(genre) {
      // console.log(genre);
      if (this.checkdata.includes(this.$store.state.allgenre_dict[genre])) {
        this.checkdata.splice(this.checkdata.indexOf(genre), 1);
      } else {
        this.checkdata.push(this.$store.state.allgenre_dict[genre]);
      }
      console.log(this.checkdata);
    },

    musiccheck(genre) {
      // console.log(genre)
      if (
        this.musiccheckdata.includes(this.$store.state.musicgenre_dict[genre])
      ) {
        this.musiccheckdata.splice(this.musiccheckdata.indexOf(genre), 1);
      } else {
        this.musiccheckdata.push(this.$store.state.musicgenre_dict[genre]);
      }
      console.log(this.musiccheckdata);
    },
    onclick(genre) {
      // console.log(genre);
      document.getElementById(genre).classList.toggle("btn-outline-warning");
      document.getElementById(genre).classList.toggle("btn-warning");
      document.getElementById(genre).classList.toggle("text-black");
    },

    genreserach() {
      const genre = this.checkdata;
      if (genre.length === 0) {
        if (this.genreresult) {
          this.genreresult = null
        } else {
          alert("하나 이상의 장르를 선택해 주세요");
        }

      } else {
        axios({
          method: "post",
          url: `${API_URL}/api/v2/genre/`,
          data: {
            genre,
          },
          headers: {
            Authorization: `Token ${this.$store.getters.token}`,
          },
        }).then((res) => {
          this.genreresult = res.data;
          // console.log(this.genreresult);
        });
      }
    },
    musicgenreserach() {
      const genre = this.musiccheckdata;
      if (genre.length === 0) {
        if (this.musicgenreresult) {
          this.musicgenreresult = null
        } else {
          alert("하나 이상의 장르를 선택해 주세요");
        }
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
  },
};
</script>

<style scoped>
.entire {
  justify-content: right;
  align-items: center;
  background-image: linear-gradient(
      to bottom,
      rgba(20, 18, 23, 0.541),
      rgba(20, 18, 23, 0.541)
    ),
    url(../search.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100vh;
  width: 100vw;
  padding-left: 7%;
  padding-right: 30%;
  padding-top: 3%;
  overflow: scroll;
}

#haha {
  background: transparent;
  border: 0;
  /* border-bottom: 2px solid rgba(0, 0, 0, 0.6); */
  border-bottom: 2px solid rgb(128, 128, 128);
  padding-left: 10px;
  padding-right: 60px;
  padding-bottom: 2px;
  font-size: 18px;
}
input:focus {
  outline: none;
  color: rgb(165, 165, 165);
}
h1 {
  font-family: "GmarketSansMedium";
}
</style>
