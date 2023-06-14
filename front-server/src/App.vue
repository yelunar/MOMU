<template style="height: 100%">
  <div style="height: 100%">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />

    <div
      class="w3-sidebar bg-black w3-card-4 w3-animate-left"
      style="width: 280px; display: block; height: 100%"
      id="mySidebar"
    >
      <div class="w3-bar">
        <button
            @click="w3_close"
            class="w3-bar-item w3-button w3-right w3-padding-1 px-0 py-0 text-white"
            style="position:absolute; top:50%; right:10%;"
            title="close Sidebar"
          >
            <span style="width:10px; height:20px; font-stretch:ultra-expanded;">  《《   </span>
          </button>
        <span class="w3-bar-item"
          ><img
            src="./final_logo.png"
            alt="123"
            style="
              width: 220px;
              padding-left: 19px;
              padding-top: 5%;
              padding-bottom: 3%;
            "
            @click="$router.push({ name: 'MovieView' }).catch(() => {})"
          /></span
        >
      </div>
      <div class="w3-bar-block">
        <div class="dropdown">
          <hr />
          <a
            href="#"
            class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
            id="dropdownUser1"
            data-bs-toggle="dropdown"
            aria-expanded="false"
            style="padding-top: 8%; padding-bottom: 7%"
          >
            <img
              v-if="this.$store.getters.currentUser != ''"
              :src="require(`../../back-server/media/${profile_img}`)"
              alt=""
              width="40"
              height="40"
              class="rounded-circle me-2 ms-5"
              style="margin-left: 5%"
            />
            <img
              v-else
              src="../media/default.png"
              alt=""
              width="40"
              height="40"
              class="rounded-circle me-2 ms-5"
              style="margin-left: 5%"
            />
            <strong v-if="!this.$store.getters.isLogin">로그인이 필요합니다</strong>
            <strong v-else style="margin-left: 1%; font-size: 25px">{{
              this.$store.getters.currentUser?.nickname
            }}</strong>
          </a>
          <ul
            class="dropdown-menu dropdown-menu-dark text-small shadow"
            aria-labelledby="dropdownUser1"
            style="list-style-type: none"
          >
            <li
              style="
                text-decoration: none;
                display: flex;
                align-items: center;
                justify-content: center;
              "
            >
              <router-link
                v-if="this.$store.getters?.currentUser"
                class="dropdown-profile text-white bi mx-auto"
                width="16"
                height="16"
                style="
                  margin: 10px 0px 10px 0px;
                  text-decoration: none;
                  display: flex;
                  align-items: center;
                  justify-content: center;
                "
                @click="$router.go(0)"
                :to="{
                  name: 'ProfileView',
                  params: {
                    userid: this.$store.getters?.currentUser?.username,
                  },
                }"
                >Profile</router-link
              >
            </li>

            <li
              style="
                text-decoration: none;
                display: flex;
                align-items: center;
                justify-content: center;
              "
            >
              <router-link
                v-if="!this.$store.getters.currentUser"
                class="dropdown-profile text-white bi mx-auto"
                width="16"
                height="16"
                style="
                  margin: 10px 0px 10px 0px;
                  text-decoration: none;
                  display: flex;
                "
                :to="{ name: 'LogInView' }"
                >LogIn</router-link
              >
              <router-link
                v-else
                class="dropdown-profile text-white bi mx-auto"
                width="16"
                height="16"
                style="
                  margin: 10px 0px 10px 0px;
                  text-decoration: none;
                  display: flex;
                "
                :to="{ name: 'LogoutView' }"
                >LogOut</router-link
              >
            </li>
          </ul>

          <hr />
        </div>

        <div>
          <div class="menu d-flex">
            <li>
              <router-link
                class="nav-link text-white bi me-3 fw-bold fs-4"
                width="16"
                height="16"
                style="margin: 10px 0px 10px 0px"
                :to="{ name: 'MovieView' }"
                >TODAY</router-link
              >
            </li>
            <li>
              <router-link
                class="nav-link text-white bi me-3 fw-bold fs-4"
                width="16"
                height="16"
                style="margin: 10px 0px 10px 0px"
                :to="{ name: 'AllMovieView' }"
                >MOVIE</router-link
              >
            </li>
            <li>
              <router-link
                class="nav-link text-white bi me-3 fw-bold fs-4"
                width="16"
                height="16"
                style="margin: 10px 0px 10px 0px"
                :to="{ name: 'AllMusicView' }"
                >MUSIC</router-link
              >
            </li>

            <li>
              <router-link
                class="nav-link text-white bi me-3 fw-bold fs-4"
                width="16"
                height="16"
                style="margin: 10px 0px 10px 0px"
                :to="{ name: 'searchView' }"
                >SEARCH</router-link
              >
            </li>
          </div>
        </div>
      </div>
    </div>

    <div
      id="main"
      class="main"
      style="margin-left: 280px; height: 100vh; width: 100vw"
    >
      <!-- <div class="w3-container w3-display-container ps-0 pe-0"> -->
      <div
        class="container display-container"
        style="padding: 0; margin: 0; width: 100vw; height: 100vh"
      >
        <router-view v-if="this.isopen"  style="height: 100%" :key="$route.fullPath" />
        <router-view v-else  style="height: 100%; padding-left:15%;" :key="$route.fullPath" />
        
        
        <span
          title="open Sidebar"
          style="display: none    
          position: absolute;
          left:0px;
          top:0px;"
          id="openNav"
          class="w3-button w3-transparent w3-display-topleft w3-xlarge text-white"
          @click="w3_open"
          >☰</span
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isopen : true
    }
  },
  computed: {
    profile_img() {
      let abc = "default.png";
      if (this.$store.getters.currentUser) {
        abc = this.$store.getters.currentUser.profile_image.substring(1);
      }
      return abc;
    },
  },
  methods: {
    w3_open() {
      document.getElementById("main").style.marginLeft = "280px";
      document.getElementById("mySidebar").style.width = "280px";
      document.getElementById("mySidebar").style.display = "block";
      document.getElementById("openNav").style.display = "none";
      this.isopen = true
    },
    w3_close() {
      document.getElementById("main").style.marginLeft = "0";
      document.getElementById("mySidebar").style.display = "none";
      document.getElementById("openNav").style.display = "inline-block";
      this.isopen = false
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main {
  padding: 0;
  margin: 0;
  height: 100vh;
  width: 100%;
  margin: 0%;
}

html {
  height: 100vh;
}

@media screen and (max-width: 455px) {
  .h3 {
    font-size: 16px;
  }
}

body {
  height: 100%;
  background: #e6e6e6;
  color: rgb(53, 53, 53);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #343435;
  display: flex;

  /* margin: 0;
  padding: 0; */

  min-height: 100vh;

  flex-direction: column;
  /* 위에 이거 추가 */
}

.menu {
  display: flex;
  flex-direction: column;
  align-items: center;
}

* {
  font-family: "GmarketSansMedium";
}

@font-face {
  font-family: "GmarketSansMedium";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

li::marker {
  color: black;
}
</style>
