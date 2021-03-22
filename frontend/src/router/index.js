import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/views/app/Main.vue";
import SearchCampsite from "@/views/campsite/SearchCampsite.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: '/main',
    name: 'Main',
    component: Main,
  },
  {
    path: '/searchCampsite',
    name: 'SearchCampsite',
    component: SearchCampsite,
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