<template>
  <div
    class="login"
    style="
      background-color: rgba(0, 0, 0, 0.881);
      padding-top: 3%;
      width: 100vw;
      overflow: auto;
    "
  >
    <div class="signupForm2">
      <h1
        class="form-container__title"
        style="
          margin-top: 0%;
          text-align: center;
          font-size: 300%;
          padding-bottom: 5%;
          color: white;
          font-weight: bold;
        "
      >
        Edit Profile
      </h1>
      <div class="form-container__form__input">
        <!-- <label for="username">E-mail </label> -->
        <label for="username" style="color: white">Email</label>
        <input
          type="email"
          id="username"
          placeholder="Email"
          readonly
          v-model="credentials.username"
        />
      </div>

      <!-- <label for="password">비밀번호 </label> -->
      <div class="form-container__form__input">
        <label for="password" style="color: white">Password</label>

        <input
          type="password"
          id="originpassword"
          placeholder="OriginPassword"
          v-model="credentials.originpassword"
        />
      </div>

      <div>
        <!-- <label for="password">비밀번호 </label> -->
        <div class="form-container__form__input">
          <label for="password" style="color: white">Password Comfirm</label>

          <input
            type="password"
            id="password"
            placeholder="NewPassword"
            v-model="credentials.password"
          />
        </div>

        <div class="form-container__form__input">
          <label for="password" style="color: white">Password Comfirm</label>

          <!-- <label for="passwordConfirmation">비밀번호 확인 </label> -->
          <input
            type="password"
            id="passwordConfirmation"
            placeholder="NewPassword Comfirm"
            v-model="credentials.passwordConfirmation"
            @keyup.enter="signup"
          />
        </div>

        <!-- <label for="nickname">닉네임 </label> -->
        <div class="form-container__form__input">
          <label for="nickname" style="color: white">Nickname</label>

          <input
            type="text"
            id="nickname"
            placeholder="Nickname"
            v-model="credentials.nickname"
          />
        </div>

        <!-- <label for="mbti">MBTI: </label> -->
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
          정보 수정
        </button>
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
        currentuser: this.$store.getters.currentUser,
        username: this.$store.getters.currentUser.username,
        originpassword: null,
        password: null,
        passwordConfirmation: null,
        nickname: null,
        mbti: null,
      },
    };
  },
  methods: {
    signup: function () {
      console.log(123);
      axios({
        method: "put",
        url: `${API_URL}/api/v1/accounts/signup/`,
        data: this.credentials,
        // headers : {
        //   Authorization: `Token ${this.$store.state.token}`
        // }
      })
        .then((res) => {
          console.log(res);
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
        this.credentials.originpassword === null ||
        this.credentials.password === null ||
        this.credentials.passwordConfirmation == null ||
        this.credentials.nickname == null ||
        this.credentials.mbti == null
      ) {
        swal("필수 정보를 모두 입력해주세요.", {
          dangerMode: true,
        });
      } else {
        if (
          this.credentials.password != this.credentials.passwordConfirmation
        ) {
          swal("새 비밀번호가 일치하지 않습니다", { dangerMode: true });
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
