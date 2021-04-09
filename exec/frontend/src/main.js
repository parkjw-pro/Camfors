import Vue from "vue";
import App from "./App";
import router from "./router";
import store from "./store/store";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

//fort-awesome
import { library as faLibrary } from "@fortawesome/fontawesome-svg-core";
import {
  faTrash,
  faAngleDown,
  faSearch
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Set up FontAwesome
faLibrary.add(faTrash, faAngleDown, faSearch);
Vue.component("font-awesome-icon", FontAwesomeIcon);

// Import Bootstrap an BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  beforeCreate() {
    if (localStorage.getItem("Login-token") != undefined) {
      this.$store.commit("userStore/GetUserInfo");
    }
  },
  render: h => h(App)
}).$mount("#app");
