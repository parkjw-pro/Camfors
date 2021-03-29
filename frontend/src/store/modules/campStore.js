import axios from "axios";

const SERVER_URL = "http://localhost:8000";

const campStore = {
  namespaced: true,

  state: {
    detailInfo: [],
    searchWordList: [],
    searchTagList: [],
  },
  getters: {
    getDetailInfo(state) {
      return state.detailInfo;
    },
    getSearchWordList(state) {
      return state.searchWordList;
    },
    getSearchTagList(state) {
      return state.searchTagList;
    }
  },
  mutations: {
    setDetailInfo(state, payload) {
      state.detailInfo = payload;
    },
    setSearchWordList(state, payload) {
      state.searchWordList = payload;
    },
    setSearchTagList(state, payload) {
      state.searchTagList = payload;
    }
  },
  actions: {
    campsiteDetail(context, campsite_id) {
      axios({
        method: "get",
        url: `${SERVER_URL}/camp/getDetail/${campsite_id}`
      })
        .then(res => {
          console.log(res.data);
          context.commit("setDetailInfo", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    searchByWord(context, word) {
      console.log("searchByWord");
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/getwordresult/`,
        data: {
          word: word
        }
      })
        .then(res => {
          console.log(res.data);
          context.commit("searchWordList", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },

    searchByTag(context, tagList) {
      console.log("searchByTag");
      console.log(tagList);
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/gettagresult/`,
        data: {
          list: tagList
        }
      })
        .then(res => {
          console.log(res);
          context.commit("searchTagList", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
export default campStore;
