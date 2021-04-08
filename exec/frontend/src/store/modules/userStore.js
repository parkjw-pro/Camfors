import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

const userStore = {
  namespaced: true,

  state: {
    accessToken: null,
    email: "",
    nickname: "",
    changeState: "",
    userId: ""
  },
  getters: {
    getAccessToken(state) {
      return state.accessToken;
    },
    getEmail(state) {
      return state.email;
    },
    getNickname(state) {
      return state.nickname;
    },
    getUserId(state) {
      return state.userId;
    }
  },
  mutations: {
    LOGIN(state, payload) {
      state.accessToken = payload[1];
      state.email = payload[0][0]["email"];
      state.userId = payload[0][0]["user_id"];
      state.nickname = payload[0][0]["nickname"];

      localStorage.setItem("Login-token", payload[1]);
      localStorage.setItem("email", payload[0][0]["email"]);
      localStorage.setItem("user_id", payload[0][0]["user_id"]);
      localStorage.setItem("nickname", payload[0][0]["nickname"]);
    },
    LOGOUT(state) {
      state.accessToken = null;
      state.email = "";
      state.nickname = "";
      state.userId = "";
    },
    GetUserInfo(state) {
      state.accessToken = localStorage.getItem("Login-token");
      state.email = localStorage.getItem("email");
      state.userId = localStorage.getItem("user_id");
      state.nickname = localStorage.getItem("nickname");
    }
  },

  actions: {
    LOGIN(context, user) {
      console.log(SERVER_URL);
      localStorage.clear();
      return axios
        .post(`${SERVER_URL}/user/login`, user)
        .then(response => {
          context.commit("LOGIN", response.data);
          //axios.defaults.headers.common["auth0-token"] = ${response.data["token"]};
          //localStorage.setItem("token",${response.data["token"]});
          // axios
          //   .get(`${SERVER_URL}/user`)
          //   .then((response) => {
          //     console.log('axios login info');
          //     localStorage.setItem('Info-token', JSON.stringify(response.data.user));
          //   })
          //   .catch(() => {
          //     localStorage.clear();
          //     window.location.href = '/login';
          //     alert('로그인 실패 아이디및 비밀번호 확인 부탁드립니다.');
          //   });
        })
        .catch(() => {
          localStorage.clear();
          window.location.href = "/login";
          alert("로그인 실패 아이디및 비밀번호 확인 부탁드립니다.");
        });
    },
    LOGOUT(context) {
      context.commit("LOGOUT");
      localStorage.clear();
      //window.location.reload();
      window.location.href = "/";
    }
  }
};
export default userStore;
