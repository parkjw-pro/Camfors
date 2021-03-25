import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const SERVER_URL = "http://localhost:8000";

export default new Vuex.Store({
  state: {
    detailInfo: [],
  },
  getters: {
    getDetailInfo(state) {
      return state.detailInfo;
    },
  },
  mutations: {
    setDetailInfo(state, payload) {
      state.detailInfo = payload;
    }
  },
  actions: {
    campsiteDetail(context, campsite_id) {
      axios({
        method: "get",
        url: `${SERVER_URL}/camp/getDetail/${campsite_id}`,
      })
        .then(res => {
          context.commit("setDetailInfo", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
  modules: {},
});
