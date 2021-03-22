<template>
  <div>
    <br />
    <br />
    <h3 style="text-align: left">{{ tag }}</h3>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="(item, index) in campsiteList" :key="index">
        <b-card
          title="캠핑장"
          img-src="https://gocamping.or.kr/upload/camp/3/thumb/thumb_720_6791ufBTEV41l7kb7jgUuvkF.jpg"
          img-alt="Image"
          img-top
          tag="article"
          style=""
          class=""
        >
          <b-card-text> 강원도 춘천시 </b-card-text>
          <b-button href="#" variant="primary">구경하기!</b-button>
        </b-card>
        <!-- <img height="70%" width="100%" src="@/assets/mainpage/campsite1.jpg" /> -->
      </swiper-slide>
      <!-- <swiper-slide>Slide 2</swiper-slide>
    <swiper-slide>Slide 3</swiper-slide>
    <swiper-slide>Slide 4</swiper-slide>
    <swiper-slide>Slide 5</swiper-slide>
    <swiper-slide>Slide 6</swiper-slide>
    <swiper-slide>Slide 7</swiper-slide>
    <swiper-slide>Slide 8</swiper-slide>
    <swiper-slide>Slide 9</swiper-slide>
    <swiper-slide>Slide 10</swiper-slide> -->
      <div class="swiper-pagination" slot="pagination"></div>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
  </div>
</template>

<script>
import { swiper, swiperSlide } from 'vue-awesome-swiper';
import 'swiper/swiper-bundle.css';

export default {
  name: 'swiper-example-loop-group',
  title: 'Loop mode with multiple slides per group',
  props: {
    tag: String,
  },
  components: {
    swiper,
    swiperSlide,
  },
  data() {
    return {
      campsiteList: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
      swiperOption: {
        slidesPerView: 7,
        spaceBetween: 20,
        slidesPerGroup: 7,
        loop: true,
        loopFillGroupWithBlank: false,
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        },
      },
    };
  },
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
