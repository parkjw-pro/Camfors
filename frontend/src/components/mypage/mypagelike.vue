<template>
  <div id="taglist">
    <h3 style="text-align: left; font-family: 'Hanna', sans-serif;"></h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="(item, index) in likeList" :key="index">
        <campsiteBlock :item="item" />
      </swiper-slide>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import campsiteBlock from "@/components/campsite/campsiteBlock";
import "swiper/css/swiper.css";

export default {
  name: "swiper-example-loop-group",
  title: "Loop mode with multiple slides per group",
  props: {
    likeList: Array
  },
  components: {
    Swiper,
    SwiperSlide,
    campsiteBlock
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 20,
        slidesPerGroup: 3,
        loop: false,
        loopFillGroupWithBlank: false,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },

        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev"
        }
      }
    };
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
.swiper {
  height: 100%;
  width: 100%;

  .swiper-slide {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-weight: bold;
    background-color: gray;
  }
}
</style>
<style scoped>
#taglist {
  margin-right: 20px;
  margin-left: 20px;
}
</style>
