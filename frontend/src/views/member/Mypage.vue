<template>
  <!-- <div :style="cssProps"> -->
  <div :style="cssProps" class="loginimg">
    <div id="my1">
      <h3>내정보</h3>
    </div>
    <!-- <span id="my2">

    /></span>
    <div id="like">
      <mypagelike/>
    </div> -->
    <span id="my2" style="position:relative">
      <h3>좋아요</h3>
      <mypagelike
    /></span>
    <span id="my3"><h3>댓글</h3></span>
  </div>
</template>

<script>
import mypagelike from "@/components/campsite/mypagelike";
export default {
  name: "Mypage",
  components: {
    mypagelike
  },
  data: function() {
    return {
      cssProps: {
        backgroundImage: `url(${require("@/assets/mypage/mypage.jpg")})`,
        width: "100vw",
        height: "100vh",
        position: "relative"
      },
      credentials: {
        userId: "",
        password: ""
      },
      error_check_login: true
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add("large");
    },
    login: function() {
      // LOGIN 액션 실행
      // 서버와 통신(axios)을 해 토큰값을 얻어야 하므로 Actions를 호출.
      this.$store
        .dispatch("LOGIN", this.credentials)
        .then(() => {
          // 나중에 getUser() 함수 사용하기!!!
          // location 정보가 있으면 Home으로 보내기!
          // const userAddress = JSON.parse(localStorage.getItem('Login-token'))["user_address"]
          // if (userAddress !== null) {
          //   location.replace('/home')
          // } else {
          //   this.$router.replace('/location')
          // }
          this.selectBadge();
          this.$router.replace("/location/first");
        })
        .catch(({ message }) => (this.msg = message));
    },
    toSignup: function() {
      this.$router.push({ name: "Register" });
    }
  },
  created: async function() {},
  computed: {
    bagimg() {
      return {
        backgroundImage: `url${require("@/assets/Login/login.jpg")}`
      };
    }
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
}

#my2 {
  display: block;
  width: 33%;
  height: 40%;
  position: absolute;
  left: 15%;
  top: 50%;
  color: black;
  background-color: rgba(255, 255, 255, 0.356);
  opacity: 0.7;
}
#my3 {
  display: block;
  width: 33%;
  height: 40%;
  position: absolute;
  left: 53%;
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
