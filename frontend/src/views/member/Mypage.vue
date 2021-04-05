<template>
  <!-- <div :style="cssProps"> -->
  <div :style="cssProps" class="loginimg">
    <span id="my2" style="position:relative">
      <h3 style="font-family: 'Hanna', sans-serif;">내가 좋아하는 캠핑장</h3>
      <mypagelike :likeList="likeCampsiteList"
    /></span>
    <span id="my3"
      ><h3 style="font-family: 'Hanna', sans-serif;">내가 쓴 댓글</h3>
      <Comment v-if="this.reviewList" :commentList="this.reviewList" />
    </span>
  </div>
</template>

<script>
import mypagelike from "@/components/mypage/mypagelike";
import Comment from "@/components/campsiteDetail/Comment";
import axios from "axios";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
export default {
  name: "Mypage",
  components: {
    mypagelike,
    Comment
  },
  data: function() {
    return {
      cssProps: {
        backgroundImage: `url(${require("@/assets/mypage/mypage.jpg")})`,
        width: "100vw",
        height: "100vh",
        position: "relative"
      },
      userId: "",
      likeCampsiteList: [],
      reviewList: []
    };
  },
  methods: {
    getUserCampsite: function() {
      console.log(this.userId);
      axios
        .post(`${SERVER_URL}/user/like`, { user_id: this.userId })
        .then(res => {
          this.likeCampsiteList = res.data;
          console.log(res.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    getUserReview: function() {
      console.log(this.userId);
      axios
        .post(`${SERVER_URL}/user/review`, { user_id: this.userId })
        .then(res => {
          this.reviewList = res.data;
          console.log(res.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    const userId = localStorage.getItem("user_id");
    this.userId = userId;
    this.getUserCampsite();
    this.getUserReview();
  }
};
</script>

<style scoped>
.loginimg::before {
  background-color: rgb(0, 0, 0);
  content: "";
  opacity: 0.3;
  position: absolute;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
}
.loginimg h2 {
  color: #fff;
  text-align: center;
  font-weight: bold;
}

#my1 {
  display: block;
  width: 40%;
  height: 35%;
  position: absolute;
  left: 30%;
  top: 10%;
  color: black;
  background-color: rgba(255, 255, 255, 0.356);
  opacity: 0.7;
  pointer-events: none; 
}

#my2 {
  display: block;
  width: 66%;
  height: 35%;
  position: absolute;
  left: 15%;
  top: 10%;
  color: black;
  background-color: rgba(255, 255, 255, 0.356);
  opacity: 0.7;
}
#my3 {
  display: block;
  width: 66%;
  height: 42%;
  position: absolute;
  left: 15%;
  top: 50%;
  color: black;
  background-color: rgba(255, 255, 255, 0.356);
  opacity: 0.7;
}
#like {
  display: block;
  width: 33%;
  height: 40%;
  position: absolute;
  left: 15%;
  top: 50%;
  color: black;
  background-color: white;
}
</style>
