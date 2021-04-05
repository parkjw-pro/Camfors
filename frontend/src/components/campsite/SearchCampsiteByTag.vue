<template>
  <div class="searchBox">
    <p style="text-align:left; color:white; font-size:30px;">#추천태그</p>
    <hr />
    <div class="search">
      <div class="tagGroup">
        <b-button
          v-for="(btn, idx) in buttons"
          :key="idx"
          :pressed.sync="btn.state"
          variant="outline-light"
        >
          {{ btn.caption }}
        </b-button>
      </div>
      <div class="searchButton">
        <b-button block class="button" variant="danger" v-on:click="searchTag"
          >검색하기</b-button
        >
        <b-button block class="button" v-on:click="changeIsTag"
          >단어로 검색</b-button
        >
      </div>
    </div>
  </div>
</template>
<script>
// const SERVER_URL = process.env.VUE_APP_SERVER_URL;
// import axios from "axios";
export default {
  data() {
    return {
      buttons: [
        { caption: "#반려견 동반이 가능한", state: false, id: 5 },
        { caption: "#산이 보이는", state: false, id: 6 },
        { caption: "#바다가 보이는", state: false, id: 7 },
        { caption: "#계곡 옆에 있는", state: false, id: 8 },
        { caption: "#도심 속에 있는", state: false, id: 9 },
        { caption: "#섬 속에 있는", state: false, id: 10 },
        { caption: "#물 놀이 하기 좋은", state: false, id: 11 },
        { caption: "#산책 하기 좋은", state: false, id: 12 },
        { caption: "#아이들 놀기 좋은", state: false, id: 13 },
        { caption: "#카라반", state: false, id: 14 },
        { caption: "#글램핑", state: false, id: 15 },
        { caption: "#자동차", state: false, id: 16 },
        { caption: "#체험 프로그램이 있는", state: false, id: 17 },
        { caption: "#장비 대여가 가능한", state: false, id: 18 },
        { caption: "#개인 트레일러 동반 가능한", state: false, id: 19 }
      ],
      checkedTag: [],
      selectedTag: [],
      selectedTagName: []
    };
  },
  computed: {
    btnStates() {
      return this.buttons.map(btn => btn.state);
    }
  },
  methods: {
    changeIsTag() {
      this.$emit("IsTag", true);
    },
    searchTag() {
      console.log("태그검색");
      for (let index = 0; index < this.buttons.length; index++) {
        if (this.buttons[index].state === true) {
          this.selectedTag.push(this.buttons[index].id);
          this.selectedTagName.push(
            this.buttons[index].caption.substring(
              1,
              this.buttons[index].caption.length
            )
          );
        }
      }
      this.$store.dispatch("campStore/searchByTagName", this.selectedTagName);
      this.$store.dispatch("campStore/searchByTag", this.selectedTag);
      this.selectedTag = [];
      this.selectedTagName = [];
      //this.$emit("IsTag", false);
    }
  },
  // created() {
  //   axios({
  //     method: "get",
  //     url: `${SERVER_URL}/camp/gettaglist`
  //   })
  //     .then(res => {
  //       this.commentList = [];
  //       console.log(res.data);
  //       if (res.data !== "리뷰가 없습니다") this.commentList = res.data;
  //     })
  //     .catch(error => {
  //       console.log(error);
  //   });
  // }
};
</script>
<style scoped>
.searchBox {
  width: 100%;
  height: 70vh;
  background-image: url("../../assets/SearchPageImage2.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  padding: 10%;
}

.search {
  display: flex;
}
.tagGroup {
  float: left;
  width: 70%;
  box-sizing: border-box;
}
.searchButton {
  float: left;
  margin: 0px 5%;
  width: 30%;
  box-sizing: border-box;
}

button {
  margin: 0 1% 8px 0;
}

hr {
  background-color: white;
}
</style>
