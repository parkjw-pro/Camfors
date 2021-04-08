import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

const campStore = {
  namespaced: true,

  state: {
    detailInfo: [],
    searchWordList: [],
    searchTagList: [[]],
    searchTagListName: [],
    searchWordName: "",
    pageNum: 0
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
    },
    getSearchTagListName(state) {
      return state.searchTagListName;
    },
    getSearchWordName(state) {
      return state.searchWordName;
    },
    getPageNum(state) {
      return state.pageNum;
    },
    getLoading(state) {
      return state.loading;
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
    },
    setSearchTagListName(state, payload) {
      state.searchTagListName = payload;
    },
    setSearchWordName(state, payload) {
      state.searchWordName = payload;
    }
  },
  actions: {
    campsiteDetail(context, campsite_id) {
      axios({
        method: "get",
        url: `${SERVER_URL}/camp/getDetail/${campsite_id}/`
      })
        .then(res => {
          context.commit("setDetailInfo", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    searchByWord(context, word) {
      context.commit("setSearchTagList", [[]]);
      context.commit("setSearchWordName", word);
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/getwordresult/`,
        data: {
          word: word
        }
      })
        .then(res => {
          context.commit("setSearchWordList", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },

    searchByTag(context, tagList) {
      context.commit("setSearchWordList", []);
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/gettagresult/`,
        data: tagList
      })
        .then(res => {
          context.commit("setSearchTagList", res.data);
          //context.commit("searchTagList", tagList);
        })
        .catch(error => {
          console.log(error);
        });
    },
    searchByTagName(context, tagList) {
      context.commit("setSearchTagListName", tagList);
    }
  }
};
export default campStore;
