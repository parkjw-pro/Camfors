<template>
  <div id="main">
    <div>
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
      style="background-color: #FFFFF0"
      v-for="(item, index) in tagList"
      :key="index"
    >
      <swipertest :tag="item" />
    </div>
  </div>
</template>

<script>
import "swiper/swiper-bundle.css";
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
        { name: "반려견 동반 가능", id: 5 },
        { name: "아이들이랑 가고 싶은 곳", id: 13 },
        { name: "산책하기 좋은 곳", id: 12 },
        { name: "바다가 보이는 곳", id: 7 }
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
