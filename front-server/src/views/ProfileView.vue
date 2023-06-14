<template>
  <div>
    <!-- 프로필 이미지 변경 Modal -->
    <div
      class="modal fade"
      id="exampleModal123"
      data-bs-backdrop="static"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">프로필 사진 변경</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <b-form-file
              v-model="file1"
              :state="Boolean(file1)"
              placeholder="원하는 이미지를 선택하거나 드래그 해주세요"
              drop-placeholder="Drop file here..."
            ></b-form-file>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              닫기
            </button>
            <button type="button" class="btn btn-primary" @click="onclick">
              사진 변경
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- 팔로잉 Modal -->
    <div
      class="modal fade"
      id="exampleModal456"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title" id="exampleModalLabel">
              내가 팔로잉한 유저들
            </h4>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <p>
              <span
                v-for="following in profile.followings"
                :key="following.pk"
                style="padding-right: 1%"
                @click="
                  $router.push({
                    name: 'ProfileView',
                    params: { userid: following?.username },
                  }),
                    $router.go(0)
                "
                >{{ following.nickname }}</span
              >
            </p>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <!-- <button type="button" class="btn btn-primary" @click="onclick">Save changes</button> -->
          </div>
        </div>
      </div>
    </div>

    <!-- 팔로워 Modal -->
    <div
      class="modal fade"
      id="exampleModal789"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              나를 팔로우한 유저들
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <p>
              <span
                v-for="follower in profile.followers"
                :key="follower.pk"
                style="padding-right: 1%"
                @click="
                  $router.push({
                    name: 'ProfileView',
                    params: { userid: follower?.username },
                  }),
                    $router.go(0)
                "
                >{{ follower.nickname }}</span
              >
            </p>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <!-- <button type="button" class="btn btn-primary">Save changes</button> -->
          </div>
        </div>
      </div>
    </div>

    <!-- 회원 탈퇴 모달 -->
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">회원탈퇴</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            정말 탈퇴하시겠습니까? 탈퇴하시겠다면
            <span class="text-danger"> 회원탈퇴</span>를 쳐주세요
            <input type="text" v-model="inputdata" />
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              닫기
            </button>
            <button
              type="button"
              class="btn btn-danger"
              data-bs-dismiss="modal"
              @click="userdelete"
            >
              회원탈퇴
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="profilecon">
      <div class="pt-5">
        <div
          v-if="profile?.username === this.$store.getters.currentUser?.username"
          class="profile"
          data-bs-toggle="modal"
          data-bs-target="#exampleModal123"
        >
          <img
            style="position: relative; width: 150px; height: 150px"
            :src="require(`../../../back-server/media/${profile_img}`)"
            alt=""
          />
        </div>
         <div
          v-else
          class="profile"
        >
          <img
            style="position: relative; width: 150px; height: 150px"
            :src="require(`../../../back-server/media/${profile_img}`)"
            alt=""
          />
        </div>
        <div v-if="profile?.username === this.$store.getters.currentUser?.username"   style="position: absolute; right: 3%; top: 2%">
          <button
            type="button"
            class="btn btn-outline-danger me-2"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
          >
            회원탈퇴
          </button>
          <router-link
            class="btn btn-outline-success"
            :to="{
              name: 'UserUpdateView',
            }"
            >회원정보수정</router-link
          >
        </div>
        <div class="info text-white pt-5 ps-1">
          <h2 style="font-weight: 800; font-size: 40px; padding-bottom: 1%">
            {{ profile?.nickname }}님의 프로필
          </h2>
          <h4>
            <span data-bs-toggle="modal" data-bs-target="#exampleModal456"
              >팔로잉 {{ profile?.followings?.length }} |
            </span>
            <span data-bs-toggle="modal" data-bs-target="#exampleModal789">
              팔로워 {{ profile?.followers?.length }}</span
            >
          </h4>

          <div
            @click="follow"
            v-if="profile?.username != this.$store.state.currentUser?.username"
          >
            <button class="btn btn-outline-danger waves-effect mb-2 me-2">
              👬
            </button>
          </div>
        </div>
      </div>
    </div>
    <div
      style="
        height: 70vh;
        width: 100vw;
        background-color: black;
        display: flex;
        overflow: scroll;
      "
    >
      <div
        style="
          width: 60vw;
          height: 100%;
          padding-left: 2%;
          background-color: black;
        "
      >
        <ul
          class="nav nav-pills mb-3"
          id="pills-tab"
          role="tablist"
          style="padding-left: 2%; padding-top: 1%"
        >
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
              좋아요한 게시글
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
              좋아요한 영화
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="pills-contact-tab"
              data-bs-toggle="pill"
              data-bs-target="#pills-contact"
              type="button"
              role="tab"
              aria-controls="pills-contact"
              aria-selected="false"
            >
              좋아요한 음악
            </button>
          </li>
        </ul>
        <div class="tab-content" id="pills-tabContent">
          <div
            class="tab-pane fade show active"
            id="pills-home"
            role="tabpanel"
            aria-labelledby="pills-home-tab"
          >
            <div class="d-flex" style="flex-wrap: wrap">
              <div
                style="width: 200px; padding-bottom: 15px"
                v-for="article in profile?.like_articles"
                :key="article.id"
              >
                <span v-if="article?.article_music?.length === 0">
                  <img
                    :src="article?.article_movie[0]?.poster_path"
                    alt=""
                    style="width: 150px; height: 200px; border-radius: 2%"
                    @click="
                      $router.push({
                        name: 'DetailView',
                        params: { id: article?.id },
                      })
                    "
                  />

                </span>
                <span v-else>
                  <img
                    :src="article?.article_music[0]?.album_img"
                    alt=""
                    style="width: 150px; height: 200px; border-radius: 2%"
                    @click="
                      $router.push({
                        name: 'MusicArticleDetailView',
                        params: { id: article?.id },
                      })
                    "
                  />
 
                </span>
              </div>
            </div>

          </div>
          <div
            class="tab-pane fade"
            id="pills-profile"
            role="tabpanel"
            style="padding-left: 2%"
            aria-labelledby="pills-profile-tab"
          >
            <div class="d-flex" style="flex-wrap: wrap">
              <div
                style="width: 200px"
                v-for="movie in profile?.like_movies"
                :key="movie.id"
              >
                <img
                  :src="movie?.poster_path"
                  alt=""
                  style="width: 150px; hight: 150px; border-radius: 2%"
                  @click="
                    $router.push({
                      name: 'MovieDetailView',
                      params: { movieid: movie?.id },
                    })
                  "
                />
                <p>
                  <span
                    class="text-white"
                    @click="
                      $router.push({
                        name: 'MovieDetailView',
                        params: { movieid: movie?.id },
                      })
                    "
                  >
                    {{ movie?.title.substr(0, 10) }}</span
                  >
                </p>
              </div>
            </div>
          </div>

          <div
            class="tab-pane fade"
            id="pills-contact"
            role="tabpanel"
            style="padding-left: 2%"
            aria-labelledby="pills-contact-tab"
          >
            <div class="d-flex" style="flex-wrap: wrap">
              <div v-for="music in profile?.like_music" :key="music.id">
                <img
                  :src="music?.album_img"
                  alt=""
                  style="width: 150px; height: 150px; padding-right: 10%"
                  @click="
                    $router.push({
                      name: 'MusicDetailView',
                      params: { musicid: music?.id },
                    })
                  "
                />
                <p style="padding-top: 5%; font-size: 12px">
                  <span class="text-white">
                    {{ music?.title.substr(0, 10) }}
                  </span>
                  <!-- <span class="text-white"> {{ music?.artist }}</span> -->
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        style="
          width: 40vw;
          height: 100wh;
          padding-right: 10%;
          background-color: black;
        "
      >
        <h1
          style="
            color: white;
            font-weight: bold;
            padding-bottom: 10px;
            margin-bottom: 2px;
          "
        >
          My review
        </h1>

        <div class="d-flex" style="flex-wrap: wrap">
          <div
            style="width: 200px; padding-bottom: 15px"
            v-for="article in profile?.articles"
            :key="article.id"
          >
            <span v-if="article?.article_music?.length === 0">
              <img
                :src="article?.article_movie[0]?.poster_path"
                alt=""
                style="width: 150px; height: 150px; border-radius: 2%"
                @click="
                  $router.push({
                    name: 'DetailView',
                    params: { id: article?.id },
                  })
                "
              />
              <!-- <p>
                  <span
                    class="text-white"
                    @click="
                      $router.push({
                        name: 'MovieDetailView',
                        params: { movieid: movie?.id },
                      })
                    "
                  >
                    {{ movie?.title }}</span
                  >
                </p> -->
            </span>
            <span v-else>
              <img
                :src="article?.article_music[0]?.album_img"
                alt=""
                style="width: 150px; height: 150px; border-radius: 2%"
                @click="
                  $router.push({
                    name: 'MusicArticleDetailView',
                    params: { id: article?.id },
                  })
                "
              />
  
            </span>
          </div>
        </div>


      </div>
    </div>
  </div>
