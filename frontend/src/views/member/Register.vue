<template>
  <!-- <div :style="cssProps"> -->
  <div :style="cssProps" class="regisimg">
    <div id="box">
      <!-- 1. 제목 -->
      <div id="title" class="mb-5">
        <h2>회원가입</h2>
      </div>
      <!-- 2. 내용 -->
      <!-- 2.1 input창 -->
      <b-col class="mx-3">
        <!-- 2.1.1 아이디 -->
        <b-row id="accountBox">
          <b-col>

              <b-form-group>
                <label
                  style="float:left; padding-right:10px; padding-top:5px; color : white"
                  for="email"
                  >이메일:
                </label>
                <b-form-input
                  type="email"
                  class="ml-5"
                  style="width:60%; float:left;"
                  v-model="credentials.email"
                  placeholder="이메일을 입력하세요"
                  required
                  @keypress.enter="onSubmit()"
                ></b-form-input>
                <br />
                <br />
              </b-form-group>
          </b-col>
        </b-row>
        <b-row id="accountBox">
          <b-col>
              <b-form-group>
                <label
                  style="float:left; padding-right:17px; padding-top:5px; color : white"
                  for="password"
                  >비밀번호:
                </label>
                <b-form-input
                  type="password"
                  class="mx-4"
                  style="width:60%; float:left; color:black;"
                  v-model="credentials.password"
                  placeholder="비밀번호를 입력하세요(6자 이상)"
                  required
                  @keypress.enter="onSubmit()"
                ></b-form-input>
                <br />
                <br />
              </b-form-group>
          </b-col>
        </b-row>
        <b-row id="accountBox">
          <b-col>
              <b-form-group>
                <label
                  style="float:left; padding-right:10px; padding-top:5px; color : white"
                  for="password_confirmation"
                  >비밀번호확인:
                </label>
                <b-form-input
                  type="password"
                  style="width:60%; float:left;"
                  v-model="password_confirmation"
                  placeholder="비밀번호를 한 번 더 입력하세요"
                  required
                  @keypress.enter="onSubmit()"
                ></b-form-input>
                <br />
                <br />
              </b-form-group>
          </b-col>
        </b-row>
        <!-- 2.1.2 닉네임 -->
        <b-row id="accountBox">
          <b-col>
              <b-form-group>
                <label
                  style="float:left; padding-right:10px; padding-top:5px; color : white"
                  for="nickname"
                  >닉네임:
                </label>
                <b-form-input
                  type="text"
                  class="ml-5"
                  style="width:60%; float:left;"
                  v-model="credentials.nickname"
                  placeholder="개성있는 닉네임을 입력하세요(2자 이상)"
                  required
                  @keypress.enter="onSubmit()"
                ></b-form-input>
                <br />
                <br />
              </b-form-group>
          </b-col>
        </b-row>
      </b-col>
      <!-- 버튼 -->
      <div>
        <b-button
          variant="secondary"
          style="width:30%; margin-bottom:10px;"
          class="mx-3"
          @click="onSubmit()"
        >
          가입 완료
        </b-button>
        <div class="small">
          <span
            style="color: rgba(161, 161, 161); cursor: pointer;"
            @click="$router.push({ name: 'Login' })"
            >로그인
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  components: {
    // extend,
  },
  name: "Register",
  data() {
    return {
      cssProps: {
        backgroundImage: `url(${require("@/assets/register/register.jpg")})`,
        width: "100vw",
        height: "100vh"
      },
      credentials: {
        nickname: "",
        email: "",
        password: ""
      },
      password_confirmation: "",
      emailCode: "",

      checkEmail: false
    };
  },
  methods: {
    onSubmit() {
      if (
        (this.credentials.email.length<6)||
        (this.credentials.password.length<6)||
        (this.credentials.password!=this.password_confirmation)||
        (this.credentials.nickname.length<2)
      ) {
        alert("회원가입 양식에 맞춰주세요!");
      } else {
        axios
          .post(`${SERVER_URL}/user/signup`, this.credentials)
          .then(() => {
            alert("회원가입 성공");
            window.location.href = "/login";
          })
          .catch(() => {
            alert("서버에 문제가 생겼습니다. 다시 가입 바랍니다.");
            window.location.href = "/register";
          });
      }
    }
  }
};
</script>

<style scoped>
.regisimg::before {
  background-color: #000;
  content: "";
  opacity: 0.5;
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
}
.regisimg h2 {
  color: #fff;
  text-align: center;
  font-weight: bold;
}

#btn_signup {
  background-color: #695549;
}

input[type="password"] {
  font: small-caption;
  font-size: 16px;
}
::placeholder {
  font-family: "Jeju Gothic", sans-serif;
}

#box {
  position: absolute;
  width: 600px;
  height: 500px;
  padding: 30px;
  padding-top: 60px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(20, 20, 20, 0.747);
}
</style>
