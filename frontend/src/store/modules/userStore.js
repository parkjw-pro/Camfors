import axios from 'axios';

const SERVER_URL = process.env.VUE_APP_SERVER_URL

const userStore = {
  namespaced: true,

  state: {
    accessToken: null,
    email: '',
    nickname: '',
    changeState: '',
  },
  getters: {
    getAccessToken(state) {
      if (localStorage.getItem('Login-token') != undefined) {
        //return localStorage.getItem('Login-token');
        return localStorage.getItem('auth-token');
      }
      return state.accessToken;
      //return state.accessToken = localStorage.getItem('auth-token');
    },
    getEmail(state) {
      if (localStorage.getItem('Login-token') != undefined) {
        return JSON.parse(localStorage.getItem('Login-token'))['email'];
      }
      return state.email;
    },
    getNickname(state) {
      if (localStorage.getItem('Login-token') != undefined) {
        return JSON.parse(localStorage.getItem('Login-token'))['nickname'];
      }
      return state.nickname;
    },
  },
  mutations: {
    LOGIN(state, payload) {
      state.accessToken = payload['auth-token'];
      state.email = payload['email'];
      state.nickname = payload['nickname'];
    },
    LOGOUT(state) {
      state.accessToken = null;
      state.email = '';
      state.nickname = '';
    },
  },

  actions: {
    LOGIN(context, user) {
      console.log(SERVER_URL);
      localStorage.clear();
      return axios
        .post(`${SERVER_URL}/user/login`, user)
        .then((response) => {
          console.log('axios login');
          context.commit('LOGIN', response.data);
          localStorage.setItem('auth-token', response.data['auth-token']);
          //axios.defaults.headers.common["auth0-token"] = ${response.data["auth-token"]};
          //localStorage.setItem("auth-token",${response.data["auth-token"]});
          axios.defaults.headers.common['auth-token'] = localStorage.getItem('auth-token');

          if (localStorage.getItem('Login-token') == undefined) {
            localStorage.setItem('Login-token', JSON.stringify(response.data));
          }

          axios
            .get(`${SERVER_URL}/user`)
            .then((response) => {
              console.log('axios login info');
              localStorage.setItem('Info-token', JSON.stringify(response.data.user));
            })
            .catch(() => {
              localStorage.clear();
              window.location.href = '/login';
              alert('로그인 실패 아이디및 비밀번호 확인 부탁드립니다.');
            });
        })
        .catch(() => {
          localStorage.clear();
          window.location.href = '/login';
          alert('로그인 실패 아이디및 비밀번호 확인 부탁드립니다.');
        });
    },
    LOGOUT(context) {
      context.commit('LOGOUT');
      axios.defaults.headers.common['auth-token'] = undefined;
      localStorage.clear();
      //window.location.reload();
      window.location.href = '/';
    },
  },
};
export default userStore;
