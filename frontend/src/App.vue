<template>
  <div id="app" class="pb-5" style="position: relative; z-index: 2;"> 
    <div><Navbar /></div>
    <div style="position: relative; z-index: 1;">
      <router-view ></router-view>
    </div>
  </div>
</template>
<script>
import Navbar from '@/components/app/Navbar'
//import 'vue-select/dist/vue-select.css';
export default {
  name: 'App',
  components: {
    Navbar,
  },
  
}
</script>
<style>

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
</style>