</template>

<script>
const API_URL = "http://127.0.0.1:8000";
import axios from "axios";
// import _ from "lodash";
export default {
  name: "ProfileView",
  data() {
    return {
      articles: [],
      username: "",
      file1: null,
      inputdata: "",
      likearticles: [],
      followings: [],
      followers: [],
    };
  },
  computed: {
    profile() {
      return this.$store.getters?.profile;
    },
    profile_img() {
      const abc = this.profile?.profile_image?.substring(1);
      //
      return abc;
    },
  },
  created() {
    this.getprofile();
  },
  methods: {
    onclick() {
      const userpk = this.profile.id;
      const profile_image = this.file1;
      // console.log(profile_image);
      axios({
        method: "post",
        url: `${API_URL}/api/v1/accounts/imgchange/`,
        headers: {
          Authorization: `Token ${this.$store.getters?.token}`,
          "Content-Type": "multipart/form-data",
        },
        data: {
          userpk,
          profile_image,
        },
      }).then(() => {
        // console.log(res);
        this.$store.dispatch("CurrentUser", this.profile?.username);
        this.$router.go(0);
      });
    },

    getprofile() {
      const username = this.$route.params?.userid;
      // console.log(username);
      this.$store.dispatch("getprofile", username);
    },
    follow() {
      const payload = { username: this.$route.params?.userid };
      // console.log(payload);
      this.$store.dispatch("follow", payload);
    },

    userdelete() {
      const inputdata = this.inputdata;
      // console.log(inputdata);
      const username = this.$route.params?.userid;
      if (inputdata === "회원탈퇴") {
        axios({
          method: "delete",
          url: `${API_URL}/api/v1/accounts/profile/${username}/`,
          headers: {
            Authorization: `Token ${this.$store.getters?.token}`,
          },
        }).then(() => {
          // console.log(res);
          alert(
            "이 편지는 영국에서 최초로 시작되어 일년에 한바퀴를 돌면서 받는 사람에게 행운을 주었고 지금은 당신에게로 옮겨진 이 편지는 4일 안에 당신 곁을 떠나야 합니다. 이 편지를 포함해서 7통을 행운이 필요한 사람에게 보내 주셔야 합니다. 복사를 해도 좋습니다. 혹 미신이라 하실지 모르지만 사실입니다. 영국에서 HGXWCH이라는 사람은 1930년에 이 편지를 받았습니다. 그는 비서에게 복사해서 보내라고 했습니다. 며칠 뒤에 복권이 당첨되어 20억을 받았습니다. 어떤 이는 이 편지를 받았으나 96시간 이내 자신의 손에서 떠나야 한다는 사실을 잊었습니다. 그는 곧 사직되었습니다. 나중에야 이 사실을 알고 7통의 편지를 보냈는데 다시 좋은 직장을 얻었습니다. 미국의 케네디 대통령은 이 편지를 받았지만 그냥 버렸습니다. 결국 9일 후 그는 암살당했습니다. 기억해 주세요. 이 편지를 보내면 7년의 행운이 있을 것이고 그렇지 않으면 3년의 불행이 있을 것입니다. 그리고 이 편지를 버리거나 낙서를 해서는 절대로 안됩니다. 7통입니다. 이 편지를 받은 사람은 행운이 깃들것입니다. 힘들겠지만 좋은게 좋다고 생각하세요. 7년의 행운을 빌면서..."
          );
          this.$store.dispatch("logout");
        });
      }
    },
  },
};
</script>

<style>
.profilecon {
  height: 35vh;
  width: 100vw;
  background-image: linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.418),
      rgba(20, 18, 23, 0.367)
    ),
    url(../profile.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  align-content: center;
}

.profile {
  position: relative;
  /* top:40px; */
  width: 150px;
  height: 150px;
  margin: 10px 10vw;
  /* background-color: #f08080; */
  border-radius: 100px;
  /* overflow:scroll; */
  overflow: hidden;

  float: left;

  /* margin-left: 120px; */
}

.image-container {
  display: flex;
  flex-wrap: wrap;
}

.image-container p {
  flex: 0 0 auto;
  margin-right: 10px; /* 여러 이미지 사이의 간격을 조절할 수 있습니다. */
}
.thumbnail-image {
  width: 10px;
  height: auto;
}

.nav-pills > .nav-item > .active {
  color: rgb(255, 255, 255) !important;
  background-color: #04aa6d !important;
}

.nav-pills > .nav-item > .nav-link {
  color: rgb(255, 255, 255) !important;
}

.h1 {
  font-family: "GmarketSansMedium";
  font-weight: bold;
}
</style>
