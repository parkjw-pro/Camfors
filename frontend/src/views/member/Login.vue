<template>
  <!-- <div :style="cssProps"> -->
  <div>
    <div :style="cssProps" class="loginimg">
      <div id="box">
        <h2>로그인</h2>
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            style="color: #695549; width:50%; text-align:center; display:block; margin: 0 auto;"
            placeholder="Email"
            id="email"
            v-model="credentials.email"
            @keypress.enter="login"
            autofocus
          />
        </div>
        <div class="form-group">
          <input
            type="password"
            class="form-control"
            style="color: #695549; width:50%; text-align:center; display:block; margin: 0 auto;"
            placeholder="Password"
            id="password"
            v-model="credentials.password"
            @keypress.enter="login"
          />
        </div>
        <div v-if="!error_check_login">
          <p>이메일 또는 비밀번호를 다시 확인해주세요.</p>
        </div>
        <div>
          <b-button
            @click="login"
            type="submit"
            class="mb-2"
            style="width:50%; background-color: #695549;"
            >Login</b-button
          >
        </div>
        <div class="small">
          <!-- <router-link :to="{ name: 'Signup' }">회원가입</router-link>
      |
      <router-link :to="{ name: 'FindPassword' }">비밀번호찾기</router-link> -->
          <span style="color: #695549; cursor: pointer;" @click="toSignup"
            >회원가입</span
          >
          |
          <span style="color: #695549; cursor: pointer;"
            >비밀번호찾기</span
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  components: {},
  data: function() {
    return {
      cssProps: {
        backgroundImage: `url(${require("@/assets/Login/login.jpg")})`,
        width: "100vw",
        height: "100vh",
        position: "relative"
      },
      credentials: {
        email: "",
        password: ""
      },
      error_check_login: true
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add("large");
    },
    login: function() {
      // LOGIN 액션 실행
      // 서버와 통신(axios)을 해 토큰값을 얻어야 하므로 Actions를 호출.
      this.$store
        .dispatch("userStore/LOGIN", this.credentials)
        .then(() => {
          // 나중에 getUser() 함수 사용하기!!!
          // location 정보가 있으면 Home으로 보내기!
          // const userAddress = JSON.parse(localStorage.getItem('Login-token'))["user_address"]
          // if (userAddress !== null) {
          //   location.replace('/home')
          // } else {
          //   this.$router.replace('/location')
          // }
          window.location.href='/';
        })
        .catch(({ message }) => (this.msg = message));
    },
    toSignup: function() {
      this.$router.push({ name: "Register" });
    }
  },
  created: async function() {},
};
</script>

<style scoped>
.loginimg::before {
  background-color: #000;
  content: "";
  opacity: 0.5;
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
}
.loginimg h2 {
  color: #fff;
  text-align: center;
  font-weight: bold;
}
#box {
  display: block;
  width: 50%;
  position: absolute;
  left: 25%;
  margin-top: 15%;
}
</style>
