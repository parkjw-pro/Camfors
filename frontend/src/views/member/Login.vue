<template>
  <!-- <div :style="cssProps"> -->
  <div>
    <div :style="cssProps" class="loginimg">
      <div id="box">
        <h2 style="margin-bottom:40px;">로그인</h2>
        <div class="form-group">
          <input
            type="text"
            class="form-control"
            style="color: #695549; width:80%; text-align:center; display:block; margin: 0 auto;"
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
            style="color: #695549; width:80%; text-align:center; display:block; margin: 0 auto;"
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
            variant="secondary"
            style="width:50%;"
            >Login</b-button
          >
        </div>
        <div class="small">
          <!-- <span style="color: #fff; cursor: pointer;" @click="toSignup"
            >비밀번호찾기
          </span> -->
          <span
            style="color: rgba(161, 161, 161); cursor: pointer;"
            @click="toSignup"
            >회원가입
          </span>
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
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center"
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
          // 로컬스토리지 정보가 있으면 홈화면으로, 아니면 다시 로그인화면으로
          const token = localStorage.getItem("Login-token");
          if (token !== null) {
            location.replace("/");
          } else {
            this.$router.replace("/login");
          }
        })
        .catch(({ message }) => (this.msg = message));
    },
    toSignup: function() {
      this.$router.push({ name: "Register" });
    }
  },
  created: async function() {}
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
  position: absolute;
  vertical-align: middle;
  width: 400px;
  height: 400px;
  padding: 30px;
  padding-top: 60px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(20, 20, 20, 0.747);
}

.form-group {
  margin-bottom: 1.5rem;
}
</style>
