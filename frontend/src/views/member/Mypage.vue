<template>
  <!-- <div :style="cssProps"> -->
  <div :style="cssProps" class="loginimg">
    <div id="mypage">
      <h2>마이페이지</h2>
    </div>
    <div id="my1">
      내정보
    </div>
    <span id="my2">좋아요</span>
    <span id="my3">리뷰</span>
  </div>
</template>

<script>
export default {
  name: "Mypage",
  components: {},
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
<<<<<<< HEAD
  background-color: #000;
  content: "";
=======
  background-color: rgb(0, 0, 0);
  content: '';
>>>>>>> 88cfdcf79a570418e42c9b4b8f95772101810bba
  opacity: 0.5;
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

#mypage {
  display: block;
  width: 50%;
  position: absolute;
  left: 25%;
  margin-top: 5%;
}
#my1 {
  display: block;
  width: 50%;
  position: absolute;
  left: 25%;
  margin-top: 17%;
  color: aqua;
}
#my2 {
  display: block;
  width: 50%;
  position: absolute;
  left: 10%;
  margin-top: 30%;
  color: aqua;
}
#my3 {
  display: block;
  width: 50%;
  position: absolute;
  left: 40%;
  margin-top: 30%;
  color: aqua;
}
</style>
