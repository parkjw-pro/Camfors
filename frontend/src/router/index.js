import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/views/app/Main.vue";
import SearchCampsite from "@/views/campsite/SearchCampsite.vue";
<<<<<<< HEAD
=======
import CampsiteDetail from "@/views/campsite/CampsiteDetail.vue";
import Login from "@/views/member/Login.vue";
import Register from "@/views/member/Register.vue";
import Mypage from "@/views/member/Mypage.vue";

>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
Vue.use(VueRouter);

const routes = [
  {
    path: '/main',
    name: 'Main',
    component: Main,
  },
  {
<<<<<<< HEAD
    path: '/searchCampsite',
    name: 'SearchCampsite',
    component: SearchCampsite,
=======
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: Mypage,
  },
  {
    path: '/searchCampsite',
    name: 'SearchCampsite',
    component: SearchCampsite,
  },
  {
    path: '/campsiteDetail/:campsiteId',
    name: 'CampsiteDetail',
    component: CampsiteDetail,
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
  }
  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // }
];
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
 
});
export default router;