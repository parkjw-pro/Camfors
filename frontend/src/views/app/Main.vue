<template>
  <div id = "main">
    <div>
      <video
        height="40%"
        width="100%"
        playsinline
        autoplay
        muted
        loop
        poster="@/assets/mainpage/main2.mp4"
      >
        <source :src="require('@/assets/mainpage/main.mp4')" type="video/mp4" />
      </video>
    </div>
    <!-- <div style="text-align: center; margin : 0 auto; width: 50%;"> -->
<<<<<<< HEAD
    <div
=======
    <div style="background-color: #FFFFF0"
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
     v-for="(item, index) in tagList" :key="index">
<swipertest :tag="item" /> 

    </div>

  </div>
</template>

<script>
import 'swiper/swiper-bundle.css'
import swipertest from '@/components/campsite/swipertest'


export default {
  name: 'Main',
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
<<<<<<< HEAD
      tagList: ['야경이 좋은 곳', '아이들이랑 가고 싶은 곳', '산책하기 좋은 곳'],
=======
      tagList: ['야경이 좋은 곳', '아이들이랑 가고 싶은 곳', '산책하기 좋은 곳', '주차하기 편한 곳'],
>>>>>>> f8e60257e4a2145bc75344de92f49ef66b90dec8
      swiperOption: {
        direction: 'vertical',
        pagination: {
          el: '.swiper-pagination',
          type: 'bullets',
        },
      },
    };
  },
  methods: {
    enlarge(event) {
      event.currentTarget.classList.add('large');
    },
  },
  created: async function() {
    console.log(this.tagList[0]);
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
