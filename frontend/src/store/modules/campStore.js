import axios from "axios";

const SERVER_URL = "http://www.camfors.shop:8000";

const campStore = {
  namespaced: true,

  state: {
    detailInfo: [],
    searchWordList: [],
    searchTagList: [[]],

  },
  getters: {
    getDetailInfo(state) {
      return state.detailInfo;
    },
    getSearchWordList(state) {
      console.log(state.searchWordList[0]);
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
    },
    createReview(state, payload){
      state.review = payload;
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
          context.commit("setSearchWordList", res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },

    searchByTag(context, tagList) {
      console.log("searchByTag");
      context.commit("setSearchTagList", tagList);
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/gettagresult/`,
        data: {
          list: tagList
        }
      })
        .then(res => {
          console.log(res);
          context.commit("setSearchTagList", res.data);
          //context.commit("searchTagList", tagList);
        })
        .catch(error => {
          console.log(error);
        });
    },

    createReview(user_id, campsite_id, review) {
      console.log("createReview");
      // context.commit("createReview", review);
      axios({
        method: "post",
        url: `${SERVER_URL}/camp/createreview/`,
        data: {
          user_id: user_id,
          campsite_id: campsite_id,
          review: review
        }
      })
        .then(res => {
          console.log(res);
        })
        .catch(error => {
          console.log(error);
        });
    },
  }
};
export default campStore;
