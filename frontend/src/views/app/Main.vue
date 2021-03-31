<template>
  <div id="main">
    <div style="background-color: black">
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
    </div>
    <!-- <div style="text-align: center; margin : 0 auto; width: 50%;"> -->
    <div
      style="background-color: black"
      v-for="(item, index) in tagList"
      :key="index"
    >
      <swipertest :tag="item" />
    </div>
  </div>
</template>

<script>
import "swiper/css/swiper.css";
import swipertest from "@/components/campsite/swipertest";

export default {
  name: "Main",
  components: {
    // Movie,
    // swiper,
    // swiperSlide,
    swipertest
    // Slider,
    // CampsiteList,
  },
  data: function() {
    return {
      tagList: [
        { name: "산과 함께하는 곳", id: 6 },
        { name: "바다가 보이는 곳", id: 7 },
        { name: "산책하기 좋은 곳", id: 12 },
        { name: "가족들과 가기 좋은", id: 5 },
        { name: "아이들이랑 가고 싶은 곳", id: 13 }
      ],
      swiperOption: {
        direction: "vertical",
        pagination: {
          el: ".swiper-pagination",
          type: "bullets"
        }
      }
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add("large");
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
</style>
