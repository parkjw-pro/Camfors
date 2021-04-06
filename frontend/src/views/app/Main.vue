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
      </div>
      <div class="desc_scroll" id="scrollBtn" @click="moveToList">
        <p style="margin-bottom: 0;">Scroll</p>
        <font-awesome-icon icon="angle-down" class="fa-1x" />
      </div>
    </div>
    <!-- <div style="text-align: center; margin : 0 auto; width: 50%;"> -->
    <!-- <div style="background: linear-gradient(0deg, black 95%, #FF8C00);"> -->
    <div
      style="background: black;"
      v-for="(item, index) in tagList"
      :key="index"
    >
      <mainCampistList :tag="item" />
    </div>
    <!-- </div> -->
    <Footer />
  </div>
</template>

<script>
import "swiper/css/swiper.css";
import mainCampistList from "@/components/campsite/mainCampistList";
import Footer from "@/components/app/Footer";
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Main",
  components: {
    // Movie,
    // swiper,
    // swiperSlide,
    mainCampistList,
    Footer
    // Slider,
    // CampsiteList,
  },
  data: function() {
    return {
      tagList: [],
      visible: true,
      swiperOption: {
        direction: "vertical",
        pagination: {
          el: ".swiper-pagination",
          type: "bullets"
        }
      },
      userId: ""
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add("large");
    },
    moveToList() {
      var location = document.querySelector("#scrollBtn").offsetTop;
      window.scrollTo({ top: location + 30, behavior: "smooth" });
    },
    no_member() {
      console.log("로그인 안 한 유저입니다.");
      axios({
        method: "get",
        url: `${SERVER_URL}/camp/camppoptag`
      })
        .then(res => {
          console.log(res.data);
          this.tagList = res.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    member() {
      console.log("로그인 한 유저입니다.");
      axios({
        method: "get",
        url: `${SERVER_URL}/camp/listbyuser/${this.userId}/`
      })
        .then(res => {
          console.log(res.data);
          this.tagList = res.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    const userId = localStorage.getItem("user_id");
    this.userId = userId;
    if (this.userId == null) {
      this.no_member();
    } else {
      this.member();
    }
  }
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
