import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/views/app/Main.vue";
import SearchCampsite from "@/views/campsite/SearchCampsite.vue";
import CampsiteDetail from "@/views/campsite/CampsiteDetail.vue";
import Login from "@/views/member/Login.vue";
import Register from "@/views/member/Register.vue";
import Mypage from "@/views/member/Mypage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Main",
    component: Main
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      title: "캠퍼스 | 로그인"
    }
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: {
      title: "캠퍼스 | 회원가입"
    }
  },
  {
    path: "/mypage",
    name: "Mypage",
    component: Mypage,
    meta: {
      title: "캠퍼스 | 마이페이지"
    }
  },
  {
    path: "/searchCampsite",
    name: "SearchCampsite",
    component: SearchCampsite,
    meta: {
      title: "캠퍼스 | 검색페이지"
    }
  },
  {
    path: "/campsiteDetail/:campsiteId",
    name: "CampsiteDetail",
    component: CampsiteDetail,
    meta: {
      title: "캠퍼스 | 상세페이지"
    }
  }
];
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  /* It will change the title when the router is change*/
  /* 페이지 제목 바꾸기 */
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  next();
});
export default router;
