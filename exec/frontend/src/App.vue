<template>
  <div id="app" style="position: relative; z-index: 2;">
    <div><Navbar :login="login" /></div>
    <div style="position: relative; z-index: 1;">
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
import Navbar from "@/components/app/Navbar";
//import 'vue-select/dist/vue-select.css';
export default {
  name: "App",
  components: {
    Navbar
  },
  data: function() {
    return {
      login: false
    };
  },
  mounted() {
    if (localStorage.getItem("Login-token") != undefined) {
      this.login = true;
    }
  }
};
</script>
<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);
/* 2번 폰트 - 나눔펜 스크립트 */
@import url("https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap");
/* 3번 폰트 - Hanna */
@import url(//fonts.googleapis.com/earlyaccess/hanna.css);

@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#box {
  display: block;
  width: 50%;
  position: absolute;
  left: 25%;
  margin-top: 15%;
}
</style>
