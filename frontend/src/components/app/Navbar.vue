<template>
   <div>
  <b-navbar class="navbar" :class="{'change_color': scrollPosition > 50}" toggleable="lg" type="dark" fixed="top">
    <b-navbar-brand href="/">Phoenix</b-navbar-brand>
        <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/searchCampsite">나만의 캠핑장을 찾아보세요</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          
          <b-form-input size="sm" class="mr-sm-2" placeholder=""></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          
        </b-nav-form>

        <b-nav-item href="#">로그인</b-nav-item>
        <b-nav-item href="#">로그아웃</b-nav-item>
        <b-nav-item href="#">마이페이지</b-nav-item>

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
    }
  }
  
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