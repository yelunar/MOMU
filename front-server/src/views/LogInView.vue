<template>
  <div id="login" style="width: 100vw; background-color: rgba(0, 0, 0, 0.881)">
    <div class="loginForm">
      <h1
        style="
          margin-top: 0%;
          text-align: center;
          font-size: 300%;
          padding-bottom: 5%;

          color: white;
          font-weight: bold;
        "
      >
        Login
      </h1>

      <form class="form-container__form" @submit.prevent="logIn">
        <div class="form-container__form__input">
          <label for="username">email <span class="ms-4 ps-3"> </span> </label>
          <input
            type="text"
            id="username"
            placeholder="email"
            v-model="username"
          />
        </div>
        <div class="form-container__form__input">
          <label for="password"> password </label>
          <input
            type="password"
            id="password"
            placeholder="password"
            v-model="password"
          />
        </div>
        <button
          type="submit"
          value="logIn"
          class="form-container__form__submit"
        >
          로그인
        </button>
      </form>

      <div style="text-align: center; padding-top: 3%">
        <router-link
          style="text-decoration: none; text-align: center; color: white"
          :to="{ name: 'SignUpView' }"
          >Sign Up For?</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogInView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    logIn() {
      const username = this.username;
      const password = this.password;
      const payload = {
        username,
        password,
      };
      this.$store.dispatch("logIn", payload);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/LoginView.scss";
</style>
