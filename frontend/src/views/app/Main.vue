<template>
  <div id="main">
    <div class="main" style="background-color: black">
      <video
        height="40%"
        width="100%"
        playsinline
        autoplay
        muted
        loop
        poster="@/assets/mainpage/main.mp4"
      >
        <source :src="require('@/assets/mainpage/main.mp4')" type="video/mp4" />
      </video>
      <div class="text_area stagger-wrapper">
        <p class="stagger-item" style="font-size:3em">Camping For Smart</p>
        <p class="stagger-item">멋쟁이들을 위한 캠핑장 추천, 캠퍼스</p>
        <b-button class="stagger-item" variant="outline-light" @click="goSearch" style="font-family: system-ui; font-weight:900; letter-spacing: -2px;"><font-awesome-icon icon="search" class="fa-1x" /> 캠핑장 검색</b-button>
      </div>
      <div class="desc_scroll" id="scrollBtn" @click="moveToList">
        <p style="margin-bottom: 0;">Scroll</p>
        <font-awesome-icon icon="angle-down" class="fa-1x" />
      </div>
    </div>
    <!-- <div style="text-align: center; margin : 0 auto; width: 50%;"> -->
    <!-- <div style="background: linear-gradient(0deg, black 95%, #FF8C00);"> -->
    <div style="background: black;">
      <bestCampistList :list="bestCampsiteList" />
    </div>
    <div style="background: black;">
      <pulse-loader
        :loading="this.loading"
        :size="size"
        style="position:absolute; left:50%; top:120vh; transform: translateX(-50%); z-index:999; }"
      ></pulse-loader>
      <div v-for="(item, index) in tagList" :key="index">
        <mainCampistList :tag="item" v-on:endLoading="endLoading" />
      </div>
    </div>

    <!-- </div> -->
    <div style="height:50px; background:black;"></div>
    <Footer />
  </div>
</template>

<script>
import "swiper/css/swiper.css";
import mainCampistList from "@/components/campsite/mainCampistList";
import bestCampistList from '@/components/campsite/bestCampistList';
import Footer from "@/components/app/Footer";
import axios from "axios";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";
const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'Main',
  components: {
    // Movie,
    // swiper,
    // swiperSlide,
    bestCampistList,
    mainCampistList,
    Footer,
    PulseLoader
    // Slider,
    // CampsiteList,
  },
  data: function() {
    return {
      tagList: [],
      bestCampsiteList: [],
      visible: true,
      swiperOption: {
        direction: 'vertical',
        pagination: {
          el: '.swiper-pagination',
          type: 'bullets',
        },
      },
      userId: "",
      size: "20px",
      loading: true
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add('large');
    },
    moveToList() {
      var location = document.querySelector('#scrollBtn').offsetTop;
      window.scrollTo({ top: location + 30, behavior: 'smooth' });
    },
    no_member() {
      axios({
        method: 'get',
        url: `${SERVER_URL}/camp/camppoptag`,
      })
        .then((res) => {
          this.tagList = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    member() {
      axios({
        method: 'get',
        url: `${SERVER_URL}/camp/listbyuser/${this.userId}/`,
      })
        .then((res) => {
          this.tagList = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    bestCampsite() {
      axios({
        method: 'get',
        url: `${SERVER_URL}/camp/camplikeslist/`,
      })
        .then((res) => {
          this.bestCampsiteList = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    endLoading() {
      setTimeout(() => {
        this.loading = false;
      }, 500);
    },
    goSearch: function() {
      this.$router.go(this.$router.push({ name: "SearchCampsite" }));
    },
  },
  created() {
    const userId = localStorage.getItem('user_id');
    this.userId = userId;
    this.bestCampsite();
    if (this.userId == null) {
      this.no_member();
    } else {
      this.member();
    }
  },
};
</script>

<style>
/* 파스텔 컬러 */
.color_red {
  background-color: #f5d5cb;
}

.color_yellow {
  background-color: #f6f6eb;
}

.color_green {
  background-color: #d7ecd9;
  background-color: black;
}

.color_purple {
  background-color: #d5d6ea;
}
</style>
<style scoped>
.swiper-slide {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.swiper-container {
  height: 500px;
}

.main {
  position: relative;
}

.text_area {
  z-index: 100;
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translateY(-50%);
  transform: translateY(-50%);
  width: 1200px;
  margin: -30px 0 0 -600px;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  color: rgba(255, 255, 255, 0.829);
  font-size: 20px;
  font-family: system-ui, -SF Pro Text, Helvetica, Roboto, sans-serif;
  font-weight: 900;
  letter-spacing: -2px;
}

.desc_scroll {
  z-index: 110;
  position: absolute;
  bottom: 36px;
  left: 50%;
  -webkit-transform: translateX(-50%);
  transform: translateX(-50%);
  font-size: 1.1rem;
  line-height: 1.3rem;
  color: white;
  font-family: system-ui, -SF Pro Text, Helvetica, Roboto, sans-serif;
  text-align: center;
  font-size: 12px;
  cursor: pointer;
}

@keyframes showText {
  from {
    transform: translateY(20px);
    opacity: 0;
  }

  to {
    transform: translateY(0px);
    opacity: 1;
  }
}
.stagger-item {
  animation: showText 1s;
  animation-fill-mode: both;
}

.stagger-item:nth-child(1) {
  animation-delay: 0.1s;
}

.stagger-item:nth-child(2) {
  animation-delay: 0.2s;
}
</style>
