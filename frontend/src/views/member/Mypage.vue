<template>
  <!-- <div :style="cssProps"> -->
  <div :style="cssProps" class="loginimg">
    <div id="box">
      <h2>마이페이지</h2>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'Mypage',
  components: {},
  data: function() {
    return {
      cssProps: {
        backgroundImage: `url(${require('@/assets/mypage/mypage.jpg')})`,
        width: '1920px',
        height: '1080px',
        position: 'relative',
      },
      credentials: {
        userId: '',
        password: '',
      },
      error_check_login: true,
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add('large');
    },
    login: function() {
      // LOGIN 액션 실행
      // 서버와 통신(axios)을 해 토큰값을 얻어야 하므로 Actions를 호출.
      this.$store
        .dispatch('LOGIN', this.credentials)
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
          this.$router.replace('/location/first');
        })
        .catch(({ message }) => (this.msg = message));
    },
    toSignup: function() {
      this.$router.push({ name: 'Register' });
    },
  },
  created: async function() {},
  computed: {
    bagimg() {
      return {
        backgroundImage: `url${require('@/assets/Login/login.jpg')}`,
      };
    },
  },
};
</script>

<style scoped>
.loginimg::before {
  background-color: #000;
  content: '';
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
</style>
