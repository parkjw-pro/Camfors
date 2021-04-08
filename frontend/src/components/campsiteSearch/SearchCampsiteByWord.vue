<template>
  <div class="searchBox">
    <p style="text-align:left; color:white; font-size:30px;">단어로 찾기</p>
    <hr />
    <div class="search">
      <div class="input">
        <b-form-input
          id="input"
          v-model="word"
          placeholder="검색어를 입력하세요"
          @keyup.enter="searchWord"
        ></b-form-input>
      </div>
      <div class="searchButton">
        <b-button block class="button" variant="danger" v-on:click="searchWord"
          >검색하기</b-button
        >
        <b-button block class="button" v-on:click="changeIsTag"
          >태그로 검색</b-button
        >
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      word: ""
    };
  },
  computed: {
    btnStates() {
      return this.buttons.map(btn => btn.state);
    }
  },
  methods: {
    changeIsTag() {
      this.$emit("IsTag", false);
    },
    searchWord() {
      // console.log(this.word);
      this.$store.dispatch("campStore/searchByWord", this.word);
      this.word = "";
    }
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
.input {
  float: left;
  width: 70%;
  box-sizing: border-box;
  /* display: flex;
    align-items: center; */
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
