import axios from "axios";

const SERVER_URL = "http://localhost:8000";

const campStore = {
  namespaced: true,

  state: {
    detailInfo: []
  },
  getters: {
    getDetailInfo(state) {
      return state.detailInfo;
    }
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
        url: `${SERVER_URL}/camp/getDetail/${campsite_id}`
      })
        .then(res => {
          context.commit("setDetailInfo", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    searchByWord(context, word) {
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/getwordresult/`,
        data: {
          word: word
        }
      })
        .then(res => {
          console.log(res);
        })
        .catch(error => {
          console.log(error);
        });
    },

    searchByTag(context, tagList) {
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/gettagresult/`,
        data: {
          list: tagList
        }
      })
        .then(res => {
          console.log(res);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
export default campStore;
