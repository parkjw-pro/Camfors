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
          <b-col align-self="right">
            <ValidationProvider
              name="이메일"
              rules="required|email"
              v-slot="{ errors }"
            >
              <b-form-group>
                <label
                  style="float:left; padding-right:10px; padding-top:5px; color : white"
                  for="email"
                  >이메일:
                </label>
                <b-form-input
                  type="email"
                  class="ml-5"
                  style="width:50%; float:left;"
                  v-model="credentials.email"
                  placeholder="이메일을 입력하세요"
                  required
                  @keypress.enter="check_user_email"
                ></b-form-input>
                <b-button
                  id="btn_signup"
                  style="margin-top:3px"
                  size="sm"
                  @click="check_user_email"
                  >확인</b-button
                >
                <br />
                <br />
                <small
                  id="error3"
                  class="text-danger"
                  style=" margin-top:5px"
                  >{{ errors[0] }}</small
                >
              </b-form-group>
            </ValidationProvider>
          </b-col>
        </b-row>
        <b-row id="accountBox">
          <b-col align-self="left">
            <ValidationProvider
              name="비밀번호"
              rules="required|min:6"
              v-slot="{ errors }"
            >
              <b-form-group>
                <label
                  style="float:left; padding-right:17px; padding-top:5px; color : white"
                  for="password"
                  >비밀번호:
                </label>
                <b-form-input
                  type="password"
                  class="mx-4"
                  style="width:50%; float:left; font-color : black;"
                  v-model="credentials.password"
                  placeholder="비밀번호를 입력하세요"
                  required
                  @keypress.enter="onSubmit()"
                ></b-form-input>
                <br />
                <br />
                <small
                  id="error5"
                  class="text-danger"
                  style=" margin-top:5px; color : white"
                  >{{ errors[0] }}</small
                >
              </b-form-group>
            </ValidationProvider>
          </b-col>
        </b-row>
        <b-row id="accountBox">
          <b-col align-self="left">
            <ValidationProvider
              name="비밀번호 확인"
              rules="required|confirmed:비밀번호"
              v-slot="{ errors }"
            >
              <b-form-group>
                <label
                  style="float:left; padding-right:10px; padding-top:5px; color : white"
                  for="password_confirmation"
                  >비밀번호확인:
                </label>
                <b-form-input
                  type="password"
                  style="width:50%; float:left;"
                  v-model="password_confirmation"
                  placeholder="비밀번호를 한 번 더 입력하세요"
                  required
                  @keypress.enter="onSubmit()"
                ></b-form-input>
                <br />
                <br />
                <small
                  id="error6"
                  class="text-danger"
                  style=" margin-top:5px"
                  >{{ errors[0] }}</small
                >
              </b-form-group>
            </ValidationProvider>
          </b-col>
        </b-row>
        <!-- 2.1.2 닉네임 -->
        <b-row id="accountBox">
          <b-col align-self="left">
            <ValidationProvider
              name="닉네임"
              rules="required|min:2"
              v-slot="{ errors }"
            >
              <b-form-group>
                <label
                  style="float:left; padding-right:10px; padding-top:5px; color : white"
                  for="nickname"
                  >닉네임:
                </label>
                <b-form-input
                  type="text"
                  class="ml-5"
                  style="width:50%; float:left;"
                  v-model="credentials.nickname"
                  placeholder="개성있는 닉네임을 입력하세요"
                  required
                ></b-form-input>
                <br />
                <br />
                <small
                  id="error2"
                  class="text-danger"
                  style=" margin-top:5px"
                  >{{ errors[0] }}</small
                >
              </b-form-group>
            </ValidationProvider>
          </b-col>
        </b-row>
      </b-col>
      <!-- 버튼 -->
      <div>
        <b-button
          id="btn_signup"
          class="mx-3"
          @click="$router.push({ name: 'Login' })"
        >
          로그인 페이지
        </b-button>
        <b-button id="btn_signup" class="mx-3" @click="onSubmit()">
          가입완료
        </b-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ValidationProvider } from "vee-validate";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  components: {
    ValidationProvider
    // extend,
  },
  name: "Register",
  data() {
    return {
      cssProps: {
        backgroundImage: `url(${require("@/assets/register/register.jpg")})`,
        width: "100vw",
        height: "100vh",
        position: "relative"
      },
      credentials: {
        nickname: "",
        email: "",
        password: ""
      },
      password_confirmation: "",
      emailCode: "",

      checkEmail: true,
    };
  },
  methods: {
    onSubmit() {
      if (
        this.checkEmail == false ||
        document.getElementById("error5").innerHTML != "" ||
        document.getElementById("error6").innerHTML != ""
      ) {
        alert("중복체크 및 유효성 검사 확인 바랍니다.");
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
    },
    check_user_email: function() {
      if (
        this.checkId == false ||
        this.credentials.email == "" ||
        document.getElementById("error3").innerHTML != ""
      ) {
        alert("이메일 다시 입력 바랍니다.");
        this.credentials.email = "";
      } else {
        axios
          .post(`${SERVER_URL}/user/email`, this.credentials)
          .then(() => {
            alert("사용 가능한 이메일 입니다.");
            this.checkEmail = true;
          })
          .catch(() => {
            if (this.credentials.email != "") {
              alert("현재 사용중인 이메일 입니다.");
              this.credentials.email = "";
            }
          });
      }
    },
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
  display: block;
  width: 50%;
  position: absolute;
  left: 25%;
  margin-top: 8%;
}
</style>
