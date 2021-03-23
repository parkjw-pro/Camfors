<template>
   <div>
  <b-navbar class="navbar" :class="{'change_color': scrollPosition > 50}" toggleable="lg" type="dark" fixed="top">
<<<<<<< HEAD
    <b-navbar-brand href="/">Phoenix</b-navbar-brand>
=======
    <b-navbar-brand href="/main">Phoenix</b-navbar-brand>
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
        <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/searchCampsite">나만의 캠핑장을 찾아보세요</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
<<<<<<< HEAD
        <!-- <b-nav-form> -->
          
          <!-- <b-form-input size="sm" class="mr-sm-2" placeholder=""></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button> -->
          
        <!-- </b-nav-form> -->

        <b-nav-item href="#">로그인</b-nav-item>
        <b-nav-item href="#">로그아웃</b-nav-item>
        <b-nav-item href="#">마이페이지</b-nav-item>
=======
        <b-nav-form>
          
          <b-form-input size="sm" class="mr-sm-2" placeholder=""></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          
        </b-nav-form>

        <b-nav-item @click="goLogin">로그인</b-nav-item>
        <b-nav-item href="#">로그아웃</b-nav-item>
        <b-nav-item @click="goMypage">마이페이지</b-nav-item>
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8

      </b-navbar-nav>
    </b-collapse>


  </b-navbar>
  <!-- <b-navbar :class="{'headroom--unpinned': scrolled}"  v-on="handleScroll" class="headroom header">Header</b-navbar> -->
</div>
</template>
<script> 
export default {
  name: 'Navbar',
  data() {
    return {
      scrollPosition: null
    };
  },
 mounted() {
    window.addEventListener('scroll', this.updateScroll);
  },
  methods: {
    updateScroll() {
       this.scrollPosition = window.scrollY
<<<<<<< HEAD
    }
  }
=======
    },
    goLogin: function() {
      // 리뷰 작성 페이지로 넘어가준다!!
      // console.log("보냅니다", this.store);
      console.log("로그인페이지로 이동")
      this.$router.push({ name: 'Login'});
    },
    goMypage: function() {
      // 리뷰 작성 페이지로 넘어가준다!!
      // console.log("보냅니다", this.store);
      console.log("마이페이지로 이동")
      this.$router.push({ name: 'Mypage'});
    },

  }

>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
  
}




</script>

<style scoped>
.navbar {
  background:rgba(0,0,0,0.2);
}
.change_color {
  background-color:black;
}

</style>