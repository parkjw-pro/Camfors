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
          #{{ btn.tag_name }}
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
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
export default {
  data() {
    return {
      buttons: [],
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
      // console.log("태그검색");
      for (let index = 0; index < this.buttons.length; index++) {
        if (this.buttons[index].state === true) {
          this.selectedTag.push(this.buttons[index].tag_id);
          this.selectedTagName.push(this.buttons[index].tag_name);
        }
      }
      this.$store.dispatch("campStore/searchByTagName", this.selectedTagName);
      this.$store.dispatch("campStore/searchByTag", this.selectedTag);
      this.selectedTag = [];
      this.selectedTagName = [];
      //this.$emit("IsTag", false);
    }
  },
  created() {
    axios({
      method: "get",
      url: `${SERVER_URL}/camp/gettaglist`
    })
      .then(res => {
        this.buttons = res.data;

        // state 추가
        for (let i = 0; i < this.buttons.length; i++) {
          this.$set(this.buttons[i], "state", false);
        }

        // console.log(this.buttons);
      })
      .catch(error => {
        console.log(error);
      });
  }
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
