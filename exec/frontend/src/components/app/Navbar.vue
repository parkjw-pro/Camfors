<template>
  <div>
    <b-navbar
      class="navbar"
      :class="{ change_color: scrollPosition > 50 }"
      type="dark"
      fixed="top"
    >
      <b-navbar-brand href="/" style="margin-right:0 3px; padding:0px"
        ><img height="35px" width="80px" src="@/assets/logo3.png"
      /></b-navbar-brand>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item @click="goSearch"
            ><font-awesome-icon icon="search" class="fa-1x" /> 나만의 캠핑장을
            찾아보세요</b-nav-item
          >
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if="!login" @click="goLogin">로그인</b-nav-item>
          <b-nav-item v-if="login" @click="logout">로그아웃</b-nav-item>
          <b-nav-item v-if="login" @click="goMypage">마이페이지</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!-- <b-navbar :class="{'headroom--unpinned': scrolled}"  v-on="handleScroll" class="headroom header">Header</b-navbar> -->
  </div>
</template>
<script>
export default {
  name: "Navbar",
  props: {
    login: Boolean
  },
  data() {
    return {
      scrollPosition: null
    };
  },
  mounted() {
    window.addEventListener("scroll", this.updateScroll);
  },
  methods: {
    updateScroll() {
      this.scrollPosition = window.scrollY;
    },
    goLogin: function() {
      // 리뷰 작성 페이지로 넘어가준다!!
      // console.log("보냅니다", this.store);
      // console.log("로그인페이지로 이동");
      this.$router.go(this.$router.push({ name: "Login" }));
    },
    goMypage: function() {
      // 리뷰 작성 페이지로 넘어가준다!!
      // console.log("보냅니다", this.store);
      // console.log("마이페이지로 이동");
      this.$router.go(this.$router.push({ name: "Mypage" }));
    },
    goSearch: function() {
      // console.log("검색페이지로 이동");
      this.$router.go(this.$router.push({ name: "SearchCampsite" }));
    },
    logout: function() {
      this.$store
        .dispatch("userStore/LOGOUT")
        .then(() => {
          // this.$router.push({ name: 'Home' })
          this.$router.push({ name: "/" });
        })
        .catch(({ message }) => (this.msg = message));
    }
  }
};
</script>

<style scoped>
.navbar {
  background: rgba(0, 0, 0, 0);
  font-family: LineSeed, system-ui, -SF Pro Text, Helvetica, Roboto, sans-serif;
  height: 88px;
  font-size: 16px;
  font-weight: 600;
  /* border-bottom: solid 1px rgba(226, 220, 220); */
  border-bottom: solid 1px;
  border-color: rgba(255, 255, 255, 0.3);
}
.change_color {
  background-color: black;
  border-bottom: solid 0px;
}

.navbar-dark .navbar-nav .nav-link {
  color: #f8f9fa;
}

@media (min-width: 1281px) {
  .navbar-expand-lg .navbar-nav .nav-link {
    padding-right: 1rem;
    padding-left: 1rem;
  }
}
</style>
