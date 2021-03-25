import Vue from "vue";
import Vuex from "vuex";
// import axios from "axios";

Vue.use(Vuex);

// const SERVER_URL = "http://localhost:8000";

export default new Vuex.Store({
  state: {
    // tagCampList: []
  },
  getters: {
    // getCampList(state) {
    //   return state.tagCampList;
    // },
  },
  mutations: {
    // setCampList(state, payload) {
    //   state.tagCampList = [];
    //   state.tagCampList = payload;
    // },
  },
  actions: {
    // getTagList(context, tag_id) {
    //   axios({
    //     method: "get",
    //     url: `${SERVER_URL}/camp/camptaglist/${tag_id}`,
    //   })
    //     .then((res) => {
    //       context.commit("setCampList", res.data);
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },
  },
  modules: {}
});
