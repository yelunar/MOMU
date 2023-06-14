<template>
  <div
    class="login"
    style="width: 100vw; background-color: rgba(0, 0, 0, 0.881)"
  >
    <div class="signupForm pt-6">
      <h1
        class="form-container__title"
        style="
          margin-top: 0%;
          text-align: center;
          font-size: 300%;
          padding-bottom: 2%;
          color: white;
          font-weight: bold;
        "
      >
        Signup
      </h1>

      <div class="form-container__form__input">
        <label for="username" style="color: white">Email</label>
        <input
          type="email"
          id="username"
          placeholder="Email"
          v-model="credentials.username"
        />
      </div>

      <div class="form-container__form__input">
        <label for="password" style="color: white">Password</label>
        <input
          type="password"
          id="password"
          placeholder="Password"
          v-model="credentials.password"
        />
      </div>
      <div class="form-container__form__input">
        <label for="password" style="color: white">Password Comfirm</label>
        <input
          type="password"
          id="passwordConfirmation"
          placeholder="Password Comfirm"
          v-model="credentials.passwordConfirmation"
          @keyup.enter="signup"
        />
      </div>
      <div class="form-container__form__input">
        <!-- <label for="nickname">닉네임 </label> -->
        <label for="nickname" style="color: white">Nickname</label>
        <input
          type="text"
          id="nickname"
          placeholder="Nickname"
          v-model="credentials.nickname"
        />
      </div>
      <div class="form-container__form__input">
        <label for="mbti" style="color: white">MBTI</label>
        <input
          type="text"
          id="mbti"
          placeholder="MBTI"
          v-model="credentials.mbti"
        />
      </div>

      <button
        class="form-container__form__submit"
        @click="isValid"
        @keyup.enter="isValid"
      >
        회원가입
      </button>
      <div style="text-align: center; padding-top: 3%">
        <router-link
          style="text-decoration: none; color: white"
          :to="{ name: 'LogInView' }"
        >
          Already have an account?</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";
const API_URL = "http://127.0.0.1:8000";
// import VueSweetalert2 from 'vue-sweetalert2';

export default {
  name: "SignUpView",
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        nickname: null,
        mbti: null,
      },
    };
  },
  methods: {
    signup: function () {
      // console.log(123);
      axios({
        method: "post",
        url: `${API_URL}/api/v1/accounts/signup/`,
        data: this.credentials,
        // headers : {
        //   Authorization: `Token ${this.$store.state.token}`
        // }
      })
        .then(() => {
          // console.log(res);
          this.$router.push({ name: "LogInView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    isValid: function () {
      // console.log(this.credentials)
      // console.log(this.credentials.mbti.toUpperCase())
      const mbti_list = [
        "ISTJ",
        "ISFJ",
        "INFJ",
        "INTJ",
        "ISTP",
        "ISFP",
        "INFP",
        "INTP",
        "ESTP",
        "ESFP",
        "ENFP",
        "ENTP",
        "ESTJ",
        "ESFJ",
        "ENFJ",
        "ENTJ",
      ];
      if (
        this.credentials.username === null ||
        this.credentials.password === null ||
        this.credentials.passwordConfirmation == null ||
        this.credentials.nickname == null ||
        this.credentials.mbti == null
      ) {
        swal("필수 정보를 모두 입력해주세요.", {
          dangerMode: true,
        });
      } else {
        if (!this.credentials.username.includes("@")) {
          swal("이메일 형식을 확인해 주세요", { dangerMode: true });
        } else if (
          this.credentials.password != this.credentials.passwordConfirmation
        ) {
          swal("비밀번호를 확인해 주세요", { dangerMode: true });
        } else if (
          this.credentials.mbti.length != 4 ||
          mbti_list.includes(this.credentials.mbti.toUpperCase()) === false
        ) {
          swal("올바른 MBTI를 입력해 주세요", { dangerMode: true });
        } else {
          this.credentials.mbti = this.credentials.mbti.toUpperCase();
          this.signup(this.credentials);
        } // else 끝
      } // isValid else 끝
    }, // isValid 함수 끝
  }, // methods 끝
}; // export default 끝
</script>

<style lang="scss" scoped>
@import "../assets/SignupView.scss";
</style>
